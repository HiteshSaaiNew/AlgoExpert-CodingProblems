class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    # SOLUTION 1:
    def removeDuplicatesFromLinkedList1(self, linkedList):
        # Write your code here.

        # Time O(n) || Space O(u) u= stores unique values in to the Dict.
        res = LinkedList(0)
        node = res
        visited = {}

        while linkedList:

            curr = linkedList
            if curr.value not in visited:
                node.next = LinkedList(curr.value)
                node = node.next
                linkedList = linkedList.next
                visited[curr.value] = True
            else:
                linkedList = linkedList.next

        return res.next

    # SOLUTION 2:
    def removeDuplicatesFromLinkedList2(self, linkedList):

        # Time O(n) || Space O(1)
        currNode = linkedList
        while currNode:
            nextNode = currNode.next
            while nextNode is not None and currNode.value == nextNode.value:
                nextNode = nextNode.next

            currNode.next = nextNode
            currNode = currNode.next

        return linkedList