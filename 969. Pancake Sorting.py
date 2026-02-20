class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr)
        flips = []
        sorted_arr = sorted(arr)

        while arr != sorted_arr:
            # Take the largest num index and put it at the end
            max_num = max(arr[:end])

            # Put it infront first and at the end
            max_ind = arr.index(max_num)

            if max_ind == end - 1:
                end -= 1
                continue
            if max_ind:
                #flip
                arr[:max_ind + 1] = arr[max_ind::-1]
                arr[:end] = arr[end - 1::-1]
                # Record flip
                flips.extend([max_ind + 1, end])
            else: # If the max_num is suddenly at the front
                arr[:end] = arr[end - 1::-1]
                flips.append(end)
            end -= 1

        return flips
