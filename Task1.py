from itertools import islice

def l33t_code(path):
    with open(path,"r") as targetfile:
        data = targetfile.read()
        data = data.replace('o', '0')
        data = data.replace('O', '0')
        data = data.replace('a', '4')
        data = data.replace('A', '4')
        data = data.replace('e', '3')
        data = data.replace('E', '3')
        data = data.replace('i', '1')
        data = data.replace('I', '1')
    with open(path, 'w') as newfile:
        newfile.write(data)

directory = "/home/sweta/fizzbuzz-sweta"


path = directory + input("Enter filename: ")
if path.endswith('.txt') == False:
    raise ValueError("Invalid file name only txt accepted")

try:
    numberofpages = int(input("Enter number of pages "))
except ValueError:
    print("The Number of pages must be integer only")
    exit()

numberoflines = int(numberofpages) * 25

with open("/home/sweta/fizzbuzz-sweta/samplefile.txt", "r") as myfile:
    linesList = list(islice(myfile,numberoflines))

with open(path,"w") as targetfile:
    for item in linesList:
        targetfile.write(item)

l33t_code(path)