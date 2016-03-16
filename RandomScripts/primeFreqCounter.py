# primeFreqCounter.py
# A program to count the frequency of prime tens places
# ... in the next prime after one ending in 1
# Author: mflax@leadps.org

# takes a number and the list of primes between 2 and the number
# returns True if it's prime
def isPrime(n, primeList):
	# walk through the prime numbers between 1 and n
	# a better applied mathematician would have a better method, probably
	for a in primeList:
		# if a goes evenly into n, return False
		if n % a == 0:
			return False
	
	# if we get this far, it's prime
	return True

# takes a list of ints and the desired tensDigit to be counted
# returns the number of integers 
def countTens(myList, tensDig):
	count = 0
	for n in myList:
		if n % 10 == tensDig:
			count += 1
	return count

def printTensFreqs(followerPrimeList):
	# aside from 2 and 5, this is all the primes
	ones = countTens(followerPrimeList, 1) * 1.0
	threes = countTens(followerPrimeList, 3) * 1.0
	sevens = countTens(followerPrimeList, 7) * 1.0
	nines = countTens(followerPrimeList, 9) * 1.0

	sum = len(followerPrimeList)
	print("Total: " + str(sum))

	print("Ones: " + str(ones/sum))
	print("Threes: " + str(threes/sum))
	print("Sevens: " + str(sevens/sum))
	print("Nines: " + str(nines/sum))

# start with a blank list
primeList = []

# go this far, program - magic number
limit = 100000

# count to the limit
for n in range(2, limit):
	if isPrime(n, primeList):
		primeList.append(n)

# write the list to a file

myFile = open('primes.txt', 'w')
for p in primeList:
	myFile.write(str(p) + '\n')
myFile.close()

# make special lists for each of our followers
# then calculate the frequencies for the follower lists

enders = [1, 3, 7, 9]
for e in enders:
	# var to tell whether to store the *next* number
	followerList = []
	nextFollower = False

	# build the followerList by checking if each prime ends in e
	# and if it does, promise to store the next prime
	for prime in primeList:
		if nextFollower:
			followerList.append(prime)
		nextFollower = False
		if prime % 10 == e:
			nextFollower = True
	
	# now check/print the stats
	print("For primes following a prime ending in " + str(e) + ":")
	printTensFreqs(followerList)

