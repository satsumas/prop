#!/usr/bin/python

from qtree import Qtree

class TraversibleExpression(object):
    """
    An expression which knows how to generate its own tree for propositional
    logic.
    """
    def __init__(self):
        self._extraWork = None


    def addWork(self, expression):
        self._extraWork = expression


    def getSubTree(self, elideRoot=False):
        if self._extraWork:
            print "returning extraWork", self._extraWork.render()
            response = self._extraWork.getSubTree(elideRoot=elideRoot)
            self._extraWork = None
            return response
        else:
            print "returning qtree", self.render()
            return self.qtree(elideRoot=elideRoot)



class Not(TraversibleExpression):
    """
    NOT expression.  Can have one sub-expression.
    """
    def __init__(self, sub):
        TraversibleExpression.__init__(self)
        self.sub = sub


    def render(self):
        return "Not(%s)" % (self.sub.render(),)
        #return "NOT " + self.sub.render()


class Or(TraversibleExpression):
    """
    OR expression.  Can have sub-expressions.
    """
    isComplex = True

    def __init__(self, lhs, rhs):
        TraversibleExpression.__init__(self)
        self.lhs = lhs
        self.rhs = rhs


    def render(self):
        return "Or(%s, %s)" % (self.lhs.render(), self.rhs.render())
        #return "(" + self.lhs.render() + " OR " + self.rhs.render() + ")"


    def qtree(self, elideRoot=False):
        return Qtree(self.render(), [self.lhs.getSubTree(), self.rhs.getSubTree()])



class And(TraversibleExpression):
    """
    AND expression.  Can have sub-expressions.
    """
    isComplex = True

    def __init__(self, lhs, rhs):
        TraversibleExpression.__init__(self)
        self.lhs = lhs
        self.rhs = rhs


    def render(self):
        return "And(%s, %s)" % (self.lhs.render(), self.rhs.render())


    def _newlineHead(self):
        return "%s\n%s" % (self.lhs.render(), self.rhs.render())


    def qtree(self, elideRoot=False):
        """
        For And expressions, render a subtree with each of the conjuncts
        separated by a newline as the head, and then proceed to recursively
        expand each conjunct in turn.
        """
        if self.lhs.isComplex and self.rhs.isComplex:
            self.lhs.addWork(self.rhs)

        subQtreeBranches = []
        if self.lhs.isComplex:
            subQtreeBranches.append(self.lhs.getSubTree(elideRoot=True))
        elif self.rhs.isComplex:
            subQtreeBranches.append(self.rhs.getSubTree(elideRoot=True))

        innerQtree = Qtree(self._newlineHead(), subQtreeBranches)
        if elideRoot:
            return innerQtree
        else:
            return Qtree(self.render(), [innerQtree])



class PropVar(TraversibleExpression):
    """
    E.g., 'p' or 'q'.
    """
    isComplex = False

    def __init__(self, name):
        TraversibleExpression.__init__(self)
        self.name = name


    def render(self):
        return self.name


    def branch(self):
        return r"%s" % (self.render())


    def qtree(self, elideRoot=False):
        """
        Given the expression that is self, return a Qtree which can be rendered
        into the LaTeX we want to output.
        """
        return Qtree(self.render())


if __name__ == "__main__": #if the file is being run as a program (and not being imported as a module)
    expr = And(Or(PropVar('p'), PropVar('q')), PropVar('r'))
    print expr.render()


