class Solution:

    ## SOLUTION 1:
    def getYoungestCommonAncestor1(self, topAncestor, descendantOne, descendantTwo):
        # Time O(d) || Space O(m-n) [m: maxDescedantDepth ; n: minDescendantDepth]
        if topAncestor == descendantOne:
            return topAncestor

        depthOne = self.getDecendantDepth1(descendantOne, topAncestor)
        depthTwo = self.getDecendantDepth1(descendantTwo, topAncestor)

        visitedAncestor = {}

        if depthOne > depthTwo:
            visitedAncestor[descendantTwo.name] = True
            return self.commonAncestor1(descendantTwo, descendantOne, visitedAncestor)
        else:
            visitedAncestor[descendantOne.name] = True
            return self.commonAncestor1(descendantOne, descendantTwo, visitedAncestor)

    def commonAncestor1(self, lowestDescend, highestDescend, visitedAncestor):

        while lowestDescend or highestDescend:
            if lowestDescend.ancestor:
                visitedAncestor[lowestDescend.ancestor.name] = True
                lowestDescend = lowestDescend.ancestor

            if (
                highestDescend.ancestor
                and highestDescend.ancestor.name in visitedAncestor
            ):
                print(highestDescend.ancestor.name)
                return highestDescend.ancestor

            else:
                highestDescend = highestDescend.ancestor

    def getDecendantDepth1(self, descendant, topAncestor):
        depth = 0
        while descendant != topAncestor:
            depth += 1
            descendant = descendant.ancestor

        return depth

    def getYoungestCommonAncestor2(self, topAncestor, descendantOne, descendantTwo):
        # Time O(d) d= max depth of the ancestraltree || Space O(1)
        if topAncestor == descendantOne:
            return topAncestor

        depthOne = self.getDecendantDepth2(descendantOne, topAncestor)
        depthTwo = self.getDecendantDepth2(descendantTwo, topAncestor)

        if depthOne > depthTwo:
            return self.commonAncestor2(
                descendantTwo, descendantOne, depthOne - depthTwo
            )
        else:
            return self.commonAncestor2(
                descendantOne, descendantTwo, depthTwo - depthOne
            )

    def getDecendantDepth2(self, descendant, topAncestor):
        depth = 0
        while descendant != topAncestor:
            depth += 1
            descendant = descendant.ancestor

        return depth

    def commonAncestor2(self, lowestDescendant, highestDescendant, diff):

        while diff > 0:

            highestDescendant = highestDescendant.ancestor
            diff -= 1

        while highestDescendant != lowestDescendant:
            highestDescendant = highestDescendant.ancestor
            lowestDescendant = lowestDescendant.ancestor

        return highestDescendant
