objects = [1, True, True, 0, False]

temp = []
ans = 0
for obj in objects:
    if id(obj) not in temp:
        temp.append(id(obj))
        ans += 1

print(ans)
