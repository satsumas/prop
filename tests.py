#!/usr/bin/python

from tree import PropVar, And, Or, Not
import os

def _renderOutput(actual):
    tex = r"""\documentclass[10pt,english]{article}
\usepackage[T1]{fontenc}
\usepackage[latin9]{inputenc}
\usepackage{amssymb}
\usepackage{qtree}
\begin{document}

\Tree %s

\end{document}
    """ % (actual,)
    f = open("/tmp/output.tex", "w")
    f.write(tex)
    f.close()
    os.system("cd /tmp; pdflatex output.tex && open /tmp/output.pdf")

t = Or(And(PropVar('p'), PropVar('q')), PropVar('q'))
_renderOutput(t.getSubTree().render())
