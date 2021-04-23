count = 0


def recursion():
    num = b(5, 2)
    print(num)


def b(n, k):
    global count
    if k == 0 or k == n:
        count += 1
        print("Base Case!  " + str(count))
        return 2
    else:
        return b(n-1, k-1) + b(n-1, k)

def recursion1():
    print(mystery(348))

def mystery(n):
    if n < 10:
        return 10*n+n
    else:
        a = mystery(n // 10)
        b = mystery(n % 10)
        return 100*a+b

def foo(lst1):
    lst1.append(1 + lst1[1])
    print(lst1)

def baz(lst2):
    lst2.append(2 + lst2[1])
    print(lst2)

def bar(lst1, lst2):
    foo(lst2)
    print(lst1)
    print(lst2)
    baz(lst1)
    print(lst1)
    print(lst2)


if __name__ == '__main__':
    # recursion()

    recursion1()

    # a = [1, 2]
    # b = [3, 4]
    # bar(a, b)
