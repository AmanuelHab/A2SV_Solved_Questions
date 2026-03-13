class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        operations = 0

        # Use the double operations optimally
        while maxDoubles and target > 1:
            new_target = target // 2
            operations += target % 2 + 1
            target = new_target
            maxDoubles -= 1
            
        # Add the increment for the left target
        operations += target - 1
        return operations