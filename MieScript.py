print('Welcome To MieScript')
print('This is an open source code, so you can edit it!')
print('This is version 0.0.1, version ShoeBox')
username = input('What is your name? ')
print(f'Welcome {username}')
print('Find code at https://progamergo1234.github.io/MieScript/ ')
print('Welcome to the terminal')
print('No need to write the slash in comands.')
print('Write /help for list of comands')
arandom = 0
while True:
 terminnal = input('/')
 if terminnal == ('help'):
  print('Comands for MieScript ShoeBox')
  print('/notebook for notebook.')
  print('/help for help')
  print('/calculator for calculator')
  print('/magic8ball for Magic 8 Ball')
  print('/HPQ for Harry Potter Quiz!')
 elif terminnal == ('calculator'):
  print(f'Welcome to Calculator, {username}.')
  print('CAUTION!!!')
  print('Using decimals will corupt the software.')
  anwser = 0
  number1 = int(input('What is the first number? '))
  number2 = int(input('What is the seccond number? '))
  opperation = input('What is the opperation? + or -? ')
  if opperation == '+':
   anwser = (number1 + number2)
   print (f'{number1} + {number2} = {anwser}')
  else:
   anwser = (number1 - number2)
   print (f'{number1} - {number2} = {anwser}')
 elif terminnal == ('magic8ball'):
  if arandom == 0:
   import random
   arandom = 1
   print('Random imported.')
   print(f'Welcome to magic 8 ball, {username}')
  else:
   print('Random already imported.')
   print(f'Welcome to magic 8 ball, {username}')
  question = input ('Question? ')
  num = random.randint(1, 9)

  if num == 1:
   print('Yes - definitely.')
  elif num == 2:
   print('It is decidedly so.')
  elif num == 3:
   print('Without a doubt.')
  elif num == 4:
   print('Reply hazy, try again.')
  elif num == 5:
   print('Ask again later.')
  elif num == 6:
   print('Better not tell you now.')
  elif num == 7:
   print ('My sources say no.')
  elif num == 8:
   print('Outlook not so good.')
  else:
   print('Very doubtful.')
   
 elif terminnal == ('HPQ'):
  print('Welcome to the Harry Potter quiz!')
  Gryffindor = 0
  Ravenclaw = 0
  Hufflepuff = 0
  Slytherin = 0
  One = int(input('Q1. Do you like Dawn or Dusk? 1. Dawn 2. Dusk '))
  if One == 1:
   Gryffindor += 1
   Ravenclaw += 1
  elif One == 2:
   Hufflepuff += 1
   Slytherin += 1
  else:
   print('Wrong Anwser')
  Two = int(input('Q2. When I’m dead, I want people to remember me as: 1. The Good 2. The Great 3. The Wise 4. The Bold '))
  if Two == 1:
   Hufflepuff += 2
  elif Two == 2:
   Slytherin += 2
  elif Two == 3:
   Ravenclaw += 2
  elif Two == 4:
   Gryffindor += 2
  else:
   print('Wrong Anwser')
  Three = int(input ('Q3. Which kind of instrument most pleases your ear? 1. The violin 2. The trumpet 3. The piano 4. The drum '))
  if Three == 1:
   Slytherin += 4
  elif Three == 2:
   Hufflepuff += 4
  elif Three == 3:
   Ravenclaw += 2
  elif Three == 4:
   Gryffindor += 4
  else:
   print('Wrong Anwser')
  print('You finished the quiz')
  if Gryffindor > Hufflepuff and Gryffindor > Slytherin and Gryffindor > Ravenclaw:
   print('You are a Gryffindor!')
  elif Hufflepuff > Gryffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
   print('You are a Hufflepuff!')
  elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
   print('You are a Slytherin!')
  elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
   print('You are a Ravenclaw!')
  else:
   print('You Failed!')

 elif terminnal == ('notebook'):
  print(f'Welcome to notebook, {username}.' )
  notebookleft = int(1)
  print(f'You have {notebookleft} notebooks left.')
  print('More notebooks may be available after update.')
  print('/Stop will stop the writing')
  notebook1 = ('')
  while notebook1 != ('/stop'):
   notebook1 = input('')
  
 else:
  print('Illigal Comand')
