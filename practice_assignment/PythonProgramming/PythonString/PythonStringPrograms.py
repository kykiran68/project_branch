# Write a python programs to find out the smallest word from string.

str1= "Hello Very good morning, We are A learning Python"
word_list = str1.split()
print(word_list)

s_len = len(word_list[0])
s_word = word_list[0]

for word in word_list:
    # print(word)
    word_len = len(word)
    if word_len < s_len: # 5 < 5, 4< 5, 4< 4, 8 < 4, 2< 4, 3< 2, 8< 2, 6< 2
        s_len = word_len # 5, 4, 2
        s_word = word # Hello, Very, We
print("smallest length :", s_len)
print("smallest word :", s_word)





print("_"*50)
# Program: write a python code to find the most simutaneously repeated characters.

str2 = "GGoood Mornnning, Hoppppe you are doiiiiing good"

most_r_char = ''
most_r_count = 0

counter = 1

for i in range(len(str2)-1):
    if str2[i] == str2[i+1]:
        counter += 1
        if most_r_count < counter:
            most_r_count = counter
            most_r_char = str2[i]
            print("most repeated char :", most_r_char, ":", most_r_count)
        else:
            pass
    else:
        counter = 1



print("most repeated char :", most_r_char, ":",  most_r_count)





