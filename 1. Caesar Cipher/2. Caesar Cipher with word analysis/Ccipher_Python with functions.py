import matplotlib
import matplotlib.pyplot as plt
import numpy as np

Cipher_Mode = ""

def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

def WordAnalysis(decryptedSentence):
    aBunchOfWords = decryptedSentence
    wordList = []
    wordCount = []
    newWord = ""

    print(aBunchOfWords)

    for letters in aBunchOfWords:
    
        if(letters ==" "):

        #If we hit a space - print the word for debuggin reasons, add the new Word to our list
        #clear our newWord variable so we can start to build again 

        #print(newWord)
            if(newWord!= ""):
                wordList.append(newWord)
            
            newWord =""
        
        else:

        #Add letters in a string / word until we hit a space - in short build the word letter at a time. 
            if(letters.isalpha()):
                newWord+=letters
                
    print(wordList)
    uWordList = list(dict.fromkeys(wordList))
    print(uWordList)

    for words in uWordList:
        wordCount.append(wordList.count(words))

    word_zip = zip(uWordList, wordCount)
    list_word_zip = list(word_zip)
    names, values = zip(*list_word_zip)
    ind = np.arange(len(list_word_zip))
    width = 0.35
    fig ,ax = plt.subplots()
    rects1 = ax.bar(ind, values, width, color = 'r')
    ax.set_ylabel('Count')
    ax.set_xticks(ind+width/2.)
    ax.set_xticklabels(names)
    autolabel(rects1, ax)
    plt.show()


    
def Encrpyt():
    
    eMessage=""
    UserInput = input ("Provide message to Encrypt : ")
    ShiftKey = int(input ("Provide Shift Key value : "))
    UserInput = UserInput.upper()
    
    if (ShiftKey > 26):
        ShiftKey = ShiftKey % 26

    for element in UserInput:
        if(element.isalpha()):
            if( ord(element) + ShiftKey > 90):
                eMessage += chr(((ord(element)) - 26) + ShiftKey)
            else:
                eMessage += chr(ord(element) + ShiftKey)
        else:
            eMessage += element
        
    print(eMessage)

def Decrypt():
    
    eMessage=""
    UserInput = input ("Provide message to Decrypt : ")
    ShiftKey = int(input ("Provide Shift Key value : "))
    
    if(ShiftKey > 26):
        ShiftKey = ShiftKey % 26

    for element in UserInput:
        if(element.isalpha()):
            if( ord(element) - ShiftKey < 65):
                eMessage += chr(((ord(element)) - ShiftKey) + 26)
            else:
                eMessage += chr(ord(element) - ShiftKey)
        else:
            eMessage += element
        
    print(eMessage)
    return eMessage

def AutoDecrypt():
    
    eMessage=""
    UserInput = input ("Provide message to Decrypt : ")

    for i in range(26):
        eMessage = "" 
        for element in UserInput:
            if(element.isalpha()):
                if( ord(element) - i < 65):
                    eMessage += chr(((ord(element)) - i) + 26)
                else:
                    eMessage += chr(ord(element) - i)
            else:
                eMessage += element
            
        print(str(i) + ": " + eMessage)

def AutoDecryptWithWordCheck():
    keyFound = False
    word =""
    wordList=[]
    eMessage=""
    UserInput = input ("Provide message to Decrypt : ")

    for i in range(26): #loop 0 - 25 for brute force - These are our Shift Keys
        
        eMessage = "" #Reset variable we are storing our decrypted message
        wordList = []
        
        for element in UserInput: #Looping through encrypted text
            
            if(element.isalpha()): #If it is a letter apply the shift
                if( ord(element) - i < 65):
                    char = chr(((ord(element)) - i) + 26) #Using a variable to store roation because it
                                                         #didn't like me doing this operation twice in a row
                    
                    eMessage += char #Building overall Sentence
                    word += char #Building Individual word as we go through
                else:
                    char = chr(ord(element) - i) #same as above
                    eMessage += char #Same as above
                    word += char #Same as above
                    
            else: #It isn't a letter
                if(element==" "): #Check if we have hit a space
                    wordList.append(word)
                    word="" #Reset Word
                    
                eMessage += element

        for j in wordList:
            print(j)
            uAns = input("Is this your word? Yes or No: ")
            if(uAns == "Yes"):
                print(str(i) + ": " + eMessage)
                break
            
        #print(str(i) + ": " + eMessage) #Removing print statement as output is same as above
        #print(str(i))
        #print(wordList)

while (Cipher_Mode != "E" and Cipher_Mode != "D"):
    Cipher_Mode = input("E or D? : ")


if(Cipher_Mode == "E"):
    
    Encrpyt()
  
else:
    #I've put them all in one for demonstration purposes
    eMessage = Decrypt()
    #AutoDecrypt()
    #AutoDecryptWithWordCheck()
    WordAnalysis(eMessage)
