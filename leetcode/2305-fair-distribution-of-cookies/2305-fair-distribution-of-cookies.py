class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies)
        maxi = sum(cookies)
        def generate(cookies, arr_k):
            if not cookies:
                return max(arr_k)
            min_maxi = maxi
            for i in range(k):
                new_arr_k = arr_k[:]
                new_arr_k[i] += cookies[0]
                min_maxi = min(min_maxi, generate(cookies[1:], new_arr_k))
            return min_maxi

        return generate(cookies, [0] * k)