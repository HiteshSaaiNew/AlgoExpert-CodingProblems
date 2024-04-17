# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def reverseLinkedList(self, head):
        ## Time O(n) || Space O(1)
        prevNode = None
        currNode = head

        while currNode:
            temp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = temp

        return prevNode
