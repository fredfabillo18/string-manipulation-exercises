numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    if n > 2:
        squares.append(n * n)

squares2 = [n*n for n in numbers if n > 2]
print("normal: ", squares, ", one-liner: ", squares2)