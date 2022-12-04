class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]

        num_of_team = len(skill) // 2

        if sum(skill) % num_of_team != 0:
            return -1

        chemistry = 0
        avg_of_team = sum(skill) // num_of_team
        # print(avg_of_team)
        teams = []

        counts = Counter(skill)
        # print(counts)

        for sk, num_of_player in counts.items():
            target = avg_of_team - sk
            if target not in counts.keys():
                return -1

            while counts[sk] > 0 and counts[target] > 0:
                counts[sk] -= 1
                counts[target] -= 1
                chemistry += sk*target

        # print(counts)
        for v in counts.values():
            if v != 0:
                return -1
        return chemistry
    