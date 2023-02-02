
print("------hangman------")

chances =7
word = ("bilal")
check=0
list_word = list(word)
len_word=len(word)

guessed_correctly = []
while len(guessed_correctly)!=len_word:
    guessed_correctly.append("_")
print(guessed_correctly)

while check!=len_word :
    
    if chances !=0:
        
        guess = input("enter one letter: ")
    
        if guess not in guessed_correctly:
            if guess in list_word:
                while guess in list_word:
                    check+=1
                    n=list_word.index(guess)
                    guessed_correctly[n]=guess
                    list_word[n]=" "
                print("\t\t",guessed_correctly)
                    
                
            else:
                chances-=1
                print("\t\tguessed wrong!")
                print(f"\t\tyou have {chances} chances left!")
                print("\t\t",guessed_correctly)
                
            if chances==6:
                print(''' 
              ____
              |   
              |
              |
    ''')
            if chances ==5:
                print('''
              +----+
              |   O
              | 
              |====
               ''')
    

            if chances ==4:
                print('''
              +----+
              |   O
              |   |
              |
              |=====
               ''')
            
            if chances ==3:
                print('''
              +----+
              |   O
              |  /|
              |
              |======
               ''')
                
            if chances ==2:
                print('''
              +----+
              |   O
              |  /|!
              |  
              |=======
               ''')
            if chances ==1:
                print('''
              +----+
              |   O
              |  /|!
              |  /
              |=======
               ''')
            if chances ==0:
                print('''
              +----+
              |   O
              |  /|!
              |  / !
              |======
               ''')   
            if check ==len_word:
                print("\t\t YOU WIN")
        
        else:
            print(f"you have already guessed  this {guess} letter!")
            
    
    else:
        print("\t\t YOU LOSE")
        print(f"answer was {word}")
        break

