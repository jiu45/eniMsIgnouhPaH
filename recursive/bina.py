#000 001 ...UnicodeEncodeError # 000 001 010 
print("Input an integer: ", end="")
num = int(input())
a = [0] * (num + 1)

def backtrack(i):
    if i == num:
        show()
        return
    
    a[i + 1] = 0
    backtrack(i + 1)
    a[i + 1] = 1
    backtrack(i + 1)
    return

def show():
    for i in range(1, (num + 1)):
        print(a[i], end="")
    print()

backtrack(0)
