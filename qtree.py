"""
A presentation layer for generating LaTeX Qtree output.
"""

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
        self.root = root
        self.branches = branches


    def _escapedRoot(self):
        """
        Converts newlines into double backslashes and wraps curlies around it.
        """
        return "{%s}" % (self.root.replace("\n", r"\\"),)


    def render(self):
        """
        Sibling branches are rendered inside qtree by simply concatenating
        them.
        """
        results = []
        for branch in self.branches:
            results.append(branch.render())
        return "[.%s %s ]" % (self._escapedRoot(), " ".join(results))


    def renderTree(self):
        r"""
        Render a tree including the starting '\Tree' part.
        """
        return r"\Tree %s" % (self.render(),)
