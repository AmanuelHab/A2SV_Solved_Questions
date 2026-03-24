from collections import defaultdict
n = int(input())

parent_children = defaultdict(list)
for i in range(2, n + 1):
    parent = int(input())
    parent_children[parent].append(i)

def leafChildren(node):
    leafs = 0
    for child in parent_children[node]:
        if child not in parent_children:
            leafs += 1
    return leafs
def traverse(node):
    if leafChildren(node) < 3:
        return False
    else:
        boolean = True
        for child in parent_children[node]:
            if child in parent_children:
                boolean = boolean and traverse(child)
        return boolean
    
if traverse(1):
    print("Yes")
else:
    print("No")