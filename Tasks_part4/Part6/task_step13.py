import sys
import pickle


pickle_file = sys.stdin.readline().strip()

args = [line.strip() for line in sys.stdin if line.strip()]

with open(pickle_file, "rb") as file:
    func = pickle.load(file)

result = func(*args)
print(result)