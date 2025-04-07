logs = []

def liitumine(a, b):
    logs.append('liitumine')
    if isinstance(a, str) or isinstance(b, str):
        print("vale andmed")
        return ""
    return a + b

def minus(a, b):
    logs.append('minus')
    if isinstance(a, str) or isinstance(b, str):
        print("vale andmed")
        return ""
    return a - b

def umon(a, b):
    logs.append('umon')
    if isinstance(a, str) or isinstance(b, str):
        print("vale andmed")
        return ""
    return a * b

def dil(a, b):
    logs.append('dil')
    try:
        if isinstance(a, str) or isinstance(b, str):
            print("vale andmed")
            return ""
        return a / b
    except ZeroDivisionError:
        print("ei saa jagada nullile")

def logsKuuvamine(logs):
    jag = 0
    korr = 0
    liit = 0
    lahut = 0
    for elem in logs:
        if elem == 'liitumine':
            korr += 1
        elif elem == 'minus':
            lahut += 1
        elif elem == 'umon':
            liit += 1
        elif elem == 'dil':
            jag += 1
    return [jag, korr, liit, lahut]

print(liitumine(5, 4))
print(minus(6, 5))
print(umon(7, 7))
print(dil(5, 2))
print(logsKuuvamine(logs))

