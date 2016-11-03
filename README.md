Prop is a program that determines the validity of an argument in propositional logic. An argument, in this sense, is a list of premises and a single conclusion.

Having established the validity of an argument, Prop outputs a demonstration of this, rendered as a tree proof in Latex.


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

# Prop in action

When given the valid argument used above:
<img src = "/gifs/prop_example_validargument.gif">     






When given an invalid argument:
<img src = "/gifs/prop_example_invalidargument.gif">

#Definitions

In order to interpret the raw content inputted to it as propositional calculus syntax, Prop includes a lexer and a parser. 

* A *lexer* converts an input into tokens.

* A *parser* uses grammar rules to convert a set of tokens into a syntax tree. 

Prop uses a lexer (lexer.py) to convert raw input received via prompting into propositional logic. The lexer uses regular expressions to identify symbols from the propositional calculus, along with their precedence rules. Using these rules, the lexer 'tokenises' raw input into logical symbols.

Prop's parser takes the lexed input, and uses a BNF grammar to establish the type of each input. The type of an input can be either:

* `PropVar`: a propositional variable, the simmplest kind of expression
* `And_exp`: an expression composed of other expressions, in which 'And' has the widest scope. Something of the form (p And q). 
* `Or_exp`: an expression composed of other expressions, in which 'Or' has the widest scope. Something of the form (p Or q).
* `Not_exp`: an expression composed of other expressions, in which 'Not' has the widest scope. Something of the form NOT p.

    Note that the raw input may additionally include 'if ... then' (conditional) expressions, and 'iff' (biconditional) expressions. Logical equivalence rules <sup>[1](#myfootnote1)</sup> mean that we can treat these as a combination of the expressions above.
    
Types of expressions are given with Python classes, defined in tree.py.

Each class of expression has a method `sympy_me()`, which generates an object of the same type from Python's Sympy library -- a library for symbolic algebra. By using Sympy objects, the lexer can take advantage of Sympy's `satisfiable()` function. This takes a Boolean expression and, if there is some assignment of truth values to propositional variables in the expression that makes the overall expression true, returns that assignment. If such an assignment exists, the expression is said to be satisfiable in propsitinoal calculus. By considering `satisfiable()` applied to the conjunction of all premises and the the negation of the conclusion of the argument, we can establish whether or not the argument is valid -- i.e. if there exists an interpetation that makes all premises true and conclusion false.

Both the lexer and the parser in Prop are based on David Baezley's PLY (Python, Lex, Yacc). This, in turn, uses:

Yacc ('Yet Another Compiler Compiler'): ~1973, Johnson

Lex: ~1974, Schmidt and Lesk

# Run prop
Eventually prop will run on a web server. For now, to use it locally:

1. Clone this repo
2. Execute prop_yacc.py in an interactive python shell
3. When prompted, enter a forumla of propositional calculus. Prop will return a message indicating whether or not the argument is valid, and if it is _not_ valid, will state which assignment of truth values to propositional variables witnesses this by making premises true, conclusion false.

## Tips
* Bracket any binary connectived -- i.e. use `(p OR q)`, not `p OR q`
* propositional variables are expressed with lower case letters: a, b, ..., p, q, ... etc
* connectives are expressed in upper case: `AND`, `OR`, `ARROW`, `IFF`, `NOT` (to avoid PopVars being inadvertently found inside connectives)


<a name="myfootnote1">1</a>: All propositional formulas can be converted to a formula in [Disjunctive Normal Form](https://en.wikipedia.org/wiki/Disjunctive_normal_form#Conversion_to_DNF), which is to say a formula using just conjunctions (ANDs), disjunctions (ORs) and negations (NOTs).
