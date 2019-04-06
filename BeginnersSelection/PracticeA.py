from sys import stdin

a = stdin.readline().rstrip()
b, c = stdin.readline().rstrip().split(" ")
s = stdin.readline().rstrip()

print(int(a) + int(b) + int(c), end=" ")
print(s)
