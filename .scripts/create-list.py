#while i < n do
#print(item + "-" + i)
#new line
#i++

item = input("Enter task or whatever you want to list:") #user input
n = input("Now enter how many list items you wanna create:") #user input
i = 1
while i <= int(n):
    # comment: 
    print(item + "-" + str(i))
    i += 1
# end while