from typing import List, Dict

from main import max_days
from environment import Contributor, Project


class Gene:
    def __init__(self, contributors, projects):
        # starting days for each project
        self.start_day = {project.name: -1 for project in projects}

        # what are the projects (contributors) are assigned for each contributor (project)
        self.projects_per_contributors = {contributor.name: [] for contributor in contributors}
        self.contributors_per_projects = {project.name: [] for project in projects}

    def greedy_init(self, sorted_projects: List[Project], contributors: List[Contributor]) -> None:
        contributors_availability_day = {contributor.name: 0 for contributor in contributors}

        for project in sorted_projects:
            for day in range(max_days):
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

    def display_gene(self):
        print('starting days of projects:')
        print(self.start_day)
        print('contributors assignment per each project:')
        print(self.contributors_per_projects)



