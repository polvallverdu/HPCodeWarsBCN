llargada1 = int(input())
llargada2 = int(input())
llargada3 = int(input())

llargada12 = llargada1 + llargada2
llargada13 = llargada1 + llargada3
llargada23 = llargada2 + llargada3

if llargada12 > llargada3 and llargada13 > llargada2 and llargada23 > llargada1:
    print("It is a triangle")

else:
    print("It is NOT a triangle")
