from typing import List, Dict

from environment import Contributor, Project


def calculate_max_days(projects: List[Project]):
    return max([project.deadline + project.score for project in projects])


class Gene:
    def __init__(self, max_days, num_contributors):
        self.gene_mat = [[None for _ in range(num_contributors)] for _ in range(max_days)]

    def greedy_init(self, sorted_projects: Dict) -> None:
        self.gene_mat = [[]]