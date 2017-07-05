#PASSWORD OF DEFAULT USER IS SAHIL

from spy_detail import spy
from spy_function import spy_verification,spy_choice
print '\033[1;30;49m WELCOME TO THE SPY WORLD'
print "\n ...VERIFICATION..."
verify=raw_input("\n \nDO YOU WANT TO CONTINUE AS MR.SAHIL (Y/N)")
if verify.upper()=="Y":
    password=raw_input("ENTER YOUR PASSWORD")
    if password=="SAHIL":
        print "\nSUMMARIZING YOUR DETAILS..."
        print "\nYOUR NAME IS %s%s. YOUR AGE IS %d. YOUR RATING IS %.2f. YOU ARE ONLINE."%(spy.salutation,spy.name,spy.age,spy.rate)
        spy_choice(spy.name,spy.age,spy.rate)
    else:
        print "INCORRECT PASSWORD"

else:
    spy_verification()
    spy_choice(spy.name,spy.age,spy.rate)
