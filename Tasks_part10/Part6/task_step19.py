def interleave(*args):
    return (item for arg in zip(*args) for item in arg)

print(*interleave('bee', '123'))


