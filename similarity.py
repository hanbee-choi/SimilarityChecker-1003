class Similarity:
    def __init__(self):
        pass

    def score_based_length(self, a, b):
        A = len(a) if len(a) > len(b) else len(b)
        B = len(b) if len(a) > len(b) else len(a)
        Gap = A - B
        return (1 - Gap / B) * 60

    def alpha_based_length(self, a, b):
        set1 = set(a)
        set2 = set(b)
        TotalCnt = len(set1.union(set2))

        SameCnt = 0
        for elem in set1:
            if elem in set2:
                SameCnt += 1

        return (SameCnt / TotalCnt) * 40
