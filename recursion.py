def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
num=int(input('enter till how many number need to be added'))
print(sum(num))
