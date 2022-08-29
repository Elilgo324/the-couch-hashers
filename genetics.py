from typing import List, Dict

import networkx as nx

import sorting
from environment import Contributor, Project


class Gene:
    def __init__(self, contributors, projects, max_days):
        self.contributors = contributors
        self.projects = projects
        self.max_days = max_days

        # starting days for each project
        self.start_day = {project.name: -1 for project in projects}
        self.projects_dict = {project.name: project for project in projects}

        # what are the projects (contributors) are assigned for each contributor (project)
        self.projects_per_contributors = {contributor.name: [] for contributor in contributors}
        self.contributors_per_projects = {project.name: [] for project in projects}

    def greedy_init(self) -> None:
        sorting.sort_projects_by_purple_score(self.projects)
        contributors_availability_day = {contributor.name: 0 for contributor in self.contributors}

        for project in self.projects:
            for day in range(self.max_days):
                available_contributors = [contributor for contributor in self.contributors
                                          if contributors_availability_day[contributor.name] >= day]

                for require_roll in project.required_rolls:
                    filtered_contributors = project.fit_contributors(available_contributors, require_roll)
                    # update assignment
                    for contributor in filtered_contributors:
                        self.projects_per_contributors[contributor.name].append(project.name)
                        self.contributors_per_projects[project.name].append(contributor)
                        self.start_day[project.name] = day
                        contributors_availability_day[contributor.name] += project.length
                        available_contributors.remove(contributor)
                        break

                if len(project.required_rolls) == len(self.contributors_per_projects[project.name]):
                    break

    def _is_assignment_legit(self, project: Project, contributors: List[Contributor]):
        graph = nx.Graph()
        graph.add_nodes_from([contributor for contributor in contributors], bipartite=0)
        graph.add_nodes_from([rr for rr in project.required_rolls], bipartite=1)
        graph.add_edges_from([(contributor, rr) for rr in project.required_rolls for contributor in contributors
                              if rr in contributor.skillz and contributor.skillz[rr] >= project.required_rolls[rr]])
        matching = nx.matching.maximal_matching(graph)
        return len(matching) == len(project.required_rolls)

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
        for project_name in self.start_day:
            project = self.projects_dict[project_name]
            if self._is_assignment_legit(project, self.contributors_per_projects[project_name]):
                score += project.score_on_day(self.start_day[project_name])
        return score

    def display_gene(self):
        print('starting days of projects:')
        print(self.start_day)
        print('contributors assignment per each project:')
        print(self.contributors_per_projects)
        print(self.fitness())
