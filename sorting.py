from typing import List

from environment import Project, Contributor


def sort_projects_by_purple_score(projects: List[Project]):
    projects.sort(key=lambda p: p.purple_score)

