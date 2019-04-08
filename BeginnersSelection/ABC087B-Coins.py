A = int(input())  # 500円
B = int(input())  # 100円
C = int(input())  # 50円
X = int(input())  # 合計金額

count = 0
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            if i * 500 + j * 100 + k * 50 == X:
                count += 1

print(count)
