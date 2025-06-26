mots = {'se débrouiller' : 'to manage, to cope, to get by (especially in a tricky situation)', 'apercevoir': 'to notice, to catch sight of'}
# I add every new word i learn
word = ' '
chosen = ' '
chosen = input("What do you want to work with? ")
if chosen == "Dictionary":
  word = input("what word are you looking for? ")
  print(f'it means {mots[word]}')
  
