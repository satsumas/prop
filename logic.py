#!/usr/bin/python


"""enter proposition in p, q and r to evaluate"""
s = raw_input("Enter proposition ")

p_val = raw_input("What is the value of p? Enter T or F. ")
if p_val == "T":
    p = True
elif p_val == "F":
    p = False
else:
    print "Please enter T or F"

q_val = raw_input("What is the value of q? Enter T or F. ")
if q_val == "T":
    q = True
elif q_val == "F":
    q = False
else:
    print "Please enter T or F"


r_val = raw_input("What is the value of r? Enter T or F. ")
if r_val == "T":
    r = True
elif r_val == "F":
    r = False
else:
    print "Enter T or F"

"""parser
will only accept expressions with two variables
and a single connective, and or or.
"""

tokens = s.split(" ")
print tokens

def fetch_value(token):
    if token == "p":
        return p

    elif token == "q":
        return q

    elif token == "r":
        return r

# we want k to be the index of "or" in the list tokens...
# tokens[k] = "or"

for (i, token) in enumerate(tokens):
    if token == "or":
        def f(a, b):
            return a or b
    elif token == "and":
        def f(a, b):
            return a and b
    else:
        continue
    flank_1 = tokens[i - 1]
    flank_2 = tokens[i + 1]
    result = f(fetch_value(flank_1), fetch_value(flank_2))


"""convert to disjunctive normal form"""


"""print the result"""

def print_result(X):
    if X == True:
        print "omg, %s!! it's true!!wwooohooooooooooooooooooooooooooooooooooooooooooooooooooooooppppppp" %s
        return True

    elif X == False:
        print "oh no! %s is  FALSE!!!!!!!!!!" %s
        return False

print_result(result)

