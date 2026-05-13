def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")
print(f"0! = {factorial(0)}")

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
print("Evens:", evens)

# Squares
squares = [x**2 for x in range(10)]
print("Squares:", squares[:5], "...")

# Filter > 50
nums = [23, 67, 12, 89, 45, 78]
large = [x for x in nums if x > 50]
print(">50:", large)
def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] 
            for i in range(len(a))]

mat1 = [[1,2], [3,4]]
mat2 = [[5,6], [7,8]]
result = add_matrices(mat1, mat2)
print("Matrix Sum:")
for row in result:
    print(row)


def count_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

sentence = "hello world"
counts = count_frequency(sentence)
print("Character frequency:")
for char, cnt in counts.items():
    print(f"'{char}': {cnt}")