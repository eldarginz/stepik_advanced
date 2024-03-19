in_list = input().split()
out_list = [[]]
add_list = []

for i in range(len(in_list)):
    for j in range(len(in_list)):
        add_list = in_list[j:i+j+1]
        if len(add_list) == i+1:
            out_list.append(add_list)

print(out_list)
