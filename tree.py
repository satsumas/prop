#!/usr/bin/python

from qtree import Qtree

class TraversibleExpression(object):
    """
    An expression which knows how to generate its own tree for propositional
    logic.
    """
    def __init__(self):
        self._stack = []


    def addWork(self, expression):
        """
        @arg expression: An Expression.
        """
        # TODO We might want to try changing this to 'insert(0, ...' to switch
        # to DFS
        self._stack.append(expression)


    def popWork(self, expression):
        """
        Get the next expression which needs dealing with.
        """
        # Get last thing off the list
        return self._stack.pop()


    def hasWork(self):
        """
        Is there any work left to do?
        """
        return len(self._stack) > 0


    def getSubTree(self, elideRoot=False):
        """
        @return:  A Qtree instance.
        """
        myQtree = self.qtree(elideRoot=elideRoot)
        if self._extraWork:
            # Either, we can deal with the extra work immediately if we
            # ourselves have no further branches:
            if not myQtree._branches:
                myQtree._branches.append(
                        self._extraWork.getSubTree(elideRoot=elideRoot))
                self._extraWork = None
            # Or, we have branches, in which case we must punt the work down
            # the tree.  How do we do this???
        return myQtree



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


    def workToDo(self):
        """
        Return a list of expressions which still need to be evaluated.
        """
        return [self.lhs, self.rhs]


    def qtree(self, elideRoot=False):
        """
        For And expressions, render a subtree with each of the conjuncts
        separated by a newline as the head, and then proceed to recursively
        expand each conjunct in turn, one at a time.
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


