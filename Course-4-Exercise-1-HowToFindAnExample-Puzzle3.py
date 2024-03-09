# There are some books on the table. If you group them by 3,
# you get some number of full groups and 2 books remain;
# if you group them by 4, you get some number of full groups and 3 books remain;
# if you group them by 5, you get some number of full groups and 4 books remain.
# What is the number of books on the table, if it is less than 100?

solutions = []

for i in range(100):
    if i % 3 == 2 and i % 4 == 3 and i % 5 == 4:
        solutions.append(i)

print(solutions)