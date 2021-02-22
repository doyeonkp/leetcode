# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
from itertools import combinations

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
def threeSum(nums):
    ans = []
    nums.sort()
    for i in range(len(nums)-1):
        first = nums[i]
        if first > 0:
            break
        if (i > 0) and (first == nums[i-1]):
            continue

        mid = i+1
        last = len(nums) - 1

        while mid < last:
            if first+nums[mid]+nums[last] > 0:
                last -= 1
            elif first+nums[mid]+nums[last] < 0:
                mid += 1
            else:
                ans.append([first, nums[mid], nums[last]])
                while (mid < last) and (nums[mid] == nums[mid+1]):
                    mid += 1
                while (mid < last) and (nums[last] == nums[last-1]):
                    last -= 1
                mid += 1
    return ans


def threeSum2(nums):
    result = []
    num_set = nums
    num_set.sort()

    for i in range(len(num_set)):
        choice_1 = num_set[i]
        if choice_1 > 0:
            break
        if (i>0 and choice_1 == num_set[i-1]):
            continue
        start = i+1
        end = len(num_set)-1

        while start < end:
            choice_2 = num_set[start]
            choice_3 = num_set[end]
            if choice_1+choice_2+choice_3 > 0:
                end -= 1
            elif choice_1+choice_2+choice_3 < 0:
                start += 1
            else: # choice_1+choice_2+choice_3 == 0:
                while start<end and num_set[start] == num_set[start+1]:
                    start += 1
                while start<end and num_set[end] == num_set[end-1]:
                    end -= 1
                start += 1
                result.append([choice_1, choice_2, choice_3])

    return result

start1 = time.time()
ans = threeSum(([-6,14,-11,7,-5,-8,12,-13,-3,-14,7,0,-7,-15,-5,-9,-13,-7,-5,9,8,-13,-6,-8,-12,7,-10,11,8,-14,12,9,-15,-14,1,-5,-7,-10,-10,5,-9,12,12,-1,12,14,-2,-15,-8,0,9,7,2,10,14,-3,2,11,-6,-13,12,13,11,5,14,-11,7,14,-6,12,-4,-7,9,-7,-1,-1,-8,4,-9,-9,-11,-15,5,6,10,4,11,-10,-8,12,-8,-10,10,11,2,9,-15,-14,0,-13,14,11,-5,0,-11,1,6,-12]))
print(ans)
print("time :", time.time() - start1)  # 현재시각 - 시작시간 = 실행 시간

start2 = time.time()
ans2 = threeSum(([-6,14,-11,7,-5,-8,12,-13,-3,-14,7,0,-7,-15,-5,-9,-13,-7,-5,9,8,-13,-6,-8,-12,7,-10,11,8,-14,12,9,-15,-14,1,-5,-7,-10,-10,5,-9,12,12,-1,12,14,-2,-15,-8,0,9,7,2,10,14,-3,2,11,-6,-13,12,13,11,5,14,-11,7,14,-6,12,-4,-7,9,-7,-1,-1,-8,4,-9,-9,-11,-15,5,6,10,4,11,-10,-8,12,-8,-10,10,11,2,9,-15,-14,0,-13,14,11,-5,0,-11,1,6,-12]))
print(ans2)
print("time :", time.time() - start2)  # 현재시각 - 시작시간 = 실행 시간