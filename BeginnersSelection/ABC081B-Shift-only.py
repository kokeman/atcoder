N = int(input())
A = list(map(int, input().split()))


def operation(A):
    if sum([True for a in A if a % 2 == 0]) == N:
        return list(map(lambda x: x / 2, A))
    else:
        return "End"

count = 0
while True:
    A = operation(A)
    if A == "End":
        break
    count += 1
print(count)
