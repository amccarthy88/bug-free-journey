#takes a string and returns if all the characters are unique or not

def unique(word):
  newWord = sorted(word)
  setWord = set(word)
  return len(newWord) == len(setWord)

print(unique('unique'))
