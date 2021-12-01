# This is my first attempt at learning python, I'm pretty happy with it! 
# cbadder special

#Opening file to be read and put into a list
file = open ('C:\\Users\\12268\\Desktop\\AdventOfCode\\day 1\\input.txt', 'r')

# readlines() creates a list of all lines, Strings
content = file.readlines()

count = 0

# Made this 10k since all input is <10k
lastline = 10000;

for line in content: # for each line in the list...
    for i in line: # i is the counter
        #print(line)
        if int(lastline)<int(line): # if new input is greater than previous input
            count = count + 1 # count it!
            
        lastline = line; #moving last line index up 1

print (count)
