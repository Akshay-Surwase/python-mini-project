responses=["Hello, My name is Robot Calculator","What Can i help you","Thank you so much","bye-bye","I don't know about this","but next time i surely ansewer your question"]

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def exp(a,b):
    return a**b
def square(a):
    return a*a
def cube(a):
    return a*a*a


def end():
    print(responses[2])
    print(responses[3])

def extract_numbers(t):
    l=[]
    for i in t.split(' '):
        try:
            l.append(float(i))
        except:
            pass
    return l

operations={"ADD":add,"ADDITION":add,"PLUS":add,"SUM":add,"SUB":sub,"SUBTRACTION":sub,"MINUS":sub,"MULTIPLICATION":mul,"MULTIPLY":mul,"MUL":mul,"PRODUCT":mul,"DIVISION":div,"DIVIDE":div,"DIV":div,"EXP":exp,"EXPONENTIAL":exp,"SQUARE":square,"CUBE":cube,}
commands={"BYE":end,"BYE-BYE":end}

print(responses[0])
print(responses[1])

while True:
    t=input("Please Ask:")
    for w in t.split(' '):
        if w.upper() in operations.keys():
            try:
                l=extract_numbers(t)
                if w.upper() in ["SQUARE","FACT","FACTORIAL","CUBE"] and len(l)==1:
                    result=operations[w.upper()](l[0])
                    print(result)
                elif len(l) ==2:
                    result=operations[w.upper()](l[0],l[1])
                    print(result)
                else:
                    print("Eneter correct oprations")
                
                break
            except:
                print("Please ask correct questions")
                break
        elif w.upper() in commands.keys():
            commands[w.upper()]()
            break
    else:
        print(responses[4])
        print(responses[5])