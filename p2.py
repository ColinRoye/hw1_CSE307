#read line
#check valid int
#switch
    #convert scientific notation to regular int



def removeNeg(val):
    if val[0] == '-':
        return val[1:]
    return val
def valBase(val, base):

    accept = []
    gt9lower = ['a','b','c','d','e','f']
    gt9Upper = ['A','B','C','D','E','F']
    for i in range(0, base):
        if(i <= 9):
            accept.append(str(i))
        else:
            accept.append(gt9lower[i%10])
            accept.append(gt9Upper[i%10])

    sciFlag = 0
    if val[0] == '0':
        return False

    val = removeNeg(val)
    for i in range(0,len(val)):
        if val[i] not in accept:
            return False
    return True
def isValidInt(val):
    #INT
        base = val[0:2]
        #base2
        if base == "0b" or base == "0B":
            if valBase(val[2:],2):
                return True
                        #base8
        if base == "0o" or base == "0O":
            if valBase(val[2:],8):
                return True

        #base16
        if base == "0x" or base == "oX":
            if valBase(val[2:],16):
                return True
        return valBase(val,10)




def isValidFloat(val):
    accept = []
    for i in range(0, 10):
        accept.append(i)
    decFlag = 0
    for i in range(0,len(val)):
        if val[i] in accept:
            continue
        if (val[i] == 'e' or val[i] == 'E') and (i != len(val)-1):
            return isValidInt(val[i+1:])
        if(val[i] == '.'):
            if decFlag == 0:
                decFlag = 1
                continue
            else:
                return False

    return True


val = input()

if isValidInt(val):
    print("Int")
    exit()
if isValidFloat(val):
    print("Float")
    exit()
print("None")