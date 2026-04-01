n, k = map(int, input().split())
a = list(map(int, input().split()))

diff = []
for i in range(1, n):
    diff.append(a[i] - a[i-1])

diff.sort(reverse=True)

cost = a[-1] - a[0]

for i in range(k-1):
    cost -= diff[i]

print(cost)