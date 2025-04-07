"""
Monotonic Stack (elements are arranged in increasing or decreasing order) approach -
TC - O(n)
SC - O(n)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if temperatures is None or len(temperatures) == 0: return []

        n = len(temperatures)
        rtnData = [0 for i in range(n)]
        mstack = []

        for i in range(n):
            # check if stack not empty and current ith temp with temp[top_element] in stack
            while len(mstack) != 0 and temperatures[i] > temperatures[mstack[-1]]:
                # subtract indices
                idx = i - mstack[-1]
                # add the idx as a value to rtnData's index to the same index of stack[-1]
                rtnData[mstack[-1]] = idx
                # pop the top element since it is solved
                mstack.pop()
            # if not above condition add element to stack
            mstack.append(i)
        return rtnData