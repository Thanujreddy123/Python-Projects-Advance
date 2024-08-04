#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

listnames=[]
with open("./input/Names/invited_names.txt")as name:
    listnames=name.readlines()
people=len(listnames)
with open("./input/Letters/starting_letter.txt")as mail:
    content=mail.read()
    for i in range(0,people):
        actualresult=content.replace("[name]",listnames[i].strip())
        with open("./Output/ReadyToSend/letterto"+listnames[i].strip(),'w') as outputfile:
            outputfile.write(actualresult)

