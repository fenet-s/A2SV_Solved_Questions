# Read number of nodes
n = int(input())

# Read parent array (convert to 0-based indexing)
p = []
for i in range(n - 1):
    parent = int(input())
    p.append(parent - 1)

# Step 1: Find all nodes that are NOT parents → potential leaves
leafs = []

for node in range(n):
    if node not in p:
        leafs.append(node)

# Step 2: Find children of those leaf nodes' parents
lp = []

for i in range(len(p)):
    child = i + 1  # because p[i] is parent of node (i+2), but we use 0-based
    if child in leafs:
        lp.append(p[i])

# Step 3: Count how many leaf-children each parent has
min_count = float('inf')

for k in p:
    count = 0
    for x in lp:
        if x == k:
            count += 1
    min_count = min(min_count, count)

# Step 4: Decide result
if min_count >= 3:
    print("Yes")
else:
    print("No")