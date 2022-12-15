def main():
	with open('wordlist.txt') as f:
	    word_list = f.read().splitlines()
	
	while(True):
		state = {
			"green": "\nEnter your green results. Type \"?\" in the positions of yellow or grey results. If no greens, type '?????':\n\n", 
			"yellow": "\n\nEnter yellow results. Same format as earlier, '?' for greens or greys. If no yellows, hit enter:\n", 
			"grey": "\n\nEnter the grey letters that you have used:\n\n"
		}

		for _ , (color, prompt) in enumerate(state.items()):
			guess = valid_input(prompt, color)
			
			word_list = [word for word in word_list if checker(guess, word, color)]
		
			if (check_list(word_list) == -1):
				with open('wordlist.txt') as f:
	   				word_list = f.read().splitlines()
				break

def valid_input(prompt, color):
	while(True):
		word = ''.join([char.lower() for char in input(prompt).strip() if not char.isdigit()]) 
		if (len(word) == 5 or color == "grey"):
			return word
		if word == "exit":
			exit()
		prompt = "invalid. Try again:\n\n"

def check_list(res):

	if len(res) > 0:
		print("possible words: \n__________________________________________\n", res)
		return 0
	else:
		print("No words, restarting script\n")
		return -1

def checker(guess, word, color):
	
	for i, char in enumerate(guess):
		
		if(char == "?"):
			continue
		
		elif(not char.isalpha()):
			print("Unknown character: fatal error. Exiting...\n")
			exit(-1)
		
		elif(color == "green" and char != word[i]):
			return False
		
		elif(color == "yellow" and (char not in word or char == word[i])):
			return False

		elif(color == "grey" and char in word):
			return False

	return True
			
	

if __name__ == "__main__":
    main()
