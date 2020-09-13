def alayGenerator(sentence_input):
    # fungsi untuk mengubah kata biasa ke alay

    # dictionary huruf alay
    huruf_alay = {
        'a': '4',
        'i': '1',
        'e': '3',
        'g': '6',
        'j': 'jh',
        'o': '0',
        's': '5',
        'u': 'uw',
        'c': 'ch',
        'f': 'v',
        'k': 'q',
        'p': 'ph',
        't': 'th',
        'y': 'iy'
    }

    result = []

    for word in sentence_input:
        for char in word:
            result.append(char)
            for alay in huruf_alay:
                if (char == alay):
                    result.pop()
                    result.append(huruf_alay[char])

    return ''.join(result)


if __name__ == '__main__':
    sentence_input = input("\nq4l1m4th y6 m4u d1ub4h: ").split(sep=' ')
    alay_generated = []

    for i in range(len(sentence_input)):
        alay_generated.append(alayGenerator(sentence_input[i]))
        print(alay_generated)

    alay_words_join = ' '.join(alay_generated)

    print("\nHasilnya: ")
    print("="*len(alay_words_join))
    print(alay_words_join)
    print("="*len(alay_words_join))
