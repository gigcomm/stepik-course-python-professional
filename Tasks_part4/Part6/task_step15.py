import sys
import pickle


def calculate_checksum(obj):
    if isinstance(obj, dict):
        int_keys = [key for key in obj.keys() if type(key) is int]
        return sum(int_keys if int_keys else 0)
    if isinstance(obj, list):
        int_elem = [item for item in obj if type(item) is int]
        return (max(int_elem) * min(int_elem) if int_elem else 0)


filename = sys.stdin.readline().strip()
checksum = sys.stdin.readline().strip()

with open(filename, "rb") as file:
    pickle_file = pickle.load(file)

calculated = calculate_checksum(pickle_file)

if calculated == checksum:
    print("Контрольные суммы совпадают")
else:
    print("Контрольные суммы не ссовпадают")

