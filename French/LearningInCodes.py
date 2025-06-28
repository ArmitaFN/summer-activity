import random

mots = {'se débrouiller' : 'to manage, to cope, to get by (especially in a tricky situation)',
        'apercevoir': 'to notice, to catch sight of',
        'améliorer': 'to improve' }
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
    
elif chosen == "cards":
  word = input("French or English? ").lower()
  
    if word == "french":
      random_word = random.choice(list(mots.keys()))
      print(random_word, "❓")
      input("Press Enter to see the meaning!")
      print(mots[random_word], "✅")
      
    elif word == "english":
      random_meaning = random.choice(list(mots.values()))
      print(random_meaning, "❓")
      input("Press Enter to see the word!")
      french_word = next(k for k, v in mots.items() if v == random_meaning)
      print(french_word, "✅")
      
    else:
      raise valueError("Never heard of that before! Make sure to learn it soon so you can add it in Dictionary.😉")
            
else:
  print("You can either choose Dictionary or Cards, want more? Add another section!☺️")
    
      
