class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        longest = 0

        for num in numsSet:
            tempLength = 0
            if num - 1 not in numsSet:
                tempLength += 1
                if tempLength > longest:
                    longest = tempLength
                while True:
                    if num + tempLength in numsSet:
                        tempLength += 1
                        if tempLength > longest:
                            longest = tempLength
                    else:
                        break

        return longest
  
        