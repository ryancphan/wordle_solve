from collections import Counter
import csv

def word_score(word_list,letters):
    score = {i : int(0) for i in word_list}
    for word in word_list:
        mycounter = 0
        a = [0,0,0,0,0]
        for characters in word:
            c = Counter(letters[mycounter])
            a[mycounter] = c.get(characters)
            mycounter += 1

        score[word] = sum(a)
    return score

with open('wordle-answers-alphabetical.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    f.close()

letters = ["","","","",""]

for word in lines:
    mycounter = 0
    for character in word:
        letters[mycounter] += character
        mycounter += 1

a = word_score(lines,letters)

sorted = {k: v for k, v in sorted(a.items(), key=lambda item: item[1], reverse=True)}

w = csv.writer(open("scored.csv", "w"))

# loop over dictionary keys and values
for key, val in sorted.items():

    # write every key and value to file
    w.writerow([key, val])

# def Convert(lst):
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return res_dct
# print(Counter(letters[0]))


# for mylist in letters:
#     print(char_frequency(mylist,5))

# give each letter a ranking number
# and add it up for each word
# and whichever words have the highest score
# make those the top words to choose to start with



