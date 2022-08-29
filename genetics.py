from typing import List, Dict

import networkx as nx
from environment import Contributor, Project
from sorting import sort_projects_by_purple_score


class Gene:
    def __init__(self, contributors, projects, max_days):
        self.contributors = contributors
        self.projects = projects
        self.max_days = max_days

        # starting days for each project
        self.start_day = {project.name: -1 for project in projects}

        # what are the projects (contributors) are assigned for each contributor (project)
        self.projects_per_contributors = {contributor.name: [] for contributor in contributors}
        self.contributors_per_projects = {project.name: [] for project in projects}

    def greedy_init(self) -> None:
        sorted_projects = sort_projects_by_purple_score(self.projects)
        contributors = self.contributors

        contributors_availability_day = {contributor.name: 0 for contributor in contributors}

        for project in sorted_projects:
            for day in range(self.max_days):
                available_contributors = [contributor for contributor in contributors
                                          if contributors_availability_day[contributor.name] >= day]
                sorted_contributors = project.get_greedy_contributors_assignment(available_contributors)

                # update assignment
                for contributor in sorted_contributors:
                    self.projects_per_contributors[contributor.name] = project.name
                    self.contributors_per_projects[project.name] = contributor
                    self.start_day[project.name] = day
                    contributors_availability_day[contributor.name] += project.length
                    break

    def _is_assignment_legit(self, project: Project, contributors: List[Contributor]):
        graph = nx.Graph()
        graph.add_nodes_from([contributor for contributor in contributors], bipartite=0)
        graph.add_nodes_from([rr for rr in project.required_rolls], bipartite=1)
        graph.add_edges_from([(contributor, rr) for rr in project.required_rolls for contributor in contributors
                              if rr in contributor.skillz and contributor.skillz[rr] > project.required_rolls[rr]])
        return nx.matching.maximal_matching(graph) == len(project.required_rolls)

    def _is_date_legit(self):
        for contributor in self.projects_per_contributors:
            last_day = -1
            for project in self.projects_per_contributors[contributor]:
                if self.start_day[project] <= last_day:
                    return False
                last_day = self.start_day[project] + project.length
        return True

    def fitness(self):
        score = 0
        for project in self.start_day:
            if self._is_assignment_legit(project, self.contributors_per_projects[project]):
                score += project.score_on_day(self.start_day[project])
        return score

    def display_gene(self):
        print('starting days of projects:')
        print(self.start_day)
        print('contributors assignment per each project:')
        print(self.contributors_per_projects)