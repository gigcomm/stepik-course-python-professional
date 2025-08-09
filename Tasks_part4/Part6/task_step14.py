import pickle


def filter_dump(filename, objects, typename):
    filtered = [item for item in objects if type(item) is typename]
    with open(filename, "wb") as file:
        pickle.dump(filtered, file)

        