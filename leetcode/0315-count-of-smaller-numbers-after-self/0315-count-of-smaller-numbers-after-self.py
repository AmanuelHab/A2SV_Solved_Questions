class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def mergesort(arr):
            m = len(arr)
            if m == 1:
                return arr
            mid = m // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            new_arr = []
            i = j = 0
            passes = 0
            # print(left, right)
            while i < len(left) and j < len(right):
                if nums[right[j]] < nums[left[i]]:
                    new_arr.append(right[j])
                    passes += 1
                    j += 1
                else:
                    new_arr.append(left[i])
                    ind_c[left[i]] += passes
                    i += 1
            while i < len(left):
                new_arr.append(left[i])
                ind_c[left[i]] += passes
                i += 1
            new_arr.extend(right[j:])
            return new_arr

        ind_c = {i: 0 for i in range(n)}
        mergesort([i for i in range(n)])
        answer = [0] * n
        for ind, c in ind_c.items():
            answer[ind] += c
        return answer