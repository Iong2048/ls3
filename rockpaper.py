import random
list_str=["bua", "keo","bao "]

def randomskill(list_skill):
    return random.choice(list_skill)

userinput= randomskill(list_str)

machineinput= randomskill(list_str)
def checkresult(user, machine):
    if (user == "keo"):
        if (machine == "bao"):
            print("thang")
        elif(machine == "bua"):
            print("thua")
        else:
            print("hoa")
    if (user == "bua"):
        if (machine == "keo"):
            print("thang")
        elif(machine == "thang"):
            print("thua")
        else:
            print("hoa")
    if (user == "bao"):
        if (machine == "bua"):
            print("thang")
        elif(machine == "keo"):
            print("thua")
        else:
            print("hoa")

print(machineinput)
checkresult(machine= machineinput, user=userinput)

