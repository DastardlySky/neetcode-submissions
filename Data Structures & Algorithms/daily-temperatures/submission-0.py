class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            print(f"looking at {temperatures[index]}")
            if len(stack) == 0:
                print(f"stack is empty, adding {(index, temp)}")
                stack.append((index, temp))
                print(f"stack is now {stack}")
            elif temperatures[index] < stack[-1][1]:
                print(f"current temperature ({temp}) is less than top of stack ({stack[-1][1]}), adding {(index, temp)} to stack")
                stack.append((index, temp))
                print(f"stack is now {stack}")
            else:
                print(f"current temperature ({temp}) is greater than top of stack ({stack[-1][1]}), starting to pop")
                while stack and temp > stack[-1][1]:
                    print(f"popping the top of stack ({stack[-1][1]}) as it is bigger than the current temperature ({temp})")
                    print(f"stack before {stack}")
                    popped = stack.pop()
                    print(f"stack now looks like {stack}")
                    output[popped[0]] = index - popped[0]
                stack.append((index, temp))
            print(f"popping is done, adding {(index, temp)} to stack")
        return output


                
        
