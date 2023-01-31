def number_vowels(word):
	a=word.count('a') + word.count('A')
	e=word.count('e') + word.count('E')
	i=word.count('i') + word.count('I')
	o=word.count('o') + word.count('O')
	u=word.count('u') + word.count('U')
	return(a+e+i+o+u)

def sol_number_vowels(word):
	a=word.count('a') + word.count('A')
	e=word.count('e') + word.count('E')
	i=word.count('i') + word.count('I')
	o=word.count('o') + word.count('O')
	u=word.count('u') + word.count('U')
	return (a+e+i+o+u)


def test_number_vowels():
	assert number_vowels('hat')==sol_number_vowels('hat')
	assert number_vowels('hate')==sol_number_vowels('hate')
	assert number_vowels('beet')==sol_number_vowels('beet')
	assert number_vowels('sky')==sol_number_vowels('sky')
	assert number_vowels('but')==sol_number_vowels('but')
	assert number_vowels('xxx')==sol_number_vowels('xxx')


# run it using command "pytest copied.py" 
#if it will fail ,it will show "copied.py and F sign" and all errors.
#if passed, it will show "copied.py and green dot".




















