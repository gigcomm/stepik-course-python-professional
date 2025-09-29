import re


def normalize_jpeg(filename):
    match = re.sub(filename.split('.')[-1], 'jpg', filename)
    return match

print(normalize_jpeg('stepik.jPeG'))
print(normalize_jpeg('mountains.JPG'))
print(normalize_jpeg('windows11.jpg'))
