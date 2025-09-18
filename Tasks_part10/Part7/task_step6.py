def parse_ranges(ranges):
    for range_str in ranges.split(','):
        start, end = range_str.split('-')
        yield from range(int(start), int(end) + 1)

print(*parse_ranges('1-2,4-4,8-10'))
print(*parse_ranges('7-32'))