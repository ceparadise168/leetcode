class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        res = defaultdict(list)  # score, ids
        scores = []
        scores_set = set()

        for i in range(len(report)):
            feedbacks = report[i].split()
            score = 0
            for feedback in feedbacks:
                if feedback in positive_feedback:
                    score += 3
                elif feedback in negative_feedback:
                    score -= 1

            heappush(res[score], student_id[i])

            if score not in scores_set:
                scores_set.add(score)
                heappush(scores, score*-1)

        out = []

        while len(out) < k:
            highest_score = heappop(scores) * -1
            while res[highest_score] and len(out) < k:
                out.append(heappop(res[highest_score]))
        return out