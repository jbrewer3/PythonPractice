def twoSum(nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i


print(twoSum(nums=[3,2,4], target=6))


