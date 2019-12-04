import sys

def Find(los):
    endResult=False
    number=0
    for name in los:
        number=number+1

        if (name=="Soroush"):
            endResult=True
            print(number)
            break


    if(endResult==True):

        print("I found Soroush :)")
    else:
        print("I didn't find Soroush")
Find(sys.argv)

print("Quitting program + some other change")



