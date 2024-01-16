
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def equation_solution_count(a, b, c):
    count = 0
    for x in range(1, 10**12 + 1):
        if x == b * digit_sum(x)**a + c:
            count += 1
    return count

a, b, c = map(int, input().split())
solution_count = equation_solution_count(a, b, c)
print(solution_count)
    