def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                if len(line) > 25:
                    yield '...'
                else:
                    yield line

print(*nonempty_lines('file1.txt'))
