#WORK IN PROGRESS
#cexking
key = input("Enter the # of Rails: \n")
userInput = input("Type the text you want encrypted: \n")
railCount = int(key)

railList =[[] for i in range(railCount)]

keyList = [(letter,i) for i, letter in enumerate(key)]

keyList.sort(key=lambda x: x[1])

currentRail = 0

direction = 1

encryptedText = ""

for char in userInput: 
    railList[currentRail].append(char)
    currentRail += direction
    if currentRail == 0 or currentRail == railCount -1:
        direction = -direction
for pair in keyList: 
    index = pair[1]
    rail = "".join(railList[index])
    encryptedText = " ".join(railList[index])
    print (encryptedText)

