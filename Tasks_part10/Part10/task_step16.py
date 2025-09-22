from itertools import tee, cycle, chain

# def ncycles(iterable, times):
#     iters = tee(iterable, times)
#     return chain.from_iterable(iters)

def ncycles(iterable, times):
    return (i for iter in tee(iterable, times) for i in iter)

print(*ncycles([1, 2, 3, 4], 3))
iterator = iter('bee')
print(*ncycles(iterator, 4))
iterator = iter([1])
print(*ncycles(iterator, 10))