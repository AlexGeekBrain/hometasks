cube_list = []

for i in range(1, 1001, 2):
    cube_list.append(i ** 3)

result = 0
for n in cube_list:
    s_m = 0
    num = n
    while num > 0:
        s_m += num % 10
        num //= 10
    if s_m % 7 == 0:
        result += n
print(result)

result = 0
for n in cube_list:
    s_m = 0
    n += 17
    num = n
    while num > 0:
        s_m += num % 10
        num //= 10
    if s_m % 7 == 0:
        result += n
print(result)
