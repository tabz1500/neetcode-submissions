class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        stack = sorted([i for i in range(len(position))], key=lambda i: position[i])

        rem = [(target - position[x]) / speed[x] for x in range(len(position))]

        iters = set()

        while stack:
            curr = stack.pop()
            while stack and rem[stack[-1]] < rem[curr]:
                rem[stack[-1]] = rem[curr]
                curr = stack.pop()
            else:
                remainder = rem[curr]
            
            if remainder not in iters:
                iters.add(remainder)
                fleets += 1
        
        return fleets




