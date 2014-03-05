#!/usr/bin/python
"""
Grammar:


compound_prop:  | PROP_VAR
                | LPAREN compound_prop AND compound_prop RPAREN
                | LPAREN compound_prop OR compound_prop RPAREN
                | LPAREN compound_prop ARROW compound_prop RPAREN
                | LPAREN compound_prop IFF compound_prop RPAREN
                | NEG compound_prop

In the grammar, symbols such as PROP_VAR, NEG, AND, OR, ARROW and IFF are known
as terminals and correspond to raw input tokens. The identifier 'proposition'
refers to grammar rules comprised of a collection of terminals and other rules
and is a non-terminal. 

"""

import ply.yacc as yacc
from tree import Or, Not, And, PropVar

from lexer import tokens
def p_compound_prop_PROP_VAR(p):
    "compound_prop : PROP_VAR"
    p[0] = PropVar(p[1])

def p_compound_prop_NEG(p):
    "compound_prop : NEG compound_prop"
    p[0] = Not(p[2])

def p_compound_prop_AND(p):
    "compound_prop : LPAREN compound_prop AND compound_prop RPAREN"
    p[0] = And(p[2], p[4])

def p_compound_prop_OR(p):
    "compound_prop : LPAREN compound_prop OR compound_prop RPAREN"
    p[0] = Or(p[2], p[4])

def p_compound_prop_ARROW(p):
    "compound_prop : LPAREN compound_prop ARROW compound_prop RPAREN"
    p[0] = Or(Not(p[2]), p[4])

def p_compound_prop_IFF(p):
    "compound_prop : LPAREN compound_prop IFF compound_prop RPAREN"
    p[0] = Or(And(p[2], p[4]), And(Not(p[2]), Not(p[4])))


# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"

# Build the parser
parser = yacc.yacc()


"""
while True:
    try:
        s = raw_input('prop > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s) 
    print result.render()
"""

# The tex code that prints a tree
tex_str = r"""

\documentclass[10pt,english]{article}
\usepackage[T1]{fontenc}
\usepackage[latin9]{inputenc}
\usepackage{amssymb}
\usepackage{qtree}
\begin{document}
 %s
\end{document} """ 

s = raw_input('prop > ')
result = parser.parse(s) 
print result.render()


# Prints latex for tree that branches on connective AND or OR with widest scope.
if isinstance(result, And):
    print "string is And!"
    print "disjunct 1 is %s and disjunct 2 is %s" %(result.lhs.render(), result.rhs.render())
    tree = r"\Tree [.{%s} {%s\\%s} ])"  %  (result.render(), result.lhs.render(), result.rhs.render())
    tex_str = tex_str % (tree)


if isinstance(result, Or):
    print "its an Or!"
    print "disjunct 1 is %s and disjunct 2 is %s" %(result.lhs.render(), result.rhs.render())
    tree = "\Tree [.{%s} {%s} [.{%s} Sublevel ]])"  %  (result.render(), result.lhs.render(), result.rhs.render())
    tex_str = tex_str % (tree)


f = open("output.tex", "w")
f.write(tex_str)
f.write(str(result.render()))

f.close



