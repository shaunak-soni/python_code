#Use comprehensions to find words in a list which have length >4

#The paragraph is 
paragraph = "I still have a dream, a dream deeply rooted in the American dream – one day this nation will rise up and live up to its creed, We hold these truths to be self evident: that all men are created equal. I have a dream ..."

print(f'The paragraph is : \n {paragraph}\n')

#replace punctuations them with spaces:
punctuation = ",.!:-\n"

for char in punctuation:
    paragraph = paragraph.replace(char, ' ')

# create a word list by splitting on spaces:	
all_words = paragraph.split()	

#create a list of unique words longer than 4 characters.
words = {word for word in all_words if len(word) > 4}

print(f'\nThe words with length > 4 are : \n {words}')