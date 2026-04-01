t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    
    count0 = count1 = 0
    equal_positions = [0] * n
    for i in range(n):
        if a[i] == '0':
            count0 += 1
        else:
            count1 += 1
        if count0 == count1:
            equal_positions[i] = 1
    
    flip = False
    possible = True
    for i in range(n-1, -1, -1):
        current_bit = a[i]
        if flip:
            current_bit = '1' if current_bit == '0' else '0'
        
        if current_bit != b[i]:
            if equal_positions[i]:
                flip = not flip
            else:
                possible = False
                break
    
    print("YES" if possible else "NO")