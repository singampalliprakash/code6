sentence = input("Enter a sentence: ")
words = sentence.split()  
longest = max(words, key=len)
print(len(longest))