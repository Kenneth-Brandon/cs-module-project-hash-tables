def no_dups(s):
    # Your code here
    new_s = s.split(" ")
    cache = {}

    for word in new_s:
        if word not in cache:
            cache[word] = word

    new_s = " ".join(list(cache.keys()))
    # print(new_s)

    return new_s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
