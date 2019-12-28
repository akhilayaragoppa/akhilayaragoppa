# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 23:42:32 2019

@author: Akhila Yaragoppa
"""

from math import acos,sqrt

def get_filtered_words_list(line):
    
    words = line.split(" ")
    word_list = []
    for word in words: #for each word in the line
        if word.isalnum() is False:
            newWord = ""
            for character in word: #for each character in the word
                if character.isalnum() is True:
                    newWord = newWord + character
            word = newWord
        word = word.lower()
        word_list.append(word)
        
    return word_list


def get_list_of_words_from_file(filename):

    filevar = open(filename,'r')

    line_list = filevar.readlines()
    big_list = []
    filevar.close()

    for line in line_list: #for each line in the document
        line = line.rstrip('\n')
        big_list.extend(get_filtered_words_list(line))
    
    return big_list


def convert_wordlist_to_freq_dictionary(word_list):
    
    freq_dict = {}
    word_set = set(word_list)
    for word in word_set:
        freq_dict[word] = word_list.count(word)
    
    return freq_dict


def get_dot_product_of_two_dictionaries(dict1, dict2): #len(dict1) < len(dict2} for faster calculation
    
    final_product = 0

    for word in dict1.keys():
        if (dict1.get(word) == None) or (dict2.get(word) == None):
            product = 0
        else:
            product = (dict1.get(word) * dict2.get(word))
                
        final_product = final_product + product
        
    return final_product


def get_angle_between_two_dictionaries(dict1, dict2):
    
    angle = 0
    
    if len(dict1) < len(dict2):
        dot_product = get_dot_product_of_two_dictionaries(dict1, dict2)
    else:
        dot_product = get_dot_product_of_two_dictionaries(dict2, dict1)
    
    magnitude = sqrt(get_dot_product_of_two_dictionaries(dict1,dict1) * get_dot_product_of_two_dictionaries(dict2,dict2)) 
        
    angle = acos(dot_product/magnitude)
    
    return angle


def main():
    
    file_name1 = input("Enter the first file name (Format: filename.txt) : ")
    word_list1 = get_list_of_words_from_file(file_name1)
    
    file_name2 = input("Enter the second file name (Format: filename.txt) : ")
    word_list2 = get_list_of_words_from_file(file_name2)
    
    freq_dict1 = convert_wordlist_to_freq_dictionary(word_list1)
    freq_dict2 = convert_wordlist_to_freq_dictionary(word_list2)
    
    value = get_angle_between_two_dictionaries(freq_dict1, freq_dict2)
    
    print("The angle between the two documents is {} radians".format(value))
    

if(__name__ == '__main__'):
    import profile
    profile.run("main()")




    
