class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize fast and slow pointers to find the intersection point
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Step 2: Find the entrance to the cycle (the duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow