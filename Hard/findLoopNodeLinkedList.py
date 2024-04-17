class Solution:

    # This is an input class. Do not edit.
    class LinkedList:
        def __init__(self, value):
            self.value = value
            self.next = None

    def findLoop(self, head):
        ## Time O(n) || Space O(1)
        if head:
            slow = head.next
            fast = head.next.next
            while True:
                if slow == fast:
                    break
                else:
                    slow = slow.next
                    fast = fast.next.next

            slow = head
            while True:
                if slow == fast:
                    return slow
                else:
                    slow = slow.next
                    fast = fast.next
