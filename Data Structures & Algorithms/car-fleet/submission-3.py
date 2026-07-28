class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)))
        stack = []
        res = 0
        print(cars)
        for car in range(len(cars)-1, -1, -1):
            arrivalTime = (target - cars[car][0]) / cars[car][1]
            print(arrivalTime)
            if len(stack) == 0 or arrivalTime > stack[-1]:
                stack.append(arrivalTime)
                
        return len(stack)
            
        