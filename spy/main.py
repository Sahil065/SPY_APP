#PLEASE READ THE INTRODUCTION CAREFULLY FOR EFFICIENT USE OF SPY_CHAT

#PASSWORD OF DEFAULT USER IS SAHIL


#THIS APP HELPS YOU TO HAVE A SECRET CONVERSATION WITH YOUR SPY FRIENDS


'''THE APP CONTAINS ALL THE MANDATORY OBJECTIVES AS WELL AS ALL THE EXTRA OBJECTIVES

THE USER HAVE TO ENTER RIGHT INFORMATION TO USE THE APP

ALWAYS ENTER INTERGER WHERE IT IS ASKED ...
ENTERING ANY OTHER DATATYPE WILL GENERATE THE UNWANTED TERMINATION OF APP
'''





#Importing Files/Library in order to use them
from spy_detail import spy
from spy_function import spy_verification,spy_choice
from termcolor import colored


print ('WELCOME TO THE SPY WORLD')
print colored('\n IM YOUR PERSONAL ASSISTANT JARVIS','green')
print "\n...VERIFICATION..."
while True:

    #asking whether user want to continue as default user or not
    verify=raw_input("\n \nDO YOU WANT TO CONTINUE AS MR.SAHIL (Y/N).")
    if verify.upper()=="Y":
        password=raw_input("ENTER YOUR PASSWORD")
        if password=="SAHIL":
            print colored("\nWELCOME BACK SIR. IT IS ALWAYS NICE TO WORK WITH YOU", 'green')
            print colored("\nSUMMARIZING YOUR DETAILS...",'green')
            print colored("\nYOUR NAME IS %s%s. YOUR AGE IS %d. YOUR RATING IS %.2f. YOU ARE ONLINE.",'green')%(spy.salutation,spy.name,spy.age,spy.rate)
            spy_choice(spy.name,spy.age,spy.rate)
        else:
            print colored("INCORRECT PASSWORD",'red')

    elif verify.upper()=="N":
        spy_verification()
        spy_choice(spy.name,spy.age,spy.rate)
    else:
         print colored("ENTER VALID INPUT","red")