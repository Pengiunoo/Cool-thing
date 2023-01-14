from numpy.core.defchararray import lower


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


if __name__ == "__main__":
    print( word_count("swan likes to eat cheese"))