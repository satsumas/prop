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

import os, sys
import ply.yacc as yacc
from tree import Or_exp, Not_exp, And_exp, PropVar
from lexer import tokens, tokenise
from sympy.logic.inference import satisfiable

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

# Prompt the user for input
premise_number = int(raw_input('How many premises does your argument have? '))
print premise_number

premises = []
for i in range(1, premise_number +1):
    s_i = raw_input('Enter premise number: %s ' %  str(i))
    premises.append(s_i)
c = raw_input('Conclusion >')



# This function isn't currently used. It finds the propositional variables in the input.
def propvarfinder(string_list):
  propvars = []
  for string in (string_list):
      for tok in tokenise(string):
          if tok.type == 'PROP_VAR' and tok.value not in propvars:
              propvars.append(tok.value)
  return propvars

# Parse the user's inputted premises and conclusion
parsed_premises = []

for string in premises:
    parsed_premises.append(parser.parse(string))
c = parser.parse(c)


# The parser turns my raw input into Python objects from defined classes. 
# Each class has a function for turning its instances into Sympy objects.


def validity_checker(premise_conjunction, conclusion_negation):
    if satisfiable(premise_conjunction & conclusion_negation):
        print "This argument is not valid. Premises true, conlusion false if: ", satisfiable(premise_conjunction & conclusion_negation)
        return  satisfiable(premise_conjunction & conclusion_negation) 
    else:
        print "Argument valid!"
        return  satisfiable(premise_conjunction & conclusion_negation)

premise_conj = parsed_premises[0].sympy_me()
for premise in parsed_premises:
    premise_conj = premise_conj & premise.sympy_me()
    
print premise_conj

conclusion_neg = ~c.sympy_me()

validity_checker(premise_conj, conclusion_neg)

