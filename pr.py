import functools, re
def add(x,y):
    return x+y

def outer(x):
    def inner(y):
        return x + y
    return inner
    # return functools.partial(add,x)

# print(outer(2))


access_log = ['2023-05-01 10:20:05 200 GET /page1.html',
              '2023-05-01 10:20:05 200 POST /submit',]

def parse1():
    for line in access_log:
        yield line.split()[1]
def parse2():
    for line in access_log:
        yield from re.findall(r'\d{2}:\d{2}:\d{2}', line)[:1]
def parse3():
    for line in access_log:
        yield re.findall(r'\d:\d:\d', line)[0]
def parse4():
    yield from access_log.split('')[1]
def parse5():
    for line in access_log:
        yield re.findall(r'\d+\d+\d', line)[0]
# for ch in parse5():
#     print(ch)

values = [1,4,6,3,5,7]
def f1(values):
    return sum(x**2 for x in values if x % 2 == 0)
def f2(values):
    return sum(x**2 for i, x in enumerate(values) if i % 2 == 0)
def f3(values):
    return sum(x*x if x%2==0 else 0 for x in values)
# def f5(values):
#     return sum(x**2 if x * 2 == 0 for x in values)

print(f1(values))
print(f2(values))
print(f3(values))

print([0,1]*3)
print(None == False)

temperatures = [1,6,3,None,14]
def fill1(temperatures):
    total,count = 0,0
    for t in temperatures :
        if t is not None:
            total += t
            count += 1
    avg = total/count
    for t in temperatures:
        if t is not None:
            t = avg
    print(temperatures)

fill1(temperatures)