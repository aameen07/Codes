N = int(input())
output = []
for i in range(N):
    Input = input().split()
    if Input[0] == "print":
        print(output)
    elif Input[0] == "insert":
        output.insert(int(Input[1]), int(Input[2]))
    elif Input[0] == "remove":
        output.remove(int(Input[1]))
    elif Input[0] == "pop":
        output.pop()
    elif Input[0] == "append":
        output.append(int(Input[1]))
    elif Input[0] == "sort":
        output.sort()
    else:
        output.reverse()
