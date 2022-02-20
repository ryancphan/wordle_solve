# so yellow or black means remove any words with letter in that position
# green means only keep words with letters in that position

# enter first word ex. slate

# return with "g", "y", or "b" representing green, yellow and black

# remove all words from list that don't have same character in g spots or have wrong character in "y" and 'b" spots
# figure out how to check if "y" character is located somewhere within string
# maybe if word[i] = "y" and is not equal to whatever character g is at the variable y_check is 1


import csv
from sys import argv

def dict_append(index,input_word,temp_dict):
    if input_word[index] not in temp_dict.keys():
        temp_list = [index]
        temp_dict[input_word[index]] = temp_list
    elif index not in temp_dict.values():
        temp_dict[input_word[index]].append(index)
    return temp_dict

def repeat_character_check(i,input_word,gyb_key,omit_list,g_dict,y_dict):
    char_count = input_word.count(input_word[i])
    skip_list = []
    if char_count >= 2:
        repeat_list = []
        for repeat_index in range(len(input_word)):
            if input_word[repeat_index] == input_word[i]:
                repeat_list.append(repeat_index)
            omit_check_list = []
        for m in repeat_list:
            skip_list.append(m)
            if gyb_key[m] == "b":
                omit_check_list.append(True)
            elif gyb_key[m] == "g":
                g_dict = dict_append(i,input_word,g_dict)
                omit_check_list.append(False)
            elif gyb_key[m] == "y":
                y_dict = dict_append(i,input_word,y_dict)
                omit_check_list.append(False)
        if all(omit_check_list) == True:
            omit_list.append(input_word[i])
    return skip_list, omit_list, g_dict, y_dict

def omit_character(input_word,gyb_key,omit_list=[],g_dict={},y_dict={}):
    for i in range(len(gyb_key)):
        skip_list, omit_list, g_dict, y_dict = repeat_character_check(i,input_word,gyb_key,omit_list,g_dict,y_dict)
        if i not in skip_list:
            if gyb_key[i] == "b" and input_word[i] not in omit_list:
                omit_list.append(input_word[i])
            elif gyb_key[i] == "g":
                g_dict = dict_append(i,input_word,g_dict)
            elif gyb_key[i] == "y":
                y_dict = dict_append(i,input_word,y_dict)
    return omit_list, g_dict, y_dict

def omit_check(word,omit_list):
    word_remove = False
    for i in omit_list:
        if i in word:
            word_remove = True
    return word_remove

def check(word,temp_dict,gyb_key):
    word_remove = False
    for m, n in temp_dict.items():
        if m not in word:
            word_remove = True
            break
        else:
            for i in n:
                if (m != word[i] and gyb_key[i] == "g") or (m == word[i] and gyb_key[i] == "y"):
                    word_remove = True
                    break
    return word_remove

def list_remove(word,word_list):
    word_list.remove(word)
    return word_list

def gyb_check(input_word,gyb_key,word_list,omit_list,g_dict,y_dict):
    if gyb_key == "ggggg":
        print("Good job! Wordle solved!")
        return None
    else:
        word_list_copy = []
        for word in word_list:
            omit_list, g_dict, y_dict = omit_character(input_word,gyb_key,omit_list,g_dict,y_dict)
            word_remove = omit_check(word,omit_list)
            if word_remove is False:
                word_remove = check(word,g_dict,gyb_key)
            if word_remove is False:
                word_remove = check(word,y_dict,gyb_key)
            if word_remove is False:
                word_list_copy.append(word)

        # print("omit list: " + ",".join(omit_list))
        # print(g_dict)
        # print(y_dict)
        print("Use " + word_list_copy[0] + " as next word and enter next gyb sequence:")
        gyb_key = input()
        gyb_check(word_list_copy[0],gyb_key,word_list_copy,omit_list,g_dict,y_dict)


scored= open("scored.csv", "r")
word_list = []
countera = 1
for line in csv.reader(scored):
    word_list.append(line[0])


# Add exception for entering multiple words at the start

print("""Hi welcome to the wordle solver
Please enter your first word:""")

first_word = input()

print("Enter green, yellow, and black squares using g, y, and b in order:")

gyb_key = input()

if gyb_key == "ggggg":
    print("Good job!")

else:
    gyb_check(first_word,gyb_key,word_list,omit_list=[],g_dict={},y_dict={})








                





                


    




