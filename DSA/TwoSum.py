class TwoSum:
    def twosum(self, nums: list[int], target:int):
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                print([seen[complement], i])
            seen[nums[i]] = i

Solution = TwoSum()
print(Solution.twosum([2, 7, 11, 15], 9))