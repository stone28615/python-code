def find_cutting_positions(s, x):
    positions = []
    s_len = len(s)
    x_len = len(x)

    for i in range(s_len - x_len + 1):
        if s[i:i+x_len] == x:
            positions.append(i)
            positions.append(i + x_len-1)

    if not positions:
        return -1
    else:
        return positions


s = input().strip()
x = input().strip()

result = find_cutting_positions(s, x)

if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))
