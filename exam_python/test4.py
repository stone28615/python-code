def evaluate_polynomial(x, coefficients):
    result = 0
    degree = len(coefficients) - 1

    for i in range(int(len(coefficients)/2)):
        y=i*2;
        result+=coefficients[y]*(x**coefficients[y+1])

    return result


coefficients1 = list(map(int, input().split()))
coefficients2 = list(map(int, input().split()))
x = int(input())
result = evaluate_polynomial(x, coefficients1)
result+=evaluate_polynomial(x, coefficients2)
print(result)
