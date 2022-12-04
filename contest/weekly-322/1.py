class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        words = sentence.split()

        q = []

        for word in words:
            q.append(word[0])
            q.append(word[-1])


        q2 = []
        while q:
            e = q.pop()
            if q2 and q2[-1] == e:
                q2.pop()
            else:
                q2.append(e)

        # print(q2)
        if not q2:
            return True
        return False