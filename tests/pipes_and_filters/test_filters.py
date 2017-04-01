# coding=utf-8

from unittest2 import TestCase

from pipes_and_filters import filters

class TestFilters(TestCase):

    def test_lowercase_lowercases_all_letters(self):
        self.assertEqual(
          filters.lowercase('Oh, Hello!'),
          'oh, hello!'
        )

    def test_exclamation_points_adds_exclamations(self):
        self.assertEqual(
          filters.exclamation_points('Oh, Hello!'),
          'Oh, Hello!!!!'
        )

    def test_sparkles_emoji_adds_sparkles(self):
        self.assertEqual(
          filters.sparkles_emoji('Oh, Hello!'),
          '✨  Oh, Hello! ✨ '
        )

    def test_no_fun_tests_if_message_contains_no_fun(self):
        self.assertFalse(
          filters.no_fun('functional programming'),
        )
        self.assertTrue(
          filters.no_fun('serverless architecture'),
        )

    def test_not_too_excited_tests_if_message_has_four_exclamation_points(self):
        self.assertFalse(
          filters.not_too_excited('serverless is so rad!!!!'),
        )
        self.assertTrue(
          filters.no_fun('serverless is quite nice.'),
        )

