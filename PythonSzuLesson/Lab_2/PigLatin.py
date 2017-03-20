#-*-coding:utf-8-*-
def PigLatin (theWord) :
	vowel = ['a' , 'e' , 'i' , 'o' , 'u']
	tail = ""
	head = ""
	i = 1
	theWord = theWord.lower ()
	if theWord[0] in vowel :
		theWord = theWord + "hay"

	elif theWord[0:2] == "qu" :
		theWord = theWord[2:] + "qu" + "ay"
	else :
		tail = tail + theWord[0]
		head = theWord[1:]
		for letter in theWord[1:] :
			if (letter in vowel) or (letter == 'y'):
				break
			else :
				i = i + 1
				tail = tail + letter
				head = theWord[i:]
		theWord = head + tail + "ay"
	return theWord

def combination (PrimitiveSentence) :
	PigLationSentence = ""
	for word in PrimitiveSentence.split() :
		PigLationSentence = PigLationSentence + PigLatin (word) + " "
	return PigLationSentence

def main () :
	sentence = raw_input ("please input the sentence : ")
	sentence2PigLatin = combination (sentence)
	print sentence2PigLatin
if __name__ == "__main__" :
	main ()