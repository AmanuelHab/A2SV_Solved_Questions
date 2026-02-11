class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        # Find distinct responses for each day
        distinct_res = []
        for response in responses:
            set_res = set()
            for res in response:
                set_res.add(res)
            distinct_res.append(set_res)

        # Count the number of responses of the distinct res of all days
        res_count = defaultdict(int)
        for res_set in distinct_res:
            for res in res_set:
                res_count[res] += 1

        # Find the maximum count
        max_count = 0
        for count in res_count.values():
            max_count = max(max_count, count)

        # Find responses with max_count
        most_common_res = []
        for res, count in res_count.items():
            if count == max_count:
                most_common_res.append(res)

        # Sort the array(lexicographically)
        most_common_res.sort()
        
        # Return the smallest
        return most_common_res[0]
