class Solution:
    def splitString(self, s: str) -> bool:
        max_n = len(s)

        def trial(arr):
            n = len(arr)
            if n > 1:
                for i in range(n - 1):
                    if int(arr[i]) != int(arr[i + 1]) + 1:
                        break
                else:
                    return True
            # If the string is unbreakable
            if n >= max_n:
                return False

            split_s = arr[0]
            boolean = False

            for i in range(1,len(split_s)):
                new_s = [split_s[:i], split_s[i:]]
                if int(new_s[0]) > int(new_s[1]):
                    boolean = boolean or trial(new_s + arr[1:])
            return boolean
        
        return trial([s])