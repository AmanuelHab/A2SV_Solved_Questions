n, k = map(int, input().split())
nums = list(map(int, input().split()))

ind_dist = dict()

for i in range(n):
    if i > 0:
        ind_dist[i] = nums[i] - nums[i - 1]

ind_dist = dict(sorted(ind_dist.items(), key=lambda x : x[1]))

i = 0
for ind, dist in ind_dist.items():
    if i >= n - k:
        break
    ind_dist[ind] = -1
    i += 1

new_distances = [0] * (n - 1)
for ind, dist in ind_dist.items():
    new_distances[ind - 1] = dist

# Construct the division
answer = []

i = 0
while i < n:
    subarray = [nums[i]]

    while i < n - 1:
        if new_distances[i] == -1:
            subarray.append(nums[i + 1])
        else:
            break
        i += 1
    answer.append(subarray)
    i += 1 

cost_division = 0
for subarray in answer:
    cost_division += subarray[-1] - subarray[0]
print(cost_division)
