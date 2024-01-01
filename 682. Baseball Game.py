ops = ["5","2","C","D","+"]
lst = []
for i in ops:
    if i == "+":
        lst.append(lst[-1] + lst[-2])

    elif i == "C":
        lst.pop()

    elif i == "D":
        lst.append(lst[-1] * 2)

    else:
        lst.append(int(i))
print(sum(lst))

# lst  = []
# for i in range(len(ops))
#     else:
#         ops[i] += 1
#     lst.append(i)
#     if i == 'D':
#         i = i * 2
#         lst.append(i)
#     elif i == 'C':
#         lst.pop()
#     elif i == "+":
#         lst.append(i)
#     else:
#         lst.append(i)
# print(lst)

