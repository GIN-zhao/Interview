class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invertTree(self, root):
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


def isRepeatNum(nums_list):
    if len(set(nums_list)) == len(nums_list):
        return False
    return True


def isRepeatNumKdistance(nums_list, k):
    num_pos = dict()
    for i in range(len(nums_list)):
        if nums_list[i] in num_pos:
            if i - num_pos[nums_list[i]] < k:
                return True
        num_pos[nums_list[i]] = i
    return False


def isNeighborNum(nums_list, k, t):
    nums_pos = dict()
    for i in range(len(nums_list)):
        for j in range(nums_list[i] - t, nums_list[i] + t + 1):
            if nums_list[i] in nums_pos:
                if i - nums_pos[nums_list[i]] < k:
                    return True
        nums_pos[nums_list[i]] = i
    return False
