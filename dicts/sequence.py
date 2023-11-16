squence = []
N = int(input())
longest = 0

def main():
    squence.append(0)
    for i in range(1, N + 1):
        squence.append(int(input()))  
    count = 0
    last_num = 0
    index = -1
    backtrack(count, last_num, index)
    if longest != 0:
        print(f"Length of the longest subsequence satisfied: {longest}")

def backtrack(count, last_num, index):
    global longest
    if index == N:
        longest = max(longest, count)
        return
    for i in range(index, N + 1):
        if i < 0:
            continue
        if i == N:
            backtrack(count, last_num, i)
            return
        if index == -1:
            backtrack(count=count + 1, last_num=squence[i + 1], index=i + 1)
            continue
        elif squence[i + 1] * last_num < 0 and abs(squence[i + 1]) > abs(last_num):
            backtrack(count=count+1, last_num=squence[i + 1], index=i + 1)
main()
            



    