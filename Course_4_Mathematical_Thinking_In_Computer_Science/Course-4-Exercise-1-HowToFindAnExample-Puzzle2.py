
# Find a three digit number that produces a remainder 1 when divided by 2, 3, 4, 5, 6, 7

answer_list = []

for i in range(100, 1000):
    j = 2
    while j <= 7:
        if i % j != 1:
            break
        if j == 7:
            answer_list.append(i)
        j += 1


print(answer_list)
