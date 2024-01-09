def solution(x, y):
  dist = 0
  for i in range(x):
    dist = dist + i + 1
    # print(dist)
  for i in range(y):
    dist = dist + x + (i - 1)
    # print(dist)
  return str(dist)
print("ans = ", solution(3, 2))
# print("ans = ", solution(5, 10))