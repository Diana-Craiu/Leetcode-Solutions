"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        current = head
        new_nodes={}

        while current:
            node = Node(x=current.val)
            new_nodes[current]=node
            current=current.next
        
        current=head
        while current:
            new_node=new_nodes[current]
            new_node.next=new_nodes[current.next] if current.next else None
            new_node.random=new_nodes[current.random] if current.random else None
            current=current.next

        return new_nodes[head]
