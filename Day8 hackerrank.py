x=int(input())

D={}

for i in range(x):
    text=input().split()
    D[text[0]]=text[1]

while True:
    try:
        name=input()
        if name in D:
            print(name + "=" + D[name])
        
        else:
            print("Not found")
    
    except EOFError:
        break