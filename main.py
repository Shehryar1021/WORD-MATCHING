def match_words(words):
    ctr=0
    lst=[]
    for word in words:
     if len(word) > 1 and word[0] == word[-1]:
        ctr+=1
        lst.append(word)
    print("LIST OF WORDS WITH FIRST AND LAST CHARACTER same \n",lst)
    return ctr

count=match_words(['abc' ,'cfc' , 'xyz' , 'abc' , '1221'])
print("LIST OF WORDS WITH FIRST AND LAST CHARACTERS ARE",count)