n = 11
t1 = 0
t2 = 1
print("FIBONACCI => {} - {}".format(t1, t2), end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(" - {}".format(t3),end="")
    t1 = t2
    t2 = t3
    cont += 1
print("\nTERMOS    => 0 - 1 - 2 - 3 - 4 - 5 - 6 - 7  - 8  - 9  - 10 ")
