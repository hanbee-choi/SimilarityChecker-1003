class Similarity:
    def __init__(self):
        pass

    def score(self, a, b):
        gap = len(a) - len(b)
        B = len(b) if len(a) > len(b) else len(a)
        return (1 - gap / B) * 60
