class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(tree, target):
  answer = []
  parent = []






  return answer


print(solution([4, 2, 6, 1, 3, 5, 7], 2))

# Definition for a binary tree node.

class TreeNode:
  tree = []
  parent_array = [0] * 1001

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def parent(self):
    TreeNode.tree.append(self.val)
    if self.left != None :
      TreeNode.parent_array[self.left.val] = self.val
      TreeNode.parent(self.left)

    if self.right != None :
      TreeNode.parent_array[self.right.val] = self.val
      TreeNode.parent(self.right)
    return self.val

class Solution:
  def toTree(self, splited, parent):
    for s in splited:
      for p in parent:
        if s == p:


      tree = TreeNode(s, TreeNode(parent.index(s))




      def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
    print(TreeNode.parent(root))
    print(TreeNode.tree)
    parent = TreeNode.parent_array[0:len(TreeNode.tree)+1]
    print(parent)

    print("======")
    splited = [target]
    left_parent = parent[::] # array 복사

    for i, p in enumerate(parent):
      print(i, p)
      if p == target and i <= target: # 부모가 target과 같고 그 수가 target 보다 작으면
        splited.append(i)
      elif p == target and i > target : # 부모가 target 과 같지만 그 수가 target  보다 크면
        left_parent[i] = parent[target] # 부모를 위로 옮겨주기
    print(splited)
    print(left_parent)

    splited = sorted(splited)
    # splited = splited.sort(reverse = True)
    print(splited)





