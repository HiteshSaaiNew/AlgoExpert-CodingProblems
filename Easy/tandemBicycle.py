class Solution:
    def tandemBicycle(self, redShirtSpeeds, blueShirtSpeeds, fastest):
        ## Time O(nlogn) || Space O(1)
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        n = len(redShirtSpeeds)
        if fastest:
            maxSpeed = 0
            left = 0
            right = n - 1
            while left < n:
                val1 = redShirtSpeeds[right]
                val2 = blueShirtSpeeds[left]
                maxSpeed += max(val1, val2)
                left += 1
                right -= 1
            return maxSpeed

        else:
            minSpeed = 0
            left = n - 1
            right = n - 1
            while left >= 0:
                val1 = redShirtSpeeds[right]
                val2 = blueShirtSpeeds[left]
                minSpeed += max(val1, val2)
                left -= 1
                right -= 1

            return minSpeed


if __name__ == "__main__":

    print(Solution().tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))
    print(Solution().tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False))
