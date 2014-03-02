#!/usr/bin/python

class Not(object):
    """
    NOT expression.  Can have one sub-expression.
    """
    def __init__(self, sub):
        self.sub = sub


    def render(self):
        return "NEG " + self.sub.render()



class Or(object):
    """
    OR expression.  Can have sub-expressions.
    """
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


    def render(self):
        return "(" + self.lhs.render() + " OR " + self.rhs.render() + ")"



class And(object):
    """
    AND expression.  Can have sub-expressions.
    """
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


    def render(self):
        return "(" + self.lhs.render() + " AND " + self.rhs.render() + ")"



class PropVar(object):
    """
    E.g., 'p' or 'q'.
    """
    def __init__(self, name):
        self.name = name


    def render(self):
        return self.name



if __name__ == "__main__": #if the file is being run as a program (and not being imported as a module)
    expr = And(Or(PropVar('p'), PropVar('q')), PropVar('r'))
    print expr.render()


