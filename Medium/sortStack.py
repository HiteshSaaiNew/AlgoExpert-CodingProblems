class Solution:
    def sortStack(self, stack):
        ## Time O(n^2) || Space O(n)
        if len(stack) == 0:
            return stack

        top = stack.pop()

        self.sortStack(stack)

        self.insertInSortedOrder(stack, top)

        return stack

    def insertInSortedOrder(self, stack, value):

        if not stack or stack[len(stack) - 1] <= value:
            stack.append(value)
            return

        top = stack.pop()

        self.insertInSortedOrder(stack, value)

        stack.append(top)


if __name__ == "__main__":

    print(Solution().sortStack([-5, 2, -2, 4, 3, 1]))
    print(Solution().sortStack([3, 4, 5, 1, 2, 2, 2, 1, 3, 4, 5, 3, 1, 3, -1, 2, 3]))