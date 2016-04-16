"""
Tests for qtree presentation layer.
"""

from unittest import TestCase
from qtree import Qtree

class QtreeTests(TestCase):
    """
    Direct tests for generating Qtree output from Qtree objects.
    """
    def test_trivial(self):
        """
        head
        """
        q = Qtree("head")
        self.assertEqual(q.render(), r"[.{head}  ]")


    def test_oneBranch(self):
        """
        head
         |
        tail
        """
        q = Qtree("head", [Qtree("tail")])
        self.assertEqual(q.render(), r"[.{head} [.{tail}  ] ]")


    def test_twoBranches(self):
        r"""
        head
         |  \
        tail tail2
        """
        q = Qtree("head", [Qtree("tail"), Qtree("tail2")])
        self.assertEqual(q.render(), r"[.{head} [.{tail}  ] [.{tail2}  ] ]")


    def test_twoBranchesDeep(self):
        r"""
        head
         |
        tail
         |
        tail2
        """
        q = Qtree("head", [
                Qtree("tail", [
                    Qtree("tail2")])])
        self.assertEqual(q.render(), r"[.{head} [.{tail} [.{tail2}  ] ] ]")


    def test_newlines(self):
        r"""
        head
         |
        tailpartA
        tailpartB
        """
        q = Qtree("head", [Qtree("tailpartA\ntailpartB")])
        self.assertEqual(q.render(), r"[.{head} [.{tailpartA\\tailpartB}  ] ]")
