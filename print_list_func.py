def print_list(h):
    a = eval(h)

    b = [[0 for c in range(0,len(a[0]))] for d in range(0, len(a))]
    for j in range(0,len(a)):
        for k in range(0, len(a[0])):
            b[j][k] = int((a[j][k]))

    print('_ '*(len(a)+1))
    print('|{}|{}|'.format(b[0][0],b[0][1] ))
    print('|{}|{}|'.format(b[1][0],b[1][1] ))
    print('-- '*(len(a)+1))

p = input("enter 2x2 nested list: ")
print_list(p)
