"""
A presentation layer for generating LaTeX Qtree output.
"""
import copy

class Qtree(object):
    r"""
    A qtree is rendered as a root with some branches:

     ROOT
     / \
    b1  b2 ...
    """
    def __init__(self, root, branches=[]):
        """
        @arg root:  A string which is rendered as "ROOT" in the example above.

        @arg branches:  A list of Qtree objects.
        """
        self._root = root
        self._branches = branches


    def addBranch(self, branch):
        """
        Add a new branch.

        @param branch:  A Qtree.
        """
        self._branches.append(branch)


    def _escapedRoot(self):
        """
        Converts newlines into double backslashes and wraps curly brackets around it.
        """
        return "{%s}" % (self._root.replace("\n", r"\\"),)


    def render(self, seen=None):
        """
        Sibling branches are rendered inside qtree by simply concatenating
        them.
        """
        if seen is None:
            seen = [self]
        else:
            seen.append(self)

        results = []
        def _debug(q):
            print repr(q._root) + ":" + hex(id(q)), "branches:", [b._root + ":" + hex(id(b)) for b in q._branches]
	_debug(self)
        for branch in self._branches:
            if branch not in seen:
                seen.append(branch)
                results.append(branch.render(seen=copy.copy(seen)))
            else:
                print "SEEN YOU BEFORE! ==="
		_debug(branch)
		print "===================="
        return "[.%s %s ]" % (self._escapedRoot(), " ".join(results))




