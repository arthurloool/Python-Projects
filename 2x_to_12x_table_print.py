from tabulate import tabulate

i = 2
table = []
head = [1,2,3,4,5,6,7,8,9,10]
while i <= 12:
    x_list = []
    for a in range(1,11):
        x = i*a
        x_list.append(x)
    table.append(x_list)
    i+=1

print(tabulate(table, headers=head, tablefmt="grid"))