import numpy as np

def read_input(fname):
    with open(fname) as f:
        data = f.read().splitlines()
    data = [list(data) for data in data]
    return np.char.array(data)



data = read_input('4.input')

word = "XMAS"

directions = [1 + 0j, 1 + 1j, 0 + 1j, -1 + 1j, -1 + 0j, -1 - 1j, 0 - 1j, 1 - 1j]
directions = [np.array(direction) for direction in directions]

letters_matches = [np.argwhere(data == letter) for letter in word]
letters_matches = [matches[..., 0] + matches[..., 1]*1j for matches in letters_matches]

nb_words = 0
for direction in directions:
    matches = letters_matches[0]
    for i in range(1, len(word)):
        matches = matches + direction
        matches = np.intersect1d(matches, letters_matches[i])
    nb_words += len(matches)

print("Number of words found:", nb_words)


#####Part 2#####

word = "MAS"

directions = [1 + 1j, -1 + 1j, -1 - 1j, 1 - 1j]
directions = [np.array(direction) for direction in directions]

letters_matches = [np.argwhere(data == letter) for letter in word]
letters_matches = [matches[..., 0] + matches[..., 1]*1j for matches in letters_matches]

matching_as = np.empty(0, dtype=complex)
for direction in directions:
    matches = letters_matches[0]
    for i in range(1, len(word)):
        matches = matches + direction
        matches = np.intersect1d(matches, letters_matches[i])
    matching_as = np.concatenate((matching_as, matches - direction))

#Get unique values and their counts for matching_as
unique, counts = np.unique(matching_as, return_counts=True)

print("Number of X-MAS found:", np.count_nonzero(counts == 2))


