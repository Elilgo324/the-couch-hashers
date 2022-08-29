from typing import List

from environment import Contributor, Project
from genetics import Gene


class Master:
    def __init__(self, contributors: List[Contributor], projects: List[Project]):
        self.contributors = contributors
        self.projects = projects
        self.max_days = max(project.latest for project in self.projects)
        self.genes = [Gene(contributors, projects, self.max_days)]
        for gene in self.genes:
            gene.greedy_purple_init()

    def best_result(self):
        return self.genes[0]

