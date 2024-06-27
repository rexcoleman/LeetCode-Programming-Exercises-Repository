# Find a six digit number which starts by 100 and is divisible by 9,127
answer_list = []

for i in range(100000, 101000):
    if i % 9127 == 0:
        answer_list.append(i)

print(answer_list)