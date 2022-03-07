# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def solution(tree, target):
#   answer = []
#   parent = []
#   return answer
#
# print(solution([4, 2, 6, 1, 3, 5, 7], 2))
'''
BST(이진 검색 트리)의 루트와 정수 대상이 주어지면 트리를 두 개의 하위 트리로 나눕니다.
여기서 한 하위 트리는 모두 대상 값과 같거나 작은 노드를 가지고 다른 하위 트리는 대상 값보다 큰 모든 노드를 가집니다.
트리에 값 대상이 있는 노드가 반드시 포함되어 있는 것은 아닙니다.

또한 원래 트리의 구조는 대부분 남아 있어야 합니다.
형식적으로, 원래 트리에 부모 p가 있는 자식 c의 경우, 분할 후 둘 다 동일한 하위 트리에 있다면 노드 c는 부모 p를 가져야 한다.

두 하위 트리의 두 루트 배열을 반환합니다.
'''
# Definition for a binary tree node.
from typing import Optional, List


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

# class Solution:
  # def toTree(self, splited, parent):
    # for s in splited:
    #   for p in parent:
    #     if s == p:

      # tree = TreeNode(s, TreeNode(parent.index(s))



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





