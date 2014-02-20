#!/usr/bin/python

"""
To do:
    prompt for as many variables as required.
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
            need to return "invalid" 
                            only if all premises are true and conclusion false
            if premise1 == True and premise2 == True and 
"""

s = raw_input("Enter proposition (lower case only) ")

#convert 'if...then...' in s  to '...arrow...'.


#Store the value of p, q and r as p_val, q_val and r_val.
p_val = raw_input("What is the value of p? Enter T or F. ")
if p_val in ["T", "t"]:
    p = True #p is the bool that is the value of "P"
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
will only accept expressions with two variables
and a single connective: or, and, arrow, iff.
"""

tokens = s.split(" ")
print tokens

def fetch_value(token):
    if token == "p": #if we find a p, return whatever bool we set p to.
        return p

    elif token == "q":
        return q

    elif token == "r":
        return r

for token in tokens:
    print token, str(fetch_value(token)) #bugchecking


# we want k to be the index of the connective in the list tokens...
# tokens[k] = "connective -- or, and, etc."


for (i, token) in enumerate(tokens):
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
    flank_1 = tokens[i - 1]
    flank_2 = tokens[i + 1]
    if token == "or" or token == "and" or token == "arrow" or token == "iff":    
        result = f(fetch_value(flank_1), fetch_value(flank_2))
    elif token == "not":
        result = g(fetch_value(flank_2))


print result


"""parser for monadic connective (i.e. not)"""



"""print the result"""

def print_result(X):
    if X == True:
        print "the proposition '%s' is TRUE" %s
        return True

    elif X == False:
        print "oh no! The proposition  '%s' is FALSE" %s
        return False

print_result(result)

