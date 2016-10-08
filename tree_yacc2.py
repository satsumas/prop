#!/usr/bin/python
"""
Grammar:

Expressed in Backus Naur Form:

compound_prop:  | PROP_VAR
                | LPAREN compound_prop AND compound_prop RPAREN
                | LPAREN compound_prop OR compound_prop RPAREN
                | LPAREN compound_prop ARROW compound_prop RPAREN
                | LPAREN compound_prop IFF compound_prop RPAREN
                | NEG compound_prop
"""

import os

import ply.yacc as yacc

from tree import Or_exp, Not_exp, And_exp, PropVar

from lexer import tokens, tokenise


# The following functions are based on David Baezley's parser. The indices that are used in the functions correspond to the words, in order, in the doc strings.
# The functions describe the relationship between different types of propositional formula, indicated by the BNF grammar above.
# They convert the tokens into instances of the classes from tree.py


def p_compound_prop_PROP_VAR(p):
    "compound_prop : PROP_VAR"
    p[0] = PropVar(p[1])

def p_compound_prop_NEG(p):
    "compound_prop : NEG compound_prop"
    p[0] = Not_exp(p[2])

def p_compound_prop_AND(p):
    "compound_prop : LPAREN compound_prop AND compound_prop RPAREN"
    p[0] = And_exp(p[2], p[4])

def p_compound_prop_OR(p):
    "compound_prop : LPAREN compound_prop OR compound_prop RPAREN"
    p[0] = Or_exp(p[2], p[4])

def p_compound_prop_ARROW(p):
    "compound_prop : LPAREN compound_prop ARROW compound_prop RPAREN"
    p[0] = Or_exp(Not_exp(p[2]), p[4])

def p_compound_prop_IFF(p):
    "compound_prop : LPAREN compound_prop IFF compound_prop RPAREN"
    p[0] = Or_exp(And_exp(p[2], p[4]), And_exp(Not_exp(p[2]), Not_exp(p[4])))


# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"

# Build the parser
parser = yacc.yacc()


s1 = raw_input('first premiss > ')
s2 = raw_input('second premiss > ')
c = raw_input('conclusion > ')


def propvarfinder(string1, string2, conclusion):
  propvars = []
  for string in (string1, string2, conclusion):
      for tok in tokenise(string):
          if tok.type == 'PROP_VAR' and tok.value not in propvars:
              propvars.append(tok.value)
  return propvars

propvarfinder(s1, s2, c)

prem1 = parser.parse(s1)
prem2 = parser.parse(s2)
conclusion = parser.parse(c)
print 'premises are %s and %s, conlusion is %s' % (s1, s2, c)

print 'these are your propvars:' 
print propvarfinder(s1, s2, c)

print "prem1 is a %s " % prem1


# The parser turns my raw input into Python objects from defined classes. 
# Each class has a function for turning its instances into Sympy objects.

"""
if __name__=="__main__":
    for k, v in globals().items():
        print k, '=', v
"""

print prem1.sympy_me()

print type(prem1.sympy_me())

print "    SYMPYING prem1!    :   " + str(prem1.sympy_me())

