class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i - 1])

        postfix = [nums[-1]]

        for i in range(len(nums) - 2, -1, -1):
            postfix.insert(0, nums[i] * postfix[0])

        res = [1] * len(nums)

        res[0] = postfix[1]
        res[-1] = prefix[-2]

        for i in range(1, len(nums) - 1):
            res[i] = prefix[i - 1] * postfix[i + 1]

        return res
