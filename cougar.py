while True:
    try:

        feline_age = int(input("Which feline are you? (Enter your age): "))

        if 0 <= feline_age <= 17:
            print ("Your a Kitten!")
    
        elif 18 <= feline_age <= 21:
            print ("Your a Wildcat!")
    
        elif 22 <= feline_age <= 29:
            print ("Your a Lynx!")
    
        elif 30 <= feline_age <= 39:
            print ("Your a Puma!")
    
        elif 40 <= feline_age <= 49:
            print ("Your a Cougar!")

        elif 50 <= feline_age <= 59:
            print ("Your a Jaguar!") 

        elif 60 <= feline_age <= 68:
            print ("Your a Panther!")

        elif feline_age == 69:
            print ("Your a Pussycat!")
    
        elif 70 <= feline_age <= 79:
            print ("Your a Cheetah!")

        elif 80 <= feline_age <= 89:
            print ("Your a Leopard!")

        elif 90 <= feline_age <= 99:
            print ("Your a Tiger!")   
    
        elif feline_age >= 100:
            print ("Your a Lion!")

        else:
            print("Sorry, I can only categorize ages from 0 to 100.")
        
       # Ask again for age after displaying the category
        continue_input = input("Would you like to enter another age? (yes/no): ").lower()
        if continue_input != "yes":
            break
        
    except ValueError:
        print("Please enter a valid number for your age.")    
    

    
