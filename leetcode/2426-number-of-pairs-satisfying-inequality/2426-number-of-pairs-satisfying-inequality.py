class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # Rearrange the equation:
        # nums2[j] - nums1[j] <= nums2[i] - nums1[i] + diff
        # The equation can be simplified as:
        # nums[j] <= nums[i] + diff , nums[k] == nums2[k] - nums1[k], i < j
        # nums[j] - nums[i] <= diff, i < j
        # nums[j] <= nums[i] + diff

        n = len(nums1)
        nums = [nums2[j] - nums1[j] for j in range(n)]
        # print(nums)
        pairs = 0
        def mergeSort(arr):
            nonlocal pairs
            n = len(arr)
            if n == 1:
                return arr
            mid = n // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            # print(left, right)
            #Count pairs
            i = len(left) - 1
            j = len(right)-1
            while i > -1 and j > -1:
                if right[j] <= left[i] + diff:
                    i -= 1
                    pairs += j + 1
                else:
                    j -= 1
            # print(pairs)
            # Merge
            i = j = 0 
            new_arr = []
            while i < len(left) and j < len(right):
                if right[j] < left[i]:
                    new_arr.append(right[j])
                    j += 1
                else:
                    new_arr.append(left[i])
                    i += 1
            new_arr.extend(left[i:])
            new_arr.extend(right[j:])
            return new_arr
        mergeSort(nums)
        return pairs