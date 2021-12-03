import urllib.request
import random


def infilt(a):
	b = 0
	while len(a) != 1:  # limits the entry to one character
		a = input("Please enter at least or only one letter.")
	while a in bad:  # prevents the same letter from being entered twice
		a = input("Please pick a new letter.")
	while a in good:
		a = input("Please pick a new letter.")
	while b == 0:  # limits the entries to the alphabet
		if ord(a) not in range(65, 123):
			a = input("Please enter a letter.")
		elif ord(a) in range(91, 97):
			a = input("Please enter a letter.")
		else:
			a = a.lower()
			b = 1


def worda(wordn):  # Function to display the word as ____.
	mystery = "_"*int(len(wordn))
	b = 0
	while b != len(good):
		e = []
		c = wordn
		d = c.index(good[b])
		e.append(d)
		f = list(c)
		f[e[-1]] = "0"
		c = ''.join(f)
		while d != -1:
			d = c.find(good[b])
			if d != -1:
				e.append(d)
				f[e[-1]] = "0"
				c = ''.join(f)
			else:
				g = len(e)
			h = 0
			while h != len(e):
				i = list(mystery)
				i[e[h]] = good[b]
				mystery = ''.join(i)
				h = int(h)+1
		b = b+1
	print(mystery)
	if mystery == wordn:
		win = 1
		tries


def man(tries):  # Hangman drawing
	if tries == 0:
		print("  _____")
		print(" |     |")
		print("       |")
		print("       |")
		print("       |")
		print("       |")
		print(" --------")
	if tries == 1:
		print("  _____")
		print(" |     |")
		print(" @     |")
		print(" |     |")
		print("       |")
		print("       |")
		print(" --------")
	elif tries == 2:
		print("  _____")
		print(" |     |")
		print(" @     |")
		print("/|     |")
		print("       |")
		print("       |")
		print(" --------")
	elif tries == 3:
		print("  _____")
		print(" |     |")
		print(" @     |")
		print("/|\    |")
		print("       |")
		print("       |")
		print(" --------")
	elif tries == 4:
		print("  _____")
		print(" |     |")
		print(" @     |")
		print("/|\    |")
		print("  \    |")
		print("       |")
		print(" --------")
	elif tries == 5:
		print("  _____")
		print(" |     |")
		print(" @     |")
		print("/|\    |")
		print("/ \    |")
		print("       |")
		print(" --------")


# Pulls a dictionary from free bsd to randomly choose a word out of.
dictionary = "http://svnweb.freebsd.org/base/head/share/dict/web2?view=co"
raw = urllib.request.urlopen(dictionary)
lessraw = raw.read()
words = lessraw.splitlines()
wordnum = random.randint(0, 235924)
word = str(words[int(wordnum)])
wordn = word[2:-1]
tries = 0
good = []
bad = []
a = input("Welcome to Hangman. The word is "+str(len(wordn)) +
          " letters long, what is your first letter guess?")
infilt(a)
win = 0


def goodOccurred(good, wordn, a):
  good_occur = wordn.count(a)
  if good_occur > 0:
    while(good_occur > 0):
 	    good.append(a)
  	    good_occur -= 1
	    return True
  return False


good_occur = wordn.count(a)
if good_occur > 0:
	while(good_occur > 0):
		good.append(a)
	good_occur -= 1
	print("Your letter is in the word.")
else:
	print("Your letter is not in the word.")
	bad.append(a)
	tries = int(tries)+1
print("You have guessed wrong "+str(tries)+" time and "+ \
      str(5-int(tries))+" left, with the letter "+str(bad)+".")
man(tries)
worda(wordn)
print(wordn)
while tries != 5: #limits the number of tries to five
	a = input("What is your next guess? ")
	infilt(a)
	if goodOccurred(good, wordn, a):
		print("Your letter is in the word.")
	else:
		print("Your letter is not in the word.")
		bad.append(a)
		tries = int(tries)+1
	print("You have guessed wrong "+str(tries)+" times and "+str(5-int(tries))+ \
	      " left, with the letters "+str(bad)+".")  # wrong guesses displayed and tries left
	man(tries)
	worda(wordn)
	if len(good) == len(wordn):
	  win += 1
	if win == 1:
	  print("Congratulations you won!")
	  name = input("Enter your name to save your score")
	  break
else:
  print("Sorry you used up all your tries, the word was "+str(wordn)+".")
  man(tries)
