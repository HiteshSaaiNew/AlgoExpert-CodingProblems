# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    # def __init__(self, array):
    #     # Do not edit the line below.
    #     self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParent = (len(array) - 2) // 2
        for currIdx in reversed(range(0, firstParent + 1)):
            self.siftDown(currIdx, len(array) - 1, array)
        return array

    def siftDown(self, currIdx, endIdx, heap):
        ## Time O(log n) || Space O(1)
        firstChildIdx = currIdx * 2 + 1
        while firstChildIdx <= endIdx:
            secondChildIdx = (currIdx * 2) + 2 if (currIdx * 2) + 2 <= endIdx else -1
            if secondChildIdx != -1 and heap[secondChildIdx] < heap[firstChildIdx]:
                swapIdx = secondChildIdx
            else:
                swapIdx = firstChildIdx
            if heap[currIdx] > heap[swapIdx]:
                self.swap(currIdx, swapIdx, heap)
                currIdx = swapIdx
                firstChildIdx = currIdx * 2 + 1
            else:
                return

    def siftUp(self, currIdx, heap):
        ## Time O(log n) || Space O(1)
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2
        return

    def peek(self):
        ## Time O(1) || Space O(1)
        return heap[0]

    def remove(self):
        ## Time O(log n) || Space O(1)
        self.swap(0, len(heap) - 1, heap)
        valueToRemove = heap.pop()
        self.siftDown(0, len(heap) - 1, heap)
        return valueToRemove

    def insert(self, value):
        ## Time O(log n) || Space O(1)
        heap.append(value)
        self.siftUp(len(heap) - 1, heap)

    def swap(self, firstIdx, secondIdx, heap):
        heap[firstIdx], heap[secondIdx] = heap[secondIdx], heap[firstIdx]


if __name__ == "__main__":

    array = [3, 1, 5, 0, 7, 4, 6, 2]
    heap = MinHeap().buildHeap(array)
    print(MinHeap().peek())
    print(MinHeap().remove())
    print(heap)