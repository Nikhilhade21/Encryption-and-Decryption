
#1
'''import string
import random

print("Choose any of the two options:")
print("1 - Convert message to secret code language")
print("2 - Convert secret code language to readable message")
user_choice = input("Enter 1 or 2: ")

if user_choice == "1":
  # Secret code language
  message = input("Enter your message: ")

  if message == "":
    print("Message can't be empty!")

  elif len(message) < 3:
    secret_code = message[::-1]
    print(f"Your secret code is: {secret_code}")

  else:
    # Remove first letter and append it to the last
    message = list(message)
    first_letter = message[0]
    message.pop(0)
    message.append(first_letter)

    # Add three random characters at the start and the end
    for i in range(3):
      message.insert(i, random.choice(string.ascii_letters))

    for _ in range(3):
      message.append(random.choice(string.ascii_letters))

    secret_code = "".join(message)
    print(f"Your secret code is {secret_code}")

elif user_choice == "2":
  # Decoding the secret code language
  message = input("Enter your secret code message: ")

  if message == "":
    print("Message can't be empty!")

  elif len(message) < 3:
    readable_message = message[::-1]
    print(f"Your message is {readable_message}")

  else:
    message = message[3:len(message)-3]
    message = list(message)
    last_letter = message[len(message)-1]
    message.pop(len(message)-1)
    message.insert(0, last_letter)

    readable_message = "".join(message)
    print(f"Your message is {readable_message}")

else:
  print("Invalid input!")
'''
#2
""""
import string
import random

# User input for code/decode

userInput = input("Choose code/decode option to start :  ")

if userInput.lower() == 'code':
    word = input("Please enter the word to code into secret language : ")
    if len(word)>=3:
        start = word[0]
        end = word[-1]
        # swapped first and last character of word
        word = end + word[1:-1] + start
        # print(word)
        coded_word = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + word + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        print(f"Here is your word in secret language : {coded_word.lower()}")
    else:
        word = word[::-1] 
        print(f"Here is your word in secret language : {word.lower()}")

elif userInput.lower() == "decode":
    word = input("Please secret language word to decode : ")
    if len(word)<3:
        word = word[::-1] 
    else:
        word = word[3:-3]
        # print(word)
        first = word[0]
        end = word[-1]
        word = end + word[1:-1] + first
        print(word)

    
else : 
    print("Wrong Input!")
"""
#3 correct one
import random

def randthree():
	alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	w=""
	for i in range(3):
		rand=random.choice(alpha)
		w=w+rand
	return w

def encode(s):
	words=s.split()
	#print(words)
	l=[]
	for i in words:
		if len(i)==1:
			l.append(i)
			
		elif len(i)==2:
			w=i[1] + i[0]
			#print(w)
			l.append(w)
		
		elif len(i)>2:
			z=list(i)
			p = z.pop(0)
			z.append(p)
			w=""
			for j in z:
				w=w+j
			r1=randthree()
			r2=randthree()
			x=r1+w+r2 
			l.append(x)
	word=" ".join(l)
	return word

def decode(s):
	words=s.split()
	#print(words)
	l=[]
	for i in words:
		if len(i)==1:
			l.append(i)
			
		elif len(i)==2:
			z=list(i)
			w=i[1] + i[0]
			#print(w)
			l.append(w)
		
		elif len(i)>2:
			z=list(i)
			for j in range(3):
				z.pop(0)
				z.pop(-1)
			fw=z.pop(-1)
			z.insert(0,fw)
			w=""
			for j in z:
				w=w+j
			l.append(w)
	word=" ".join(l)
	return word

print("      welcome to secret code exercise")

while True:
	print("\n1. encode\n2. decode\n3. exit")
	inp=int(input("Enter your choice"))
	if inp==1:
		message=input("Enter message to encode: ")
		en=encode(message)
		print ("encoded message is: ",en)
	elif inp==2:
		message=input("Enter message to decode: ")
		d=decode(message)
		print("decoded message is: ",d)
	else:
		break