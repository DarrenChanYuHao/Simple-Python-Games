def insert_Lexicographic(ls,str):

    strlen = len(str) # Check string length

    if ls == []: # If list is empty, just append, this is the starting node
        ls.append(str)
        return

    if(str in ls): # If str already exist in ls, then just add it right beside the existing word
        for index in range(len(ls)):
            
            if(str == ls[index]):
                ls.insert(index,str)
                return

    for index in range(len(ls)): 
        word = ls[index] # Set current word in list that is being checked
        wordlen = len(word) # Check word length
        shorter_word = min(strlen,wordlen) # Find out which one is shorter, to prevent index out of range
        
        for count in range(shorter_word): # Loop thru the shorter word length

            if word[count] > str[count]: # If word corresponding letter is bigger than the to_be inserted, insert it before in the ls
                ls.insert(index,str)
                return

            elif word[count] == str[count]: # If they have the same prefix etc
                if(shorter_word == strlen and count+1 == shorter_word): # If it is the last letter of the to_be inserted, and it still havent find anything, aka boo <- to be inserted is being compared with book, insert it
                    ls.insert(index,str)
                    return
                continue

            else: # Break out of the loop if one of the above have been found, aka book <- to be inserted, found boo is ls, but book should not be inserted yet
                break

        if(index+1 == len(ls)): # Insert if you are at the end of the list and havent found any words smaller than you, aka zzzzzzz can be a smallest
            ls.insert(index+1,str)
            return

ls = []

while(True):
    str = input("Key in word: ")
    insert_Lexicographic(ls,str)
    print(ls)