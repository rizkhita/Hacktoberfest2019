
def reverse(word):
    new_string = []
    index = len(word)
    # word_arr = list(word)

    while index:
        index -= 1
        new_string.append(word[index])
    return new_string

word = input('input a string :')
print(reverse(word))
