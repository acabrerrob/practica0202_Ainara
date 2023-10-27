def eco():
  userInput = input('Escriba lo que usted quiera para hacer eco, si quiere pararlo introduzca salir ')
  
  while userInput == "salir":
    print("Has salido del loop")
    break
  else:
    print(userInput)
    eco()
    
eco()