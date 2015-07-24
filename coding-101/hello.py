#welcome to coding!

#This is just a normal text file. All we have done is named it hello.py.
#The .py extension makes it a python file, which means our text editor knows what the syntax should look like
#and we can run it by pressing cmd + B!


#lines that start with a hashtag/pound sign are commments.
#this means that they don't do anything. 
#it is also common to 'comment out' code that you do not want to run anymore



#print hello world
print "Hello, World"


#Types

# #string
b = "hello"
print b
print type(b)


# #int
c = 5
print type(c)

# #use str() to convert int to a string
d = b + str(c)
print d

e = "5"
f = int(e) + c
print f 









#String Formatting
# %s = for string
name = "Emmett"
text = 'Hi %s, you have 10 dollars in credits!' % name

print text 

name = "D'nae"
credits = 50000
text_2 = "Hi %s, you have %d dollars in credits!" % (name, credits)
print text_2


#list! aka Arrays
names = ['Emmett', "D'nae", "Alex", "Braden", "Nate", "William", "Karen"]
credits = [50, 10 , 3, 100 , 3, 5, 1]

# print len(names)

# #lists are 0 based, which means first item is list[0]
# print names[0]
# print names[2]



for name in names:	
	text_2 = "Hi %s, you have 100 dollars in credits!" % (name)
	print text_2


for a in range(6):
	print 'a = ', a
	text_2 = "Hi %s, you have %d dollars in credits!" % (names[a], credits[a])
	print text_2
