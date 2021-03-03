import time
<<<<<<< HEAD

count = int(input())

for x in range(count, -1, -1):
    print(x, end=' ')

# while count >= 0:
#     time.sleep(1)
#     print(count)
#     count -= 1
=======
count = int(input())


while count > 0:
     time.sleep(1)
     print(count)
     count = count -1
else:
     time.sleep(1)
     print("0")
>>>>>>> bb138f27f174278e24adb2939c523606a2d8749f
