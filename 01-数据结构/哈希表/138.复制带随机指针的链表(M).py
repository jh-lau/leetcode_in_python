"""
  @Author       : Liujianhan
  @Date         : 20/5/12 22:29
  @FileName     : 138.复制带随机指针的链表(M).py
  @ProjectName  : leetcode_in_python
  @Description  : 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
    要求返回这个链表的 深拷贝。 
    我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
    val：一个表示 Node.val 的整数。
    random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
    示例 1：
    输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
    示例 2：
    输入：head = [[1,1],[2,1]]
    输出：[[1,1],[2,1]]
    示例 3：
    输入：head = [[3,null],[3,0],[3,null]]
    输出：[[3,null],[3,0],[3,null]]
    示例 4：
    输入：head = []
    输出：[]
    解释：给定的链表为空（空指针），因此返回 null。
    提示：
    -10000 <= Node.val <= 10000
    Node.random 为空（null）或指向链表中的节点。
    节点数目不超过 1000 。
 """


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}

    # 40ms, 14.1MB
    @classmethod
    def copy_random_list(cls, head: 'Node') -> 'Node':
        if not head:
            return head
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        ptr_old_list = head
        ptr_new_list = head.next
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next

        return head_old

    # 44ms, 14.7MB
    def copy_random_list_v2(self, head: 'Node') -> 'Node':
        if not head:
            return head
        if head in self.visited:
            return self.visited[head]

        node = Node(head.val, None, None)

        self.visited[head] = node

        node.next = self.copy_random_list_v2(head.next)
        node.random = self.copy_random_list_v2(head.random)

        return node
