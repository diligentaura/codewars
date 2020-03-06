def disemvowel(string):
    a=[]
    b=0
    a.append(string)
    x = len(string)
    for i in range(0,x):
        a.append(a[0][0+b])
        b=b+1
    a.pop(0)
    if ("a") in a:
        o = a.count("a")
        for i in range(0,o):
            a.remove("a")
    if ("A") in a:
        q = a.count("A")
        for i in range(0,q):
            a.remove("A")
    if ("e") in a:
        p = a.count("e")
        for i in range(0,p):
            a.remove("e")
    if ("E") in a:
        k = a.count("E")
        for i in range(0,k):
            a.remove("E")
    if ("i") in a:
        u = a.count("i")
        for i in range(0,u):
            a.remove("i")
    if ("I") in a:
        h = a.count("I")
        for i in range(0,h):
            a.remove("I")
    if ("o") in a:
        y = a.count("o")
        for i in range(0,y):
            a.remove("o")
    if ("O") in a:
        s = a.count("O")
        for i in range(0,s):
            a.remove("O")
    if ("u") in a:
        r = a.count("u")
        for i in range(0,r):
            a.remove("u")
    if ("U") in a:
        t = a.count("U")
        for i in range(0,t):
            a.remove("U")
    return "".join(a)
