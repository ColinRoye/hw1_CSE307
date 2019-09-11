#read line
val = input()
#check valid int
#switch
    #convert scientific notation to regular int

if 'e' in val:
    val = convScientific(val)
if 'E' in val:
    val = convScientific(val)
if containsFrac(val):
    if isValidFloat(val):
        return "Float"
if isValidInt():
    return "Int"
return "None"

def isValidInt(val):
    #INT
        base = val[0:2]
        #base2
        if base == "0b" or base == "0B":
            if isValidB2(val):
                return True;
                        #base8
        if base == "0o" or base == "0O":
            if isValidB8(val):
                return True

        #base16
        if base == "0x" or base == "oX":
            if isValidB16(val):
                return True

        #check num '.', '-', 'e', 'E'
        if isValidB10(val):
            return True

        return False


def isValidFloat(val):

    return True
