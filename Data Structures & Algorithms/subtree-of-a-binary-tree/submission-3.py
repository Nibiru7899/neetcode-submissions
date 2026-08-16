class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sametree(s, t):
            if not s and not t:
                return True

            if not s or not t:
                return False

            if s.val != t.val:
                return False

            return (
                sametree(s.left, t.left) and
                sametree(s.right, t.right)
            )

        if not subRoot:
            return True

        if not root:
            return False

        if sametree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )