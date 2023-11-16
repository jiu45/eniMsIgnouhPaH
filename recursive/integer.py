print("Enter an integer: ", end="")
num = int(input())

def print_digit(n):
    if n == 0:
        return
    
    print_digit(int(n / 10))

    print(n % 10)

print_digit(num)