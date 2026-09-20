from functools import cache
from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)

        @cache
        def A(i):
            if i == 0:
                return energyDrinkA[i]
            if i == 1:
                return energyDrinkA[i] + A(0)

            return max(A(i - 1), B(i - 2)) + energyDrinkA[i]

        @cache
        def B(i):
            if i == 0:
                return energyDrinkB[i]
            if i == 1:
                return energyDrinkB[i] + B(0)

            return max(B(i - 1), A(i - 2)) + energyDrinkB[i]
        
        return max(A(n - 1), B(n - 1))