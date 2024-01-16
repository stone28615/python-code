def digit_sum(num):
    return sum(map(int, str(num)))

def count_integer_solutions(a, b, c):
    count = 0
    for i in range(109):
        x=b*(i**a)+c
        if(digit_sum(x)==i):
            count+=1
        


    return count

a, b, c = map(int, input().split())

result = count_integer_solutions(a, b, c)

print(result)
