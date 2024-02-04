import random

print("****** Answers correctly to 3 questions to win the game ! ******\n")

choice1 = random.randint(1, 3)
choice2 = random.randint(1, 3)
choice3 = random.randint(1, 4)

answer = ""

print("# Question 1 #\n")
match choice1:
    case 1:
        print("What is the country with the largest population ?")
        print("1. China")
        print("2. India")
        print("3. USA")
        print("4. Russia")
        
        answer = input()
        if(answer == "2"):
            print("Good answer !\n")
        else:
            print("This is not an answer or the answer is incorrect, you lose !")
            answer = "0"
    case 2:
        print("What is the capital of the USA ?")
        print("1. San Francisco")
        print("2. New York")
        print("3. Los Angeles")
        print("4. Washington")
        
        answer = input()
        if(answer == "4"):
            print("Good answer !\n")
        else:
            print("This is not an answer or the answer is incorrect, you lose !")
            answer = "0"
    case 3:
        print("What is the largest ocean in the world ?")
        print("1. Pacific")
        print("2. Atlantic")
        print("3. Indian")
        print("4. Arctic")
        
        answer = input()
        if(answer == "1"):
            print("Good answer !\n")
        else:
            print("This is not an answer or the answer is incorrect, you lose !")
            answer = "0"
        
        
        
if(answer != "0"):
    
    print("# Question 2 #\n")
    match choice1:
        case 1:
            print("When did Neil Armstrong arrive on the moon ?")
            print("1. 1962")
            print("2. 1969")
            print("3. 1972")
            print("4. 1979")
            
            answer = input()
            if(answer == "2"):
                print("Good answer !\n")
            else:
                print("This is not an answer or the answer is incorrect, you lose !")
                answer = "0"
        case 2:
            print("In which country were the first modern Olympic Games held ?")
            print("1. France")
            print("2. USA")
            print("3. China")
            print("4. Greece")
            
            answer = input()
            if(answer == "4"):
                print("Good answer !\n")
            else:
                print("This is not an answer or the answer is incorrect, you lose !")
                answer = "0"
        case 3:
            print("Who is the Greek god of war ?")
            print("1. Ares")
            print("2. Hades")
            print("3. Zeus")
            print("4. Athena")
            
            answer = input()
            if(answer == "1"):
                print("Good answer !\n")
            else:
                print("This is not an answer or the answer is incorrect, you lose !")
                answer = "0"
                
                
                
if(answer != "0"):
    
    print("# Question 3 #\n")
    match choice1:
        case 1:
            print("Who was the highest paid athlete of the world in 2021 ?")
            print("1. Lionel Messi")
            print("2. Conor McGregor")
            print("3. Cristiano Ronaldo")
            print("4. LeBron James")
            
            answer = input()
            if(answer == "2"):
                print("Good answer, you won !\n")
            else:
                print("This is not an answer or the answer is incorrect, you lose !")
                answer = "0"
        case 2:
            print("How many elements are in the periodic table ?")
            print("1. 72")
            print("2. 154")
            print("3. 96")
            print("4. 118")
            
            answer = input()
            if(answer == "4"):
                print("Good answer, you won !\n")
            else:
                print("This is not an answer or the answer is incorrect, you lose !")
                answer = "0"
        case 3:
            print("What company was initially known as Blue Ribbon Sports ?")
            print("1. Nike")
            print("2. Puma")
            print("3. Adidas")
            print("4. Fila")
            
            answer = input()
            if(answer == "1"):
                print("Good answer, you won !\n")
            else:
                print("This is not an answer or the answer is incorrect, you lose !")
                answer = "0"
        case 4:
            print("What is the longest river in europe ?")
            print("1. Volga")
            print("2. Danube")
            print("3. Oural")
            print("4. Dniepr")
            
            answer = input()
            if(answer == "1"):
                print("Good answer, you won !\n")
            else:
                print("This is not an answer or the answer is incorrect, you lose !")
                answer = "0"