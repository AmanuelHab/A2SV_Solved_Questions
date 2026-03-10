class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        num_nextG = defaultdict(lambda: -1)
        stack = []

        for i in range(n2):
            while stack and stack[-1] < nums2[i]:
                num_nextG[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
            
        for i in range(n1):
            nums1[i] = num_nextG[nums1[i]]
        return nums1