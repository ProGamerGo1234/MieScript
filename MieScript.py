print('Welcome To MieScript')
print('This is an open source code, so you can edit it!')
print('This is version 0.0.1, version ShoeBox')
username = input('What is your name? ')
print('Welcome to the terminal')
print('No need to write the slash in comands.')
print('Write /help for list of comands')
arandom = 0
while True:
 terminnal = input('/')
 if terminnal == ('help'):
  print('Comands for MieScript ShoeBox')
  print('/help for help')
  print('/calculator for calculator')
  print('/magic8ball for Magic 8 Ball')
 elif terminnal == ('calculator'):
  print('Welcome to Calculator')
  anwser = 0
  number1 = int(input('What is the first number?'))
  number2 = int(input('What is the seccond number?'))
  opperation = input('What is the opperation? + or -?')
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
  else:
   print('Random already imported.')
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
 else:
  print('Illigal Comand')
