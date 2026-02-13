def poly_value(values, x):

    result = values[-1]   

    for k in range(len(values) - 2, -1, -1):
        result = result * x + values[k]

    return result

coeff = [3, -2, 0, 5]
x = 2

value = poly_value(coeff, x)
print("Result:", value)
