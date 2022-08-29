from typing import Dict


class Contributor:
    def __init__(self, name: str, skills: Dict):
        self._name = name
        self._skills = skills

    def improve_skill(self, skill_name: str):
        self._skills[skill_name] += 1


class Project:
    def __init__(self, reward: int, deadline: int, length: int, required_skills: Dict):
        self._reward = reward
        self._deadline = deadline
        self._length = length
        self._required_skills = required_skills

    @property
    def reward(self):
        return self._reward

    @property
    def deadline(self):
        return self._deadline

    @property
    def length(self):
        return self._length

    @property
    def required_skills(self):
        return self._required_skills
