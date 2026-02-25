class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        answer = []

        i = 0
        prev = -1
        partitioner = 0
        for i in range(n):
            #last index of the current char
            last_ind = s.rfind(s[i])
            partitioner = max(last_ind, partitioner)
            
            #Proper substring end reached
            if i == partitioner:
                answer.append(partitioner - prev)
                prev = i
                partitioner = i + 1
                
        return answer
