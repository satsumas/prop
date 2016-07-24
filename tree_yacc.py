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
from tree import Or, Not, And, PropVar

from lexer import tokens
# The following functions are based on David Baezley's parser. The indices that are used in the functions correspond to the words, in order, in the doc strings.

def p_compound_prop_PROP_VAR(p):
    "compound_prop : PROP_VAR"
    p[0] = PropVar(p[1])

# Here, p[0] is the result of calling PropVar on the 1st word (excluding the colon) in the doc string -- i.e. the PropVar itself.

def p_compound_prop_NEG(p):
    "compound_prop : NEG compound_prop"
    p[0] = Not(p[2])
# p[0] is Not(compound_prop)    

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
Tree:
\Tree %s
\end{document} """ 

s = raw_input('prop > ')


"""
TODO: this needs work -- figure out how to get fine-grained error handling. SHould be called if we have p_error
# Check raw input is well-formed -- binary connectives need to be encased in parentheses.
result = None
raw_binary_connectives = ["OR", "AND", "IFF", "ARROW"]
for bin_conn in raw_binary_connectives:
    if bin_conn in s:
        bin_conn_index = s.index(bin_conn)
        left_index = bin_conn_index -2
        right_index = bin_conn_index + 2
	if s[left_index] != "(" or s[right_index] != ")":
            error = "Binary connectives should be bracketed!"
            print error
	    break
        else:
            result = parser.parse(s) # result only chnages fron None if this error is not found
    print "We've parsed this as %s " % result
"""


result = parser.parse(s) 
print result


if result:
    print result.getSubTree().render()
    tex_str = tex_str % (result.getSubTree().render(),)
    f = open("output.tex", "w")
    f.write(tex_str)
    f.close()

    os.system("pdflatex output.tex > /dev/null && open output.pdf")
else:
    print "SOMETHING WENT WRONG :("


