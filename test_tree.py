"""
Tests for the expression => Qtree layer.
"""

from tree import PropVar, And, Or, Not
import os

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
        self.assertEqual(p.getSubTree().render(), Qtree('p').render())


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
        self.assertEqual(p.getSubTree().render(), expectedOutput.render())


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
        self.assertEqual(p.getSubTree().render(), expectedOutput.render())



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
        self.assertEqual(p.getSubTree().render(), expectedOutput.render())


    def _renderDebugOutput(self, actual, expected):
        tex = r"""\documentclass[10pt,english]{article}
\usepackage[T1]{fontenc}
\usepackage[latin9]{inputenc}
\usepackage{amssymb}
\usepackage{qtree}
\begin{document}
EXP

\Tree %s

ACTUAL

\Tree %s
\end{document}
        """ % (expected, actual)
        f = open("/tmp/output.tex", "w")
        f.write(tex)
        f.close()
        os.system("cd /tmp; pdflatex output.tex")


    def test_complexAnd(self):
        r"""
        And(And(p, q), r)
         |
        And(p, q)
         r
         |
         p
         q
        """
        p = And(And(PropVar('p'), PropVar('q')), PropVar('r'))
        expectedOutput = Qtree("And(And(p, q), r)",
                               [Qtree("And(p, q)\nr",
                                   [Qtree("p\nq")])])
        actual = p.getSubTree().render()
        expected = expectedOutput.render()
        self.assertEqual(actual, expected)


    def test_complexAndRightHand(self):
        r"""
        And(r, And(p, q))
         |
         r
        And(p, q)
         |
         p
         q
        """
        p = And(PropVar('r'), And(PropVar('p'), PropVar('q')))
        expectedOutput = Qtree("And(r, And(p, q))",
                               [Qtree("r\nAnd(p, q)",
                                   [Qtree("p\nq")])])
        actual = p.getSubTree().render()
        expected = expectedOutput.render()
        self.assertEqual(actual, expected)


    def test_complexDoubleAnd(self):
        r"""
        And(And(a, b), And(c, d))
         |
        And(a, b)
        And(c, d)
         |
         a
         b
         |
         c
         d
        """
        p = And(And(PropVar('a'), PropVar('b')),
                And(PropVar('c'), PropVar('d')))
        expectedOutput = Qtree("And(And(a, b), And(c, d))",
                               [Qtree("And(a, b)\nAnd(c, d)",
                                   [Qtree("a\nb",
                                       [Qtree("c\nd")])])])
        actual = p.getSubTree().render()
        expected = expectedOutput.render()
        self._renderDebugOutput(actual, expected)
        self.assertEqual(actual, expected)


