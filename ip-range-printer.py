
# Made By GnikLlort 
# Tool that prints out the entire ip range
# Good For setting up scan lists
# python ip-range-printer.py >> filename.txt

a = 1 
b = 1
c = 1
d = 1


while d < 256: # Everything is done insde the while loop
	print('%i.%i.%i.%i') % (a, b, c, d) # Print the ip out to the terminal
	d += 1
	while d == 256: 
		d = 1
		c += 1
		while c == 256:
			c = 1
			b += 1
			while b == 256:
				b = 1
				a += 1
				while a == 256:
					die('DONE!') # When it gets to 255.255.255.255 it will print "DONE"
