# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:

    ## SOLUTION 1:
    def removeKthNodeFromEnd1(self, head, k):
        # Time O(n) || Space O(1)
        first = head
        second = head
        counter = 1
        while counter <= k:
            second = second.next
            counter += 1

        if second is None:
            head.value = head.next.value
            head.next = head.next.next
            return

        while second.next is not None:
            second = second.next
            first = first.next

        first.next = first.next.next
        return

    ##SOLUTION 2:
    def removeKthNodeFromEnd2(self, head, k):
        # Time O(n) || Space O(n)
        node = head
        array = []
        while node is not None:
            array.append(node.value)
            node = node.next

        nodeToDelete = array[-k]

        if head.value == nodeToDelete:
            head.value = head.next.value
            head.next = head.next.next
            return

        while head.next is not None:
            if head.next.value == nodeToDelete:
                head.next = head.next.next
                return
            else:
                head = head.next
