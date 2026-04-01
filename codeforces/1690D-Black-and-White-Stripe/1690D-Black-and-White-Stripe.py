# count W in first window
    w_count = s[:k].count('W')
    ans = w_count

    # slide window
    for i in range(k, n):
        if s[i] == 'W':
            w_count += 1
        
        if s[i-k] == 'W':
            w_count -= 1
        
        ans = min(ans, w_count)

    print(ans)