from typing import List

import numpy as np

from environment import Contributor, Project
from genetics import Gene


class Master:
    def __init__(self, contributors: List[Contributor], projects: List[Project]):
        self.contributors = contributors
        self.projects = projects
        self.max_days = max(project.latest for project in self.projects)
        self.genes = [Gene(contributors, projects, self.max_days) for _ in range(1)]
        for gene in self.genes:
            gene.greedy_init()
        self.fitnesses = [gene.fitness() for gene in self.genes]

    def advance_generation(self):
        pass

    def best_result(self):
        return self.genes[np.argmax(self.fitnesses)]

