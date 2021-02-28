def escaleras(n):
    if n > 0:
        print(" " * (2 * n - 1) + "_" * n)
        for i in range(n-1):
            print(" " * (2 * n - i - 2) + "_|")
        print("_" * n + "|")


n = int(input())
escaleras(n)
