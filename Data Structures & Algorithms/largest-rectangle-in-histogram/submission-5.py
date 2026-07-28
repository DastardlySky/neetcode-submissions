class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for height in range(len(heights)):
            if not stack or heights[height] > stack[-1][1]:
                stack.append((height, heights[height]))
            else:
                poppedCount = 0
                poppedValue = (-1, -1)
                while stack and stack[-1][1] > heights[height]:
                    poppedValue = stack.pop()
                    poppedCount += 1
                    maxArea = max(maxArea, ((height - poppedValue[0]) * poppedValue[1]))
                if poppedValue != (-1, -1): 
                    stack.append((poppedValue[0], heights[height]))
                print(stack)
        
        print(stack)

        for pair in stack:
            maxArea = max(maxArea, (len(heights) - pair[0]) * pair[1])

        return maxArea
            

                
        