def test(greeting):
    if greeting == "hello":
        return "Hi"
print (test("hello"))
print ""
#print ("How are you?")
h = raw_input ("How are you?")
#if input == "good"
#    return "great"
print ""
print (h + " good").split(",")
#ask = str(input ("Would you care to find the king number?"))
ask = raw_input("Will you play to find the king number?")
#no = 0

#no = "no" or "n"
if ask.lower() in ['no','n']:
#if no == True:
    print ("Too bad, you're playing it anyway.")

num = input("Now enter your favorite number:")
add = num +  3

print (add)
print (" is your favorite number plus three.")
print ""
a = 7
if num == a:
    print ("your number is 7, the king of numerical rulers.")
else: print ("your number is subject to the rule of the king number")

def division():
    print num / 7
    print ("That is your number divided by the king number.")
division()


#if add >= 7
#    print ("your number is at least 7.")


#a, b = input("Guess two numbers")#.split(",")
#print (a)
#print (b)
