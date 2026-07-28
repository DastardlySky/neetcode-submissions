class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_map:
                return [nums_map[diff], i]
            else:
                nums_map[nums[i]] = i
                print(nums_map)