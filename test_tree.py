"""
Tests for the expression => Qtree layer.
"""

from tree import PropVar, And, Or, Not

from unittest import TestCase
from qtree import Qtree

class ConversionTests(TestCase):
    """
    Test converting various expressions into Qtree instances.
    """
    def test_propvar(self):
        """
        Rendering a PropVar trivially renders just that PropVar in a tree on
        its own.
        """
        p = PropVar('p')
        self.assertEqual(p.qtree().render(), Qtree('p').render())


    def test_or(self):
        r"""
        Rendering an Or renders the Or expression in the root and branches on
        each of the subexpressions.

        Or(p, q)
          /  \
         p    q
        """
        p = Or(PropVar('p'), PropVar('q'))
        expectedOutput = Qtree("Or(p, q)", [Qtree("p"), Qtree("q")])
        self.assertEqual(p.qtree().render(), expectedOutput.render()) 


    def test_and(self):
        r"""
        Rendering an And renders the And expression in the root and both of the
        conjuncts newline-separated in a single subtree.

        And(p, q)
           |
           p
           q
        """
        p = And(PropVar('p'), PropVar('q'))
        expectedOutput = Qtree("And(p, q)", [Qtree("p\nq")])
        self.assertEqual(p.qtree().render(), expectedOutput.render()) 



    def test_complexOr(self):
        r"""
           Or(p, Or(z, q))
          /  \
         p  Or(z, q)
              /  \
             z    q
        """
        p = Or(PropVar('p'), (Or(PropVar('z'), PropVar('q'))))
        expectedOutput = Qtree("Or(p, Or(z, q))",
                               [Qtree("p"), Qtree("Or(z, q)",
                                                  [Qtree("z"), Qtree("q")])])
        self.assertEqual(p.qtree().render(), expectedOutput.render()) 



    def test_complexAnd(self):
        r"""
        WANT

        And(And(p, q), r)
         |
        And(p, q)
         r
         |
         p
         q

        GOT
        And(And(p, q), r)
         |
        And(p, q)
         r
        """
        p = And(And(PropVar('p'), PropVar('q')), PropVar('r'))
        expectedOutput = Qtree("And(And(p, q), r)",
                               [Qtree("And(p, q)\nr",
                                   [Qtree("p\nq")])])
        self.assertEqual(p.qtree().render(), expectedOutput.render()) 


