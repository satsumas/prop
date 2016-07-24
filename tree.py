#!/usr/bin/python

from qtree import Qtree
import copy

class TraversibleExpression(object):
    """
    An expression which knows how to generate its own tree for propositional
    logic.
    """
    def __init__(self):
        self.stack = []


    def getSubTree(self, elideRoot=False):
        """
        @return:  A Qtree instance.
        """
        myQtree = self.qtree(elideRoot=elideRoot)
        if len(self.stack) > 0:
            if not myQtree._branches:
                # Either, we can deal with the extra work immediately if we
                # have no further branches:
                myQtree._branches.append(
                        self.stack.pop().getSubTree(elideRoot=True))
            else:
                # Or, we have branches, in which case the work is deferred     		       # ('punted') deeper into the tree.
                self.punt(copy.copy(self.stack))
                myQtree = self.qtree(elideRoot=elideRoot)
        return myQtree


class Not(TraversibleExpression):
    """
    NOT expression.  Can have one sub-expression.
    """
    isComplex = False

    def __init__(self, sub):
        TraversibleExpression.__init__(self)
        self.sub = sub


    def render(self):
        return "Not(%s)" % (self.sub.render(),)
        #return "NOT " + self.sub.render()

    def branch(self):
        return r"%s" % (self.render())

    def qtree(self, elideRoot=False):
        return Qtree(self.render())

    def punt(self, stuff):
	    self.stack.extend(stuff)


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
        if elideRoot:
            text = ""
        else:
            text = self.render()
        return Qtree(text, [self.lhs.getSubTree(), self.rhs.getSubTree()])


    def punt(self, stuff):
        self.lhs.stack.extend(stuff)
        self.rhs.stack.extend(stuff)



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
        expand each conjunct in turn, one at a time.
        """
        if self.lhs.isComplex and self.rhs.isComplex:
            self.lhs.stack.append(self.rhs)

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


    def punt(self, stuff):
        self.lhs.stack.extend(stuff)
        self.rhs.stack.extend(stuff)


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


    def punt(self, stuff):
        self.stack.extend(stuff)


if __name__ == "__main__":
    expr = And(Or(PropVar('p'), PropVar('q')), PropVar('r'))
    print expr.render()
	# testing

