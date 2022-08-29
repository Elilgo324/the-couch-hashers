from typing import List

from environment import Project, Contributor


def sort_projects_by_purple_score(projects: List[Project]):
    projects.sort(key=lambda p: p.purple_score)


def find_most_fit_contributor(contributors: List[Contributor], project: Project, required_roll: str):
    filtered_contributors = [contributor for contributor in contributors if
                             contributor.skillz[required_roll] - project.required_rolls[required_roll] >= 0]
    filtered_contributors.sort(key=lambda c: max(c.skillz[required_roll] - project.required_rolls[required_roll], -.5))
    return filtered_contributors

