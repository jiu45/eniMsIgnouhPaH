print("Enter an integer: ", end="")
num = int(input())

def print_reverse_digit(n):
    if n == 0:
        return
    
    print(n % 10)

    print_reverse_digit(int(n / 10))

print_reverse_digit(num)