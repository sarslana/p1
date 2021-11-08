#p_6. Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

#Examples
#stutter("incredible") ➞ "in... in... incredible?"
#stutter("enthusiastic") ➞ "en... en... enthusiastic?"
#stutter("outstanding") ➞ "ou... ou... outstanding?"

word = input("Write the word you want to stutter  ")
def stutter (word):
    return (2*(word[:2] + '... ')) + word + '!'

print(stutter(word))