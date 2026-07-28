class Solution:
    def trap(self, height: List[int]) -> int:
        lWall = []
        rWall = []

        area = 0

        tempMax = 0
        for i in range(len(height)):
            tempMax = max(height[i], tempMax)
            lWall.append(tempMax)
        
        tempMax = 0
        for i in range(len(height)-1, -1, -1):
            tempMax = max(height[i], tempMax)
            rWall.insert(0, tempMax)

        for i in range(len(height)):
            area += min(lWall[i], rWall[i]) - height[i]

        return area

            
            