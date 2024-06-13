class Similarity:
    def __init__(self):
        pass

    def score(self, a, b):
        A = len(a) if len(a) > len(b) else len(b)
        B = len(b) if len(a) > len(b) else len(a)
        Gap = A - B
        return (1 - Gap / B) * 60
