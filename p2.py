#read line
val = input();
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

        #leading zeros for int not valid

        #base2
            #ignore neg
            #no number > 1
        #base8
            #ignore neg
            #no number > 7
        #base16
            #ignore neg
            #no number > 15
    return True
def isValidFloat(val):
    #FLOAT
        #check decimal
    return True
    
def conatainsFrac(val):
    return True
