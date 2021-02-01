#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import heapq

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        tmp = None
        while nums:
            if i >= len(nums):
                break
            if tmp == nums[i]:
                del nums[i]
            else:
                tmp = nums[i]
                i += 1

        return(len(nums))

