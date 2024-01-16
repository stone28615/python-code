def digit_sum(num):
    return sum(map(int, str(num)))

def count_integer_solutions(a, b, c):
    count = 0
    max_x = 10**12

    if a >= 2:
        max_digit_sum = int((max_x - c)**(1/a))
        for digit_sum_x in range(b+c, max_digit_sum + 1):
            x_candidate = b * (digit_sum_x**a) + c
            if 1 <= x_candidate <= max_x and digit_sum(x_candidate) == digit_sum_x:
                count += 1
    else:
        for x in range(b+c, max_x + 1):
            if x == b * digit_sum(x) + c:
                count += 1
                
    return count

a, b, c = map(int, input().split())

result = count_integer_solutions(a, b, c)

print(result)
