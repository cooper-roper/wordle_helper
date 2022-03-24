
def main():	
	while(1):
		wordle()

def wordle():
	prompt = "\nEnter 5 letter word. Type ? to indicate unknown characters. If no greens, type '?????'. Also type ? for yellow spaces. We will fill those in later:\n\n"

	file = open("wordlist.txt", "r")
	list= file.read().split('\n')

	res = []
	check = True
	while(check):
		word = input(prompt)
		word = word.strip()
		length = len(word)
		if length == 0:
			prompt = ""
		elif word == "exit":
			exit()
		elif length != 5:
			prompt = "invalid. Try again:\n\n"
		else:
			check = False

	if(word == "?????"):
		result = list
	else:
		i = 0
		for char in word:
			if char != '?': 
				l = []
				if char.isalpha():
					char = char.lower()
					for elem in list:
						if char == elem[i]:
							l.append(elem)
					res.append(l)
				else:
					print("found invalid character")
					return	
			i+=1
	
		result = set.intersection(*map(set,res))

	if len(result) == 1:
		print("the word is ", result)
		return
	elif len(result) > 1:
		print("possible words:")
		print("__________________________________________")
		print(result)
	else:
		print("No words")
		return

	prompt = "\n\nEnter yellow letters. Same format as earlier, '?' for greens or grey. If none, hit enter. After, we will check available keyboard letters. Type 'exit' to exit\n\n"
	yellows = input(prompt)
	yellows = yellows.strip()
	if yellows == "exit":
		exit()
	elif len(yellows) == 0 or yellows == "?????":
		y_result = result
					
	elif(len(yellows) > 5):
		print("invalid input or too many yellows")
		return
	

	else:
		i = 0
		y_result = []
		for char in yellows:
			if char != '?': 
				l = []
				if char.isalpha():
					char = char.lower()
					for r in result:
						if r.find(char) != i and r.find(char) != -1:
							l.append(r)
					y_result.append(l)
				else:
					print("found invalid character")
					return	
			i+=1
	
		y_result = set.intersection(*map(set,y_result))

	if len(y_result) == 1:
		print("the word is ", y_result)
		return
	elif len(y_result) > 1:
		print("possible words:")
		print("__________________________________________")
		print(y_result)
	else:
		print("No words")
		return

		
	prompt = "\n\nEnter the letters that you have used:\n\n"
	greys = input(prompt)
	greys = greys.strip()
	if greys == "exit":
		exit()
	elif greys.isalpha():
		g_result = []
		for char in greys:
			char = char.lower()
			l = []
			for r in y_result:
				if(r.find(char) == -1):
					l.append(r)
			g_result.append(l)
			
	else:
		print("invalid input or too many yellows")
		return

	g_result = set.intersection(*map(set,g_result))
	if len(g_result) == 1:
		print("the word is ", g_result)
	elif len(g_result) > 1:
		print("possible words:")
		print("__________________________________________")
		print(g_result)
	else:
		print("No words")

	print("__________________________________________\n\n\n")
	return



if __name__ == "__main__":
    main()
