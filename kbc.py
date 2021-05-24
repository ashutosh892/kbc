from questions import QUESTIONS

def isAnswerCorrect(question, answer):
    return True if answer == question["answer"] else False

def lifeLine50(ques):
    a=ques["answer"]
    if a==1 :
        print(f'\t\tOption 1: {ques["option1"]}')
        print(f'\t\tOption 2: {ques["option2"]}')
    elif a==2:
        print(f'\t\tOption 2: {ques["option2"]}')
        print(f'\t\tOption 3: {ques["option3"]}') 
    elif a==3:
        print(f'\t\tOption 3: {ques["option3"]}')
        print(f'\t\tOption 4: {ques["option4"]}')
    else:
        print(f'\t\tOption 4: {ques["option4"]}')
        print(f'\t\tOption 1: {ques["option1"]}')           
    print()    

def kbc():
    total_won=0
    print("\t\t\t\t\t\tWELCOME TO KON BANEGA CROREPATI\n")
    prize=0
    y,z=1,1
    lifeline=2
    for i in range(0,15):
        a=0
        if lifeline==2:
            print("\t\tlifeline : 50-50 and swap_question",end=" ")
        elif lifeline==1 and y:
            print("\t\tlifeline : 50-50",end= " ")
        elif lifeline==1 and z:
            print("\t\tlifeline : swap_question",end=" ")
        else:
            print("\t\tlifeline : lifelines exhausted",end=" ")
        print("\t\twinning_prize :",QUESTIONS[i]["money"],end=" ")
        print("\t\t(type 'quit' to quit the game)\n\n")

        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
        print(f'\tOptions:')
        print(f'\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\tOption 4: {QUESTIONS[i]["option4"]}')
        print()
        if lifeline==2 and i!=14:    
            ans = input('Your choice ( 1-4 ) or type "50-50" or "swap_question" to use any of the one lifeline : ')
        elif lifeline==1 and i!=14 and y:
            ans = input('Your choice ( 1-4 ) or type "50-50" to use another lifeline :')
        elif lifeline==1 and i!=14 and z:
            ans = input('Your choice ( 1-4 ) or type "swap_question" to use another lifeline :')
        else:
            ans = input('Your choice ( 1-4 ) :')
        if i!=14:
            while (ans=="50-50" and not y) or (ans=="swap_question" and not z):
                    print("\n\t\t\t\tdon't cheat with the game ! you can use only available lifelines\n\n")
                    ans = input('Your choice : ')
            if ans=="50-50" and y:
                a=0
                lifeLine50(QUESTIONS[i])
                lifeline-=1
                y-=1
                if z:
                    ans = input('Your choice or type "swap_question" to use another lifeline :')
                else:
                    ans = input('Your choice : ') 
                while (ans=="50-50" and not y) or (ans=="swap_question" and not z):
                    print("\n\t\t\t\tdon't cheat with the game ! you can use only available lifelines\n\n")
                    ans = input('Your choice : ')               
            if ans=="swap_question" and z:
                a=1
                if 0<=i<5:
                    r=-3
                elif 5<=i<11:
                    r=-2
                else:
                    r=-1        
                print(f'\tQuestion {i+1} swapped : {QUESTIONS[r]["name"]}' )
                print(f'\tOptions:')
                print(f'\t\tOption 1: {QUESTIONS[r]["option1"]}')
                print(f'\t\tOption 2: {QUESTIONS[r]["option2"]}')
                print(f'\t\tOption 3: {QUESTIONS[r]["option3"]}')
                print(f'\t\tOption 4: {QUESTIONS[r]["option4"]}')
                lifeline-=1
                z-=1
                if y:
                    ans = input('Your choice or type "50-50" to use another lifeline :')
                else:
                    ans = input('Your choice : ') 
                while (ans=="50-50" and not y) or (ans=="swap_question" and not z):
                    print("\n\t\t\t\tdon't cheat with the game ! you can use only available lifelines\n\n")
                    ans = input('Your choice : ')        
            if ans=="50-50" and y:
                a=0
                lifeLine50(QUESTIONS[i])
                lifeline-=1
                y-=1
                if z:
                    ans = input('Your choice or type "swap_question" to use another lifeline :')
                else:
                    ans = input('Your choice : ') 
                while (ans=="50-50" and not y) or (ans=="swap_question" and not z):
                    print("\n\t\t\t\tdon't cheat with the game ! you can use only available lifelines\n\n")
                    ans = input('Your choice : ')           
        while i==14 and (ans=="50-50" or ans=="swap_question"):
            print("\n\t\t\t\tyou can't use lifeline at the end of the game \n\n")
            ans = input('Your choice : ')
        if ans=="quit":
            break    
        if a==0:
            if isAnswerCorrect(QUESTIONS[i], int(ans) ):
                print('\nCorrect !')
                prize+=QUESTIONS[i]["money"]
                if i==4:
                    print("\n\t\t\t\t\tCONGRATULATIONS !! YOU HAVE PASSED LEVEL ONE\n")
                elif i==10:
                    print("\n\t\t\t\t\tCONGRATULATIONS !! YOU HAVE PASSED LEVEL TWO\n")
                elif i==14:
                    print("\n\t\t\t\t\tCONGRATULATIONS !! YOU HAVE COMPLETED THE GAME\n")        
                if i!=14:
                    print("\ttotal till now : ",prize,end=" ")
            else:
                print('\nIncorrect !')
                if 0<=i<4:
                    total_won=0
                elif 4<=i<11:
                    total_won=10000   
                elif i>=11:
                    total_won=320000     
                break    
        elif a==1:
            if isAnswerCorrect(QUESTIONS[r], int(ans) ):
                print('\nCorrect !')
                prize+=QUESTIONS[i]["money"]
                if i==4:
                    print("\t\t\nCONGRATULATIONS !! YOU HAVE PASSED LEVEL ONE\n")
                elif i==10:
                    print("\t\t\nCONGRATULATIONS !! YOU HAVE PASSED LEVEL TWO\n")
                elif i==14:
                    print("\t\t\nCONGRATULATIONS !! YOU HAVE COMPLETED THE GAME\n")        
                print("\ttotal till now : ",prize,end=" ")
            else:
                print('\nIncorrect !')
                if 0<=i<4:
                    total_won=0
                elif 4<=i<11:
                    total_won=10000   
                elif i>=11:
                    total_won=320000     
                return total_won
    total_won=prize
    return total_won
total_won=kbc()
print("\tThankyou for playing with us !! you've won total money : ",total_won)