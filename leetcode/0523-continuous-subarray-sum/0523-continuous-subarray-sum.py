class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        need_ind = dict()
        for i in range(n + 1):
            need = prefix_sum[i] % k
            # print(num, num % k, need)
                            # zero is considered as multiple
            if need in need_ind:
                if i - need_ind[need] > 1:# or (need == k and num != 0):
                    return True
            else:
                need_ind[need] = i
        return False