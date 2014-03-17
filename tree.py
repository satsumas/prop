#!/usr/bin/python

import ply.yacc as yacc

class Not(object):
    """
    NOT expression.  Can have one sub-expression.
    """
    def __init__(self, sub):
        self.sub = sub


    def render_escaped_expansion(self):
        return self.render()


    def render(self):
        return "Not(%s)" % (self.sub.render(),)
        #return "NOT " + self.sub.render()


class Or(object):
    """
    OR expression.  Can have sub-expressions.
    """
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


    def render(self):
        return "Or(%s, %s)" % (self.lhs.render(), self.rhs.render())
        #return "(" + self.lhs.render() + " OR " + self.rhs.render() + ")"


    def render_escaped_expansion(self):
        return self.render()


    def render_branch(self):
        return r"[.{%s} %s %s ]" % (self.render(), self.lhs.render_branch(), self.rhs.render_branch())
        

class And(object):
    """
    AND expression.  Can have sub-expressions.
    """
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


    def render(self):
        return "And(%s, %s)" % (self.lhs.render(), self.rhs.render())
        #return "(" + self.lhs.render() + " AND " + self.rhs.render() + ")"

    def root(self):
        return r".{%s}" % (self.render())

    def render_escaped_expansion(self):
        return r"{%s\\%s }" % (self.lhs.render(), self.rhs.render())

    def branch(self):
        # the recursive bit
        if isinstance (self.lhs, PropVar) and isinstance(self.rhs, PropVar):
            return r"%s   " % (self.render_escaped_expansion())  
        if isinstance (self.lhs, And) and isinstance(self.rhs, And):
            return r"[.%s [.%s %s ] ]" % (self.render_escaped_expansion(), "[." + self.lhs.render_escaped_expansion() + "[ [." + self.lhs.lhs.branch + " " + self.lhs.rhs.branch + " ]", self.rhs.branch() + " ]")  
 
    def render_branch(self):
        #root plus recursive bit
        return r"[%s %s ] " % (self.root(), self.branch())


class PropVar(object):
    """
    E.g., 'p' or 'q'.
    """
    def __init__(self, name):
        self.name = name

    def render(self):
        return self.name

    def branch(self):
        return r"%s" % (self.render())


if __name__ == "__main__": #if the file is being run as a program (and not being imported as a module)
    expr = And(Or(PropVar('p'), PropVar('q')), PropVar('r'))
    print expr.render()


