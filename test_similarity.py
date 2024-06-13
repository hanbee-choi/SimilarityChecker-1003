from unittest import TestCase
from similarity import Similarity


class TestSimilarity(TestCase):
    def test_similarity(self):
        sim = Similarity()
        result = sim.score('AAA', 'DSA')
        self.assertEqual(0, result)