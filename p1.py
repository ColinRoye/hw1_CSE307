
#read line
words = ["False","class","from","or","None","continue",
"global","pass","True","def","if","raise","and",
"del","import","return","as","elif","in","try",
"assert","else","is","while","async","except",
"lambda","with","await","finally","nonlocal",
"yield","break","for","not"]


val = input();
if val in words:
    print("False")
    exit();
#check first char
if val[0].isalpha() or val[0] == '_':
    for i in range(1,len(val)):
        if not (val[i].isalpha() or val[i] == '_' or val[i].isnumeric()):
            print("False")
            exit()
    print("True")
    exit()
print("False")
exit()
#check all char after first char
#check full string
