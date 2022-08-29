
class Gene:
    def __init__(self, max_days, num_contributors):
        self._gene_mat = [[None for _ in range(num_contributors)] for _ in range(max_days)]

    def apply_random_assignment(self, projects_contributors_skills: Dict) -> None:
        self._gene_mat = [[]]