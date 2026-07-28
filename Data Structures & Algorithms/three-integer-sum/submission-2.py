class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        print(nums)
        for index, a, in enumerate(nums):

            if index > 0 and a == nums[index - 1]:
                continue

            l = index + 1
            r = len(nums) - 1

            tempSum = None
            while r > l:
                tempSum = a + nums[l] + nums[r]
                print(a, nums[l], nums[r])
                if tempSum == 0:
                    triplets.append([a, nums[l], nums[r]])
                    l += 1
                    # making sure l is not a duplicate
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1
                elif tempSum > 0:
                    r -= 1
                elif tempSum < 0:
                    l += 1

        return triplets






        