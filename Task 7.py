def print_pascals_triangle(n):
    for line in range(n):
        row = [1]
        if line > 0:
            for i in range(1, line):
                row.append(triangle[line - 1][i - 1] + triangle[line - 1][i])
            row.append(1) 
        triangle.append(row)
        print(" ".join(map(str, row)).center(2 * n))

n = 5
triangle = []
print_pascals_triangle(n)
