word=input()
reserverd_word=""
for i in range (len(word)-1,-1,-1):
    reserverd_word+= word[i]
print(reserverd_word)