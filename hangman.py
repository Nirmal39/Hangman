from random import choice

player_score =0
computer_score =0

def hangedman(hangman):

    graphics=[
           '''       
                      +-------+ 
                      |       | 
                      |       
                      |        
                      |        
                      |    
                 ==============    
           ''',
           '''      
                      +-------+        
                      |       |
                      |       o 
                      |              
                      | 
                      |                
                 ===============   
           ''',
           '''       
                      +-------+        
                      |       |
                      |       o
                      |       |         
                      |       
                      |                  
                 ===============    
           ''',
           '''       
                      +-------+        
                      |       |        
                      |       o        
                      |      -|  
                      |            
                      |        
                 =============== 
           ''',
           '''        
                      +-------+        
                      |       |       
                      |       O        
                      |      -|-        
                      |                
                      |             
                 ===============    
           ''',
           '''          
                      +-------+        
                      |       |        
                      |       O        
                      |      -|-       
                      |      /         
                      |            
                 ===============    
           ''',
           '''    
                      +-------+        
                      |       |        
                      |       O        
                      |      -|-      
                      |      / \         
                      |            
                 ===============    
           '''
             ]
    print(graphics[hangman]) 
    return           
    

def start():
    print('lets play hangman baby\nrules are the following:\nyou have to choose the correct word according to the clue \nthese are the names of some of yours friend')
    while game():
        pass
    scores()

def game():
    dictionary=["akash","sutar","aiiii","ashu","jumbo","champ","shubham","rajesh","kitu","ankit","susuu","raja","prasanna","animesh"]
    word=choice(dictionary)
    word_length=len(word)
    clue=word_length*['_']
    tries=6
    letters_tried=''
    letters_wrong=0
    hangedman(0)
    def clues():
        for i in dictionary:
            if word=='akash' or word=='prasanna':
                st="he is your ex roommate"
            elif word=='aiiii' or word=='sutar' or word=='ankit' or word=='kitu' or word=='susuu':
                st="he is your housemate"
            elif word=='champ' or word=='jumbo' or word=='shubham' or word=='rajesh':
                st="he is your school friend"
            elif word=='raja' or word=='animesh':
                st="he is your roommate"
            elif word=='ashu':
                st="he is your section CR"
            else:
                st="i dont think he is your"
        return st
    s=clues()
    print('the clue is:',s)
    print("the length of word is:",word_length)
    print('_'*word_length)
    global computer_score,player_score

    while (letters_wrong!=tries) and (''.join(clue)!=word):
        letter=guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter)!=-1:
                print('you have already picked',letter)
            else:
                letters_tried+=letter
                first_index=word.find(letter)
                if first_index==-1:
                    letters_wrong+=1
                    print('sorry '+letter+' is not the letter you are searching for ')
                else:
                    print('congo,you get the perfect letter')
                    for i in range(word_length):
                        if letter==word[i]:
                            clue[i]=letter
                        
        else:
            print("choose another")

        hangedman(letters_wrong)
        print("".join(clue))
        print("guesses",letters_tried)

        if letters_wrong==tries:
            print("Game_over")
            print("you loose boy")
            print("The word is: ",word)
            computer_score+=1
            break
        if "".join(clue)==word:
            print("hurrah you won")
            print("the word is: ",word)
            player_score+=1
            break
    return play_again()

def guess_letter():
    print()
    letter=input("take a guess of your friends name\n")
    letter.strip()
    letter.lower()
    print()
    return letter

def play_again():
    answer=input("would you like to play again\nyes or no \n")
    if answer in ('y','yes','yaa'):
        return answer 
    else:
        print("ty for playing the game\nyou will be seen soon\nbyee byeeeeeeee")

def scores():
    global player_score,computer_score
    print("high scores")
    print("player score: ",player_score)
    print("computer score: ",computer_score)    

if __name__=="__main__":
    start()