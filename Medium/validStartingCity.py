class Solution:
    def validStartingCity(self, distances, fuel, mpg):
        # Time O(n) || Space O(1)
        minimumGasEver = 0
        cityIdx = 0
        reminingFuel = 0
        for i in range(1, len(distances)):
            distanceToTravel = distances[i - 1]
            reminingFuel += (fuel[i - 1] * mpg) - distanceToTravel
            if reminingFuel < minimumGasEver:
                minimumGasEver = reminingFuel
                cityIdx = i

        return cityIdx
