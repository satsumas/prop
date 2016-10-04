#!/usr/bin/python

# Classes for truth functions of propositional logic expressions

class Simple_exp(object):
    """
    A simple expression, i.e. a propositional variable.
    
    Define value(self) when creating the propositional variable.
    """
    def __init__(self):
        pass


class Not_exp(object):
    """
    A expression that is a negation, i.e. negation has widest scope.
    """
    def __init__(self, rhs):
        self.rhs = rhs

    def value(self):
        if value(self.rhs) == True:
            return False
        if value(self.rhs) == False:
            return True


class Or_exp(object):
    """
    A disjunction: p OR q
    """
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def value(self):
        return (value(lhs) or value(rhs))


class And_exp(object):
    """
    A conjunction: p AND q
    """
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def value(self):
        return (value(lhs) and value(rhs))
        
