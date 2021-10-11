from random import randint
import sys
# generate a number 1~10


# input from user?
# check that input is a number 1~10

def run_guess(guess, answer):
    try: 
      if  0 < int(guess) < 11:
          if int(guess) == answer:
            print('you are a genius!')
            return True
    except ValueError as err:
      return False
				
    else:
        print('hey bozo, I said 1~10')
        return False

if __name__ == "__main__":
	answer = randint(1, 10)
	while True:
			try:
					guess = int(input('guess a number 1~10:  '))
					if (run_guess(guess, answer)):
						break
			except ValueError:
					print('please enter a number')
					continue
