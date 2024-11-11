def compress(word):
    comp = ""
    i = 0

    while i < len(word):
        # Count the length of the current character run, capped at 9
        length = 1
        while i + length < len(word) and word[i] == word[i + length] and length < 9:
            length += 1

        # Append the compressed part to comp
        comp += str(length) + word[i]

        # Move i forward by the length of the current prefix
        i += length

    return comp
word = "abcde"
print(compress(word))  # Output: "1a1b1c1d1e"
word = "aaaaaaaaaaaaaabb"
print(compress(word))  # Output: "9a5a2b"
