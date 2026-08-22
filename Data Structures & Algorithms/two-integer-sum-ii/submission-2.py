class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers is increasing
        index1 < index2, cant be equal
        O(1) space
        1 index array

        two pointers
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r] 
            if s == target:
                return [l+1, r+1]
            elif s > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]
