text = str(input("Enter sentence to be turned into camel case:\n"))
text = text.lower()
textList = text.split(" ")

position = 0
text2 = ""

for element in textList:
    textList[position] = element.capitalize()
    position += 1

position = 0
for element in textList:
    text2 += textList[position]
    position += 1

text2 = text2[0].lower() + text2[1:]
print(text2)
