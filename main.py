import random
print("Infinity Dice 🎲")
sides = int(input("how many sides? : "))
playGame = input("roll again?(yes/no)")
def rollDice(sides):
  while True:
    sides = int(input("how many sides? : "))
    #print("you rolled", random.randint(1,sides))
    playGame = input("roll again?(yes/no)")
    print("how many sides?: ")
    print("you rolled", random.randint(1,sides))
    sides = int(input("how many sides? : "))
    playGame = input("roll again?(yes/no)")
    print("roll again? : ")
    if playGame == "yes":
      print("you rolled", random.randint(1,sides))
    else:
      print("no!")
      break
rollDice(sides)
      

      
      
   
 
    

  



    
  

  
