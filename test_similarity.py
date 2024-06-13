from unittest import TestCase
from similarity import Similarity


class TestSimilarity(TestCase):
    def test_similarity(self):
        similarity_checker = Similarity()
        result = similarity_checker.score('AAA', 'DSA')
        self.assertEqual(60, result)

    def test_similarity_zero_score(self):
        similarity_checker = Similarity()
        result = similarity_checker.score('A', 'BB')
        self.assertEqual(0, result)

    def test_similarity_subscore_case_1(self):
        similarity_checker = Similarity()
        result = similarity_checker.score('AAABB', 'BAA')
        self.assertEqual(20.000000000000004, result)

    def test_similarity_subscore_case_2(self):
        similarity_checker = Similarity()
        result = similarity_checker.score('AA', 'AAE')
        self.assertEqual(30, result)