ls = ['p', 'e', 'd', '.', 'h', 'n', 'i', 'x', '.', 'g', 'n', 'o', 'u', 'h', 'P', '.', 'a', 'H']

length = len(ls)

def print_char(i):
    if i == length:
        return
    
    print_char(i + 1)

    if ls[i] == '.':
        ls[i] = " "
    
    print(ls[i], end="")

print_char(0)
print("shiina")
print()
