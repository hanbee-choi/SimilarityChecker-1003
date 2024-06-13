from unittest import TestCase
from similarity import Similarity


class TestSimilarity(TestCase):
    def test_similarity(self):
        similarity_checker = Similarity()
        result = similarity_checker.score('AAA', 'DSA')
        self.assertEqual(60, result)
