def has_teen(a, b, c):
	if a >= 13 and a <= 19:
		return True
	elif b >= 13 and b <= 19:
		return True
	elif c >= 13 and c <= 19:
		return True
	else:
		return False
print has_teen(9, 15, 7) #expect True
print has_teen(4, 7, 3) #expect False
print has_teen(14, 18, 19) #Expect True
print has_teen(13, 2, 5)# expect True

def not_string(str):
	if str.startswith("not"):
		return (str + "not")
	else: 
		return ("not" + str)

print not_string("nothappy") #Expect not Happy not
print not_string("happy") #Expect not Happy
print not_string("not sad") #Expect not sad
print not_string("sad") #Expect not sad not

def icy_hot(a,b):
	if a < 0 and b > 100:
		return True
	elif b < 0 and a > 100:
		return True
	else:
		return False

print icy_hot(101, 3) #expect True
print icy_hot(10, -9) #expect True
print icy_hot(58, 13) #expect False
print icy_hot(1, 99) #return False

def closer_to(c, a, b): #c is target, b and a are guesses
	differenceA = abs(c - a) 
	differenceB = abs(c - b)
	if differenceA > differenceB:
		return b
	if differenceB > differenceA:
		return a
	if differenceA  == differenceB:
		return 0

print closer_to(4, 90, 5) #expect 4
print closer_to(10, 3, 5) #expect 3
print closer_to(3, 78, 85) #expect 78
print closer_to(8, 1, 2) #expect 1

def two_as_one(a,b,c):
	if a + b == c:
		return True
	elif b + c == a:
		return True
	elif a + c == b:
		return True
	else:
		return False


print two_as_one(2, 3, 5) #expect True
print two_as_one(2, 3, 6) #expect False
print two_as_one(20, 3, 23) #expect True
print two_as_one(1, 5, 2) #expect False

def pig_latinify(str):
	if str.startswith ("a") or str.startswith ("e") or str.startswith ("i") or str.startswith ("o") or str.startswith ("u"):
		return (str + "way")
	if not str.startswith ("a") or not str.startswith ("e") or not str.startswith ("i") or not str.startswith ("o") or not str.startswith ("u"):
			return (str + "ay")

print pig_latinify("Lindsay") #Expect Lindsayay
print pig_latinify("apple") #expect appleway
print pig_latinify("orange") #expect orangeway
print pig_latinify("Puppy") #expect puppyay
