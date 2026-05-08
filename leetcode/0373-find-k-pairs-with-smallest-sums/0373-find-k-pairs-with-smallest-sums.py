class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = [ (nums1[0] + nums2[0], 0, 0)]
        visited = {(0,0)}
        pairs = []

        while q:
            s, x, y = heappop(q)
            pairs.append([nums1[x], nums2[y]])
            if len(pairs) == k:
                break
            
            if x < len(nums1) - 1 and (x+1, y) not in visited:
                heappush(q, (nums1[x+1]+ nums2[y], x+1, y))
                visited.add((x+1, y))
            if y < len(nums2) - 1 and (x, y+1) not in visited:
                heappush(q, (nums1[x]+ nums2[y+1], x, y+1))
                visited.add((x, y+1))
        return pairs