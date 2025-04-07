"""
Stack (monotonic) approach-
TC - O(n) ==> 3 pass
SC - O(n)
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0: return []

        n = len(nums)
        rtnData = [-1] * n
        mstack = []

        for i in range(n * 2):
            # case 1: while stack not empty
            while mstack and nums[i % n] > nums[mstack[-1]]:
                greater = nums[i % n]
                rtnData[mstack[-1]] = greater
                mstack.pop()
            # case 2: while stack empty
            if i < n:
                mstack.append(i)

        return rtnData