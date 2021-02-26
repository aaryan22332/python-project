introString = input("enter a string:")
characterCount=0
worldCount=1
for i in introString:
    characterCount=characterCount+1
    if(i==' '):
        worldCount=worldCount+1
print("number of words in the string: ")
print(worldCount)
print("number of charaters in the string: ")
print(characterCount)      
          