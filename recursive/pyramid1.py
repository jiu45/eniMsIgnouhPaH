print("Enter the height of pyramid: ", end="")
height = int(input())

def draw(n):
    if n > height:
        return

    for i in range (n):
        print("#", end="")
    print()

    draw(n + 1)

draw(1)