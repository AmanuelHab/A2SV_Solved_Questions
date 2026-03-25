# Calculate the needed final destination
dest = 0
for ch in s1:
    if ch == '+':
        dest += 1
    else:
        dest -= 1

# Find the possibilities
event_space = []
def explore(mapp, dir):
    if not mapp:
        event_space.append(dir)
        return
    if mapp[0] == '+':
        explore(mapp[1:], dir + 1)
    elif mapp[0] == '-':
        explore(mapp[1:], dir - 1)
    else:
        explore(mapp[1:], dir + 1)
        explore(mapp[1:], dir - 1)

explore(s2, 0)
count = 0
for event in event_space:
    if event == dest:
        count += 1

print(count / float(len(event_space)))