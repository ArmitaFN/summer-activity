mots = {'se débrouiller' : 'to manage, to cope, to get by (especially in a tricky situation)', 'apercevoir': 'to notice, to catch sight of'}
# I add every new word i learn
word = ' '
chosen = ' '
chosen = input("What do you want to work with? ").lower()
if chosen == "dictionary":
  word = input("What word are you looking for? ").lower()
  if word in mots:
    print(f'It means {mots[word]}')
  else:
    print("Oops, there is no word like that! Let's add it now!😊")
  
