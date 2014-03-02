#!/usr/bin/python
"""
Grammar:
proposition: NEG proposition
           | (proposition AND proposition)
           | (proposition OR proposition)
           | (proposition ARROW proposition)
           | (proposition IFF proposition)
           | PROP_VAR

In the grammar, symbols such as PROP_VAR, NEG, AND, OR, ARROW and IFF are known as terminals and correspond to raw input tokens. The identifier 'proposition'  refers to grammar rules comprised of a collection of terminals and other rules and is a non-terminal. 
"""

import ply.yacc as yacc
from tree import Or, Not, And, PropVar

from lexer import tokens
def p_proposition_NEG(p):
    "proposition : NEG proposition"
    p[0] = Not(p[2])

def p_proposition_AND(p):
    "proposition : proposition AND proposition"
    p[0] = And(p[1], p[3])

def p_proposition_OR(p):
    "proposition : proposition OR proposition"
    p[0] = Or(p[1], p[3])

def p_proposition_ARROW(p):
    "proposition : proposition ARROW proposition"
    p[0] = Or(Not(p[1]), p[3])

def p_proposition_IFF(p):
    "proposition : proposition IFF proposition"
    p[0] = Or(And(p[1], p[3]), And(Not(p[1]), Not(p[3])))

def p_proposition_PROP_VAR(p):
    "proposition : PROP_VAR"
    p[0] = PropVar(p[1])

def p_proposition_expr(p):
    'proposition : LPAREN proposition RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('prop > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print result.render()
