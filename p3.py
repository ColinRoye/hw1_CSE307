#remove all escape characters
#validate begining and end quotes
def str_fail(num):

    print("False" + num)
    exit()
def str_pass():
    print("True")
    exit()

s1 = input()
s2 = input()

singleQuoteStringState = False
doubleQuoteStringState = False

illegalChar = []
escapableChars = ['\'', '\"', '\n', '\\']

escapeState = False

if(s1[0] == '\''):
    singleQuoteStringState = True
    illegalChar.append('\'')
elif s1[0] == '\"':
    doubleQuoteStringState = True
    illegalChar.append('\"')
else:
    print("False")
    exit()

# if (s1[-1] == '\'' or s1[-1] == '\"') and len(s2) > 0:
#     print("False")
#     exit()


for i in range(0,len(s1)):
    current = s1[i]
    if current == '\\':
        escapeState = not escapeState
        continue
    if current in escapableChars and escapeState:
        escapeState = not escapeState
        continue
    if current not in escapableChars and escapeState:
        str_fail("1")
    if current in illegalChar and (len(s2) > 0 or i < len(s1)-1) and i != 0:
        print(illegalChar)
        print(current)
        str_fail("2")
if len(s2) == 0:
    if s1[-1] != '\'' and singleQuoteStringState:
        str_fail("3")
    if s1[-1] != '\"' and doubleQuoteStringState:
        str_fail("4")
    str_pass()
elif s1[-1] != '\\':
    str_fail("5")
elif not escapeState:
    str_fail("6")

for i in range(0,len(s2)):
    if current == '\\':
        escapeState = not escapeState
        continue
    if current in escapableChars and escapeState:
        escapeState = not escapeState
        continue
    if current not in escapableChars and escapeState:
        str_fail("7")
    if current in illegalChar and (i < len(s2)-1):
        str_fail("8")
if doubleQuoteStringState:
    if s2[-1] != '\"':
        str_fail("9")
if singleQuoteStringState:
    if s2[-1] !=  '\'':
        str_fail("10")
str_pass()
