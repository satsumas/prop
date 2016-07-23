#!/usr/bin/python

"""
To do:
    prompt for as many variables as required.

request multiple propositions -- call them premises -- evaluate their truth values.
request conclusion, and evaluate its conclusion.
spit out validity.
"""

"""
A Class for arguments


class Argument(object):
        def __init__(self, premise1, premise2, conclusion, validity, proof):
            self.premise1 = premise1
            self.premise2 = premise2
            self.conclusion = conclusion
            self.proof = proof
        def validity(self):
            if result(premise1) == True and result(premise2) == True and result(conclusion) == False:
                return "invalid"
            else:
                return "valid"
                          
"""

premise1 = raw_input("Enter first premise (lower case only) ")
premise2 = raw_input("Enter second premise (lower case only) ")

#Store the value of p, q and r as p_val, q_val and r_val.
#Currently just three propositional variables used in formulas.
p_val = raw_input("What is the value of p? Enter T or F. ")
if p_val in ["T", "t"]:
    p = True 
elif p_val in ["F","f"]:
    p = False
else:
    print "Please enter T or F"

q_val = raw_input("What is the value of q? Enter T or F. ")
if q_val in ["T", "t"]:
    q = True
elif q_val in ["F", "f"]:
    q = False
else:
    print "Please enter T or F"

r_val = raw_input("What is the value of r? Enter T or F. ")
if r_val in ["T", "t"]:
    r = True
elif r_val in ["F", "f"]:
    r = False
else:
    print "Enter T or F"

"""parser for binary connectives.
Will only accept expressions with two variables
and a single connective: or, and, arrow, iff.
"""

tokens1 = premise1.split(" ")
print tokens1

tokens2 = premise2.split(" ")
print tokens2


def fetch_value(token):
    if token == "p": #if we find a p, return whatever bool we set p to.
        return p

    elif token == "q":
        return q

    elif token == "r":
        return r

for token in tokens1:
    print token, str(fetch_value(token)) #bugchecking
for token in tokens2:
    print token, str(fetch_value(token))

# we want k to be the index of the connective in the list tokens...
# tokens[k] = "connective -- or, and, etc."

def value_for_atomic(lst):
    for (i, token) in enumerate(lst):
        if token == "or":
            def f(a, b): #f is truth-function for binary connective.
                return a or b
        elif token == "and":
            def f(a, b):
                return a and b
        elif token == "arrow":
            def f(a, b):
                return ((not a) or b)
        elif token == "iff":
            def f(a, b):
                return (a and b) or (not a and not b)
        elif token == "not":
            def g(b): #g is truth-function for neg.
                return not b
        else:
            continue
        flank_1 = lst[i - 1]
        flank_2 = lst[i + 1]
        if token == "or" or token == "and" or token == "arrow" or token == "iff":    
            return f(fetch_value(flank_1), fetch_value(flank_2))
        elif token == "not":
            return  g(fetch_value(flank_2))
        
value_for_atomic(tokens1)
value_for_atomic(tokens2)

print value_for_atomic(tokens1)
print value_for_atomic(tokens2)


"""parser for monadic connective (i.e. not)"""



"""print the result"""

def print_result(X):
    if value_for_atomic(X) == True:
        concatenation = ""
        for token in X:
            concatenation = concatenation + " " + str(token)
        print "The proposition '%s' is TRUE" %concatenation
        return True

    elif value_for_atomic(X) == False:
        concatenation = ""
        for token in X:
            concatenation = concatenation + " " + str(token)
        print "The proposition  '%s' is FALSE" %concatenation
        return False

print_result(tokens1)
print_result(tokens2)



