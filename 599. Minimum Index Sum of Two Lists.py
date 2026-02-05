class Solution(object):
    def findRestaurant(self, list1, list2):
        answer = []

        common_set = set(list1) & set(list2)
        min_index_sum = len(list1) + len(list2)
        for string in common_set:
            i = list1.index(string)
            j = list2.index(string)
            if i + j < min_index_sum:
                min_index_sum = i + j

        for string in common_set:
            i = list1.index(string)
            j = list2.index(string)
            if i + j == min_index_sum:
                answer.append(string)

        return answer
