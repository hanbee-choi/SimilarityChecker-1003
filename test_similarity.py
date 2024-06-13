from unittest import TestCase
from similarity import Similarity


class TestSimilarity(TestCase):
    def setUp(self):
        super().setUp()
        self.similarity_checker = Similarity()

    def test_similarity(self):
        self.assertEqual(60, self.similarity_checker.score('AAA', 'DSA'))

    def test_similarity_zero_score(self):
        self.assertEqual(0, self.similarity_checker.score('A', 'BB'))

    def test_similarity_subscore_case(self):
        self.assertEqual(20.000000000000004, self.similarity_checker.score('AAABB', 'BAA'))
        self.assertEqual(30, self.similarity_checker.score('AA', 'AAE'))