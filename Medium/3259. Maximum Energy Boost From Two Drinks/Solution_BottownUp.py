from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        A, B = [0] * n, [0] * n

        A[0], B[0] = energyDrinkA[0], energyDrinkB[0]
        A[1], B[1] = A[0] + energyDrinkA[1], B[0] + energyDrinkB[1]
        for i in range(2, n):
            A[i] = max(A[i - 1], B[i - 2]) + energyDrinkA[i]
            B[i] = max(B[i - 1], A[i - 2]) + energyDrinkB[i]
        
        return max(A[n - 1], B[n - 1])