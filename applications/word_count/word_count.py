def word_count(s):
    # Your code here
    cache = {}
    skip_characters = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    lowercase_s = s.lower()

# replace skipped characters with empty space
    for char in skip_characters:
        lowercase_s = lowercase_s.replace(char, "")

    for word in lowercase_s.split():
        if word == "":
            continue
        if word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
