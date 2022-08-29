from typing import List, Dict

import networkx as nx
import numpy as np

import sorting
from environment import Contributor, Project


class Gene:
    def __init__(self, contributors, projects, max_days):
        self.contributors = contributors
        self.projects = projects
        self.max_days = max_days

        # starting days for each project
        self.start_days = {project.name: -1 for project in projects}
        self.projects_dict = {project.name: project for project in projects}

        # what are the projects (contributors) are assigned for each contributor (project)
        self.projects_per_contributors = {contributor.name: [] for contributor in contributors}
        self.contributors_per_projects = {project.name: [] for project in projects}

    def greedy_init(self) -> None:
        sorting.sort_projects_by_purple_score(self.projects)
        contributors_availability_day = {contributor.name: -1 for contributor in self.contributors}

        for project in self.projects:
            for start_day in range(self.max_days):
                available_contributors = [contributor for contributor in self.contributors
                                          if contributors_availability_day[contributor.name] < start_day]
                if len(available_contributors) < len(project.required_rolls):
                    break

                graph = nx.Graph()
                graph.add_nodes_from([contributor for contributor in available_contributors], bipartite=0)
                graph.add_nodes_from([rr for rr in project.required_rolls], bipartite=1)
                graph.add_edges_from([(contributor, rr) for rr in project.required_rolls for contributor in available_contributors
                                      if rr in contributor.skillz and contributor.skillz[rr] >= project.required_rolls[
                                          rr]])
                matching = nx.matching.maximal_matching(graph)

                if len(matching) == len(project.required_rolls):
                    for (chosen_contributor, _) in matching:
                        self.projects_per_contributors[chosen_contributor.name].append(project.name)
                        self.contributors_per_projects[project.name].append(chosen_contributor)
                        self.start_days[project.name] = start_day
                        contributors_availability_day[chosen_contributor.name] += project.length
                        available_contributors.remove(chosen_contributor)

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
            for project_name in self.projects_per_contributors[contributor]:
                if self.start_days[project_name] < last_day:
                    return False
                last_day = self.start_days[project_name] + self.projects_dict[project_name].length
        return True

    def fitness(self):
        score = 0
        if not self._is_date_legit():
            return 0
        for project_name in self.start_days:
            project = self.projects_dict[project_name]
            if self._is_assignment_legit(project, self.contributors_per_projects[project_name]):
                score += project.score_on_day(self.start_days[project_name])
        return score

    def display_gene(self):
        print('starting days of projects:')
        print(self.start_days)
        print('contributors assignment per each project:')
        print(self.contributors_per_projects)
        print(self.fitness())
