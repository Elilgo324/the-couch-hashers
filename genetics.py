from typing import List, Dict

import networkx as nx

from environment import Contributor, Project


def calculate_max_days(projects: List[Project]):
    return max([project.deadline + project.score for project in projects])


class Gene:
    def __init__(self, max_days, num_contributors):
        self.start_day = {project: -1 for project in projects}
        self.worked_on = {project: [] for project in projects}
        self.working_on = {contributor: [] for contributor in contributors}

    def _is_assignment_legit(self, project: Project, contributors: List[Contributor]):
        graph = nx.Graph()
        graph.add_nodes_from([contributor for contributor in contributors], bipartite=0)
        graph.add_nodes_from([rr for rr in project.required_rolls], bipartite=1)
        graph.add_edges_from([(contributor, rr) for rr in project.required_rolls for contributor in contributors
                              if rr in contributor.skillz and contributor.skillz[rr] > project.required_rolls[rr]])
        return nx.matching.maximal_matching(graph) == len(project.required_rolls)

    def _is_date_legit(self):
        for contributor in self.working_on:
            last_day = -1
            for project in self.working_on[contributor]:
                if self.start_day[project] <= last_day:
                    return False
                last_day = self.start_day[project] + project.length
        return True

    def fitness(self):
        score = 0
        for project in self.start_day:
            if self._is_assignment_legit(project, self.working_on[project]):
                score += project.score_on_day(self.start_day[project])
        return score

    def greedy_init(self, sorted_projects: Dict) -> None:
        self.gene_mat = [[]]