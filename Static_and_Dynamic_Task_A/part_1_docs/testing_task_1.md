### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #requires an equality operator (==) instead of a reasignment. 
      return True
    else #requires a colon after else (else:)
      return False
   

  dif highest_card(self, card1 card2): #def misspelt. Also, need a comma to seperate parameters (card1, card2)
  if card1.value > card2.value: #if bock requires indentation
    return card #variable returned should be 'card1'
  else:
    return card2
  


def cards_total(self, cards): #def requires indentation
  total #total needs to be initialised (total = 0)
  for card in cards:
    total += card.value
    return "You have a total of" + total #total needs to be converted to string type before concatenation ( str(total) ). Also, return statment needs to be unindented to take it out of the for loop. Also, possible bug: require space at end of string ("...total of ")
  
```
