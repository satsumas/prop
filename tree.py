#!/usr/bin/python

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


    def render_escaped_expansion(self):
        return r"{%s\\%s }" % (self.lhs.render(), self.rhs.render())


    def render_branch(self):
        # [.{%s} {%s\\%s} [. xxx ] ]
        # [.{%s} {%s\\%s} [. xxx ] ]
        return r"[.{%s} {%s\\%s } ]" % (self.render(), self.lhs.render_branch(), self.rhs.render_branch())
 

class PropVar(object):
    """
    E.g., 'p' or 'q'.
    """
    def __init__(self, name):
        self.name = name

    def render(self):
        return self.name

    def render_branch(self):
        return r"%s" % (self.render())


if __name__ == "__main__": #if the file is being run as a program (and not being imported as a module)
    expr = And(Or(PropVar('p'), PropVar('q')), PropVar('r'))
    print expr.render()


