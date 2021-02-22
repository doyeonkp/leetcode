#https://leetcode.com/problems/two-sum/submissions/
def twoSum(nums, target):
    dic_num = {}

    for key, val in enumerate(nums):
        print(val)
        # 디션너리에 타겟 빼기 현재 들어온 숫자를 빼면 얼마가 남는지 저장
        # ex) [3,2,4] target: 6
        # 6 - 3(현재 들어온 수) = 3(빼고 남은 수)
        # 딕셔너리[빼고 남은 수] = key(현제 인덱스)
        # 그 후 딕셔너리에 넣은 수가 있는지 리스트가 interate할때마다 찾음
        # 딕셔너리 => {3(6-3):0, 4(6-2):2}
        # 찾으면 리턴 -> dic의 find를 쓰기 때문에 runtime이 n(1) 그러나 메모리는 많이 소모
        if val in dic_num:
            return [dic_num[val], key]
        else:
            dic_num[target - val] = key


