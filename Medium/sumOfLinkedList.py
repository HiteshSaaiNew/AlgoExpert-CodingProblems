# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Time O(max(n, m)) || Space O(max(n,m))
    if not linkedListOne and linkedListTwo:
        return linkedListTwo
    if not linkedListTwo and linkedListOne:
        return linkedListOne
    if not linkedListTwo and not linkedListOne:
        return None

    res = LinkedList(0)
    node = res

    carry = 0
    while linkedListOne and linkedListTwo:

        l1Val = linkedListOne.value
        l2Val = linkedListTwo.value

        currSum = l1Val + l2Val + carry

        value = currSum % 10
        carry = currSum // 10
        node.next = LinkedList(value)

        node = node.next
        linkedListOne = linkedListOne.next
        linkedListTwo = linkedListTwo.next

    if linkedListOne:

        while linkedListOne:

            currSum = linkedListOne.value + carry
            value = currSum % 10
            carry = currSum // 10
            node.next = LinkedList(value)
            node = node.next
            linkedListOne = linkedListOne.next

    else:

        while linkedListTwo:

            currSum = linkedListTwo.value + carry
            value = currSum % 10
            carry = currSum // 10
            node.next = LinkedList(value)
            node = node.next
            linkedListTwo = linkedListTwo.next

    if carry:
        node.next = LinkedList(carry)

    return res.next
