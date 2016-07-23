Prop is a program that determines the validity of an argument (i.e. a list of premises and a single conclusion) expressed in propositional calculus.

# Background

An argument is *valid* if there is no interpretation of the propositional variables it is composed of that makes the premises all true and the conclusion false. In this sense, an interpretation can be understood as an assignment of True and False to the primitive propositional variables of the argument.


For example, consider the argument:
P1. A or B
P2. If A then C
P3. not-B

Conclusion: C

This argument is valid just if there is no way to assign True or False to the propositional variables A, B, and C so that, according to the normal logical meaning of 'or', 'if...then', and 'not', we could have P1, P2, and P3 coming out True and the conclusion coming out False.

So, imagine the premises are all true. Then, it is true that 'A or B'. So, either A is true, or B is true (or they are both true -- since 'or' in propositional logic is not exclusive). But, we know from P3 that not-B is True. So, B must be false. By P1, then, A must be true. And P2 tells us that if A is true, then C is true.

This reasoning tells us that if all the premises are true, then the conclusion must also be true. It is impossible for the premises to be true, and for the conclusion to fail to be true. This argument therefore satisfies the definition of validity.
 
In general, arguments may be much more complex than [P1, P2, P3, C] above, and their validity is harder to determine in a non-methodological way. In particular, there may be _many ways_ for their premises to be true -- just as 'A or B or C' can be true if any one of those propositional variables is true, or if any two of them are, or all of them are.

One proof method for establishing the validity of an argument is the proof tree. Prop produces a diagramatic representation of a proof tree, rendered in Latex, using the Latex package qtree.


#Definitions
===========
In order to comprehend the formulas inputted to it, Prop needs to include a lexer and a parser. 

* A *lexer* converts an input into tokens.

* A *parser* uses grammar rules to convert a set of tokens into a syntax tree. 

Yacc ('Yet Another Compiler Compiler'): ~1973, Johnson
Lex: ~1974, Schmidt and Lesk

Prop uses David Baezley's PLY (Python, Lex, Yacc) to compile propositional calculus.

PLY consists of two modules:

```python
	ply.lex
	ply.yacc
``` 
