
lucky_numbers = [5, 8, 11, 20, 24, 31, 43, 43] #some random numbers
friends = ["John", "Mike", "David", "Danny", "Joel", "Karen"] #random people

friends2 = friends.copy() #copy the list

friends.append("Creed") #this add something on the end of the list
friends.insert(1, "Robin") #this will add it into the list and delete that on the position

friends.remove("Danny") # remove the certain information from the list
friends.pop() #removes the last element of the list
friends.sort() #sort them by alphabet

print(friends.index("David")) #print the order of the character
print(lucky_numbers.count(43)) #counts how many times is the item on the list
print(friends)



