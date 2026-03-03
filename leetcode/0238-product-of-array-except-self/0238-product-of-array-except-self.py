class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Compute cummulative products from left and right
        prefix_product = [1] * (n + 1)
        suffix_product = [1] * (n + 1)

        product = 1
        for i in range(n):
            prefix_product[i + 1] = prefix_product[i] * nums[i]
            
        product = 1
        for i in range(n - 1, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i]

        answer = []
        for i in range(1, n + 1):
            # Collect the product of previous and following elements(except self)
            answer.append(prefix_product[i - 1] * suffix_product[i])
        return answer