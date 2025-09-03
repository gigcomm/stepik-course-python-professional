import builtins


def print(*args, sep=' ', end='\n'):
    upper_args = [str(arg).upper() for arg in args]
    sep = str(sep).upper()
    end = str(end).upper()
    builtins.print(*upper_args, sep=sep, end=end)

words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')