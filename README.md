Prop is a program that determines the validity of an argument (i.e. a list of premises and a single conclusion) expressed in propositional calculus.

An argument is *valid* if there is no interpretation of its variables according to which the premises are all true and the conclusion is false. 

Definitions
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
