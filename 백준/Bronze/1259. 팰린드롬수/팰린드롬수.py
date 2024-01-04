import sys

def palindrome(n, i, j):
    if i >= j: 
        print("yes")
        return
    else:
        if n[i] == n[j]:
            palindrome(n, i + 1, j - 1)
        else:
            print("no")
            return
n = str(sys.stdin.readline()).strip()
while n != "0":
    palindrome(n, 0, len(n) -1)# 0 2
    n = str(sys.stdin.readline()).strip()
# 1 1