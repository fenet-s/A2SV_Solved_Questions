n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = {}
left = 0
best_len = 0
best_l = 0
best_r = 0

for right in range(n):
    freq[a[right]] = freq.get(a[right], 0) + 1
    
    while len(freq) > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            del freq[a[left]]
        left += 1
    
    if right - left + 1 > best_len:
        best_len = right - left + 1
        best_l = left
        best_r = right

print(best_l + 1, best_r + 1)