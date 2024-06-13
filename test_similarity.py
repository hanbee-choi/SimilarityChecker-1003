from unittest import TestCase
from similarity import Similarity


class TestSimilarity(TestCase):
    def setUp(self):
        super().setUp()
        self.similarity_checker = Similarity()

    def test_similarity(self):
        self.assertEqual(60, self.similarity_checker.score_based_length('AAA', 'DSA'))
        self.assertEqual(40, self.similarity_checker.alpha_based_length('ASD', 'DSA'))

    def test_similarity_zero_score(self):
        self.assertEqual(0, self.similarity_checker.score_based_length('A', 'BB'))
        self.assertEqual(0, self.similarity_checker.score_based_length('A', 'BB'))

    def test_similarity_subscore_case(self):
        self.assertEqual(20.000000000000004, self.similarity_checker.score_based_length('AAABB', 'BAA'))
        self.assertEqual(40, self.similarity_checker.alpha_based_length('AAABB', 'BAA'))
        self.assertEqual(30, self.similarity_checker.score_based_length('AA', 'AAE'))
        self.assertEqual(20, self.similarity_checker.alpha_based_length('AA', 'AAE'))