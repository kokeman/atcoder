N = int(input())
A = [int(a) for a in input().split()]

count = 0
while True:
    if sum([True for a in A if a % 2 == 0]) == N:
        A = [a / 2 for a in A]
        count += 1
    else:
        break

print(count)
