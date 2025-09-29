import re
import sys

code = sys.stdin.read()

code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)

code = re.sub(r'^\s*#.*$', '', code, flags=re.MULTILINE)

code = re.sub(r'#.*$', '\n', code, flags=re.MULTILINE)

lines = [line.rstrip() for line in code.splitlines() if line.strip() != '']

print('\n'.join(lines))

# """hello everyone
# welcome to my project"""
#
# import math  # importing a useful math module
# # let's take a look at some functions
# def circle_area(radius):
#     """coming soon"""
#     return math.pi * r ** 2  # my favorite formula
# def triangle_area(base, height):
#     """the function takes
#     the base and height
#     of a triangle and
#     returns its area"""
#     return 0.5 * base * height
