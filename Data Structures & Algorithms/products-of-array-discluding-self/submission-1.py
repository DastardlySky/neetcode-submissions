class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = [nums[-1]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[-1])


        for i in range(len(nums) -2, -1, -1):
            postfix.insert(0, nums[i] * postfix[0])

        res = []


        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[1])
            elif i == len(nums) - 1:
                res.append(prefix[-2])
            else:
                res.append(prefix[i-1] * postfix[i+1])

        return res