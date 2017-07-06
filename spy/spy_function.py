#Importing Files/Library in order to use them
from spy_detail import Spy,spy,chat_Message
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored


#Function to input the details of New User
def spy_verification():
    spy.name=raw_input('\n\nENTER YOUR NAME...')

    #name verification
    while True:
        spy.length= len(spy.name)
        if spy.length==0:
            print colored("\n\nINVALID NAME",'red')
            spy.name=raw_input("\nENTER VALID NAME")
        else:
            break

    #asking for the details
    print "\n\nENTER YOUR DETAILS..."

    #asking for gender
    spy.gender = raw_input("\n\nENTER YOUR GENDER (MALE/FEMALE)...")
    while True:
        if len(spy.gender.upper())==0:
            print colored("YOU ENTER INVALID INFORMATION",'red')
        if spy.gender.upper()=="MALE" or spy.gender.upper()=="FEMALE":
            break
        spy.gender=raw_input("ENTER A VALID INPUT")

    #asking for salutation
    spy.salutaion =raw_input("\n\nSHOULD I CALL YOU MR OR MISS")
    while True:
        if len(spy.salutaion.upper()) == 0:
            print colored("\nYOU ENTER INVALID INFORMATION", 'red')
        if spy.salutaion.upper() == "MR" or spy.salutaion.upper() == "MISS":
            break
        spy.salutaion = raw_input("ENTER A VALID INPUT")

    #asking for age
    spy.age =int(raw_input("\nENTER YOUR AGE"))
    if spy.age>12 and spy.age<50:
        print colored("\nVALID AGE",'green')
    else:
        while True:
            print (colored("\nINVALID AGE",'red'))
            spy.age = int(raw_input("ENTER VALID AGE"))
            if spy.age > 12 and spy.age < 50:
               break

    #asking for rating
    while True:
        spy.rate = float(raw_input("\n\nENTER YOU RATING(OUT OF 5)"))
        if spy.rate<=5:
            if spy.rate >= 4.6 and spy.rate <= 5.0:
                print colored("\nYOU HAVE NO MATCH",'green')
            elif spy.rate >= 3.5 and spy.rate <= 4.5:
                print colored("\nYOU ARE EXCELLENT",'green')
            elif spy.rate >= 2.5 and spy.rate < 3.5:
                print colored("\nYOU ARE GOOD",'green')
            else:
                print colored("\nYOU ARE NOT BAD",'green')
            break
        else:
            print colored("INVALID RATING","red")
            print colored("\n I GUESS YOU ARE TRYING TO BE OVERSMART....BUT IM ONE STEP AHEAD","red")
            print colored("ENTER A VALID RATING","red")

    #asking whether spy wants to stay online or not
    print "\n\nYOU WANT TO STAY ONLINE "
    spy_status=int(raw_input("\n1.PRESS 1 FOR YES \n2.PRESS 2 FOR NO"))
    if spy_status==1:
        spy.online=True
        print colored("\n\nSUMMARIZING YOUR DETAILS...",'green')
        print colored("\n \n YOUR NAME IS %s. YOUR AGE IS %d. YOUR RATING IS %.2f. YOU ARE ONLINE.","green")%(spy.name,spy.age,spy.rate)
    else:
        spy.online=False
        exit(colored("\nBYE..... \n HAVE A GOOD DAY",'red'))


#declaring list for status
status_list=[]

#declaring list for friends
friend=[]


#Function to spy friends
def add_friend(spy_rate):
    spy.rate = float(spy.rate)
    new_friend=Spy('','','',19,4.8)
    new_friend.name=raw_input("\nENTER YOUR NAME")
    new_friend.gender=raw_input("ENTER YOUR GENDER (MALE/FEMALE)")
    new_friend.salutation=raw_input("SHOULD I CALL YOU MR OR MISS")
    new_friend.age=int(raw_input("ENTER YOUR AGE"))
    new_friend.rate=float(raw_input("ENTER YOUR RATING"))

    #checking validity
    if len(new_friend.name)>0 and new_friend.age>12 and new_friend.age<50 and new_friend.rate>=spy.rate:
        friend.append(new_friend)
        print colored("\n%s IS SUCCESSFULLY ADDED TO YOUR FRIEND LIST",'green')%(new_friend.name)
        print colored("\nCONGRATS NOW YOU HAVE %d FRIENDS","green")%(len(friend))
    else:
        print colored("\n\nSORRY DETAILS ARE NOT SUFFICIENT","red")
    return len(friend)



#Function to select a friend
def select_friend():
    if friend==[]:
        print colored("\n\nYOU HAVE NO FRIENDS\nPLEASE ADD SOME","blue")
    else:
        position=1
        print"\n YOUR FRIEND LIST IS...."
        for friends in friend:
            print colored("%d. %s aged %d having rating %.2f is online","blue")%(position,friends.name,friends.age,friends.rate)
            position=position+1
        c=int(raw_input("\nSELECT ANY FRIEND"))
        if c<=position:
            return c-1
        else:
            print colored("WRONG INPUT","red")



#Function to send a secret message to SPY friend
def send_a_message():
    m_sender=select_friend()
    if m_sender!=None:
        original_image=raw_input("PLEASE ENTER THE NAME OF THE IMAGE...")
        output_path=raw_input("ENTER THE OUTPUT PATH")
        text=raw_input("ENTER YOUR MESSAGE")
        Steganography.encode(original_image,output_path,text)

    #storing secret message to chats list
        new_chat=chat_Message(text,datetime.now(),True)
        friend[m_sender].chats.append(new_chat)
        print colored("\nYOUR SECRET MESSAGE IMAGE IS READY","green")



#Function to read a secret message from SPY friend
def read_a_message():
    m_recieve=select_friend()
    if m_recieve != None:
        output_path=raw_input("\nPLEASE ENTER NAME OF THE IMAGE...\n")
        hidden_text=Steganography.decode(output_path)

        #If image contains no message
        if len(hidden_text)==0:
            print colored("NO MESSAGE FOUND","red")
        else:
            splited=hidden_text.split()

            #identifying special keywords
            for x in splited:
                if x=="SOS" or x=="CREATE" or x=="DELETE":
                    print colored("SPECIAL CODE WORD IS IDENTIFIED %s",'green')%(x)

            #Maintaining the average number of words spoken by a spy everytime you receive a message from a particular spy.
            average=len(splited)
            print colored("THE AVERAGE NUMBER OF WORDS BY YOUR SPY FRIEND IS %d","yellow")%(average)

            #storing secret message to chats list
            new_chat=chat_Message(hidden_text,datetime.now(),False)
            friend[m_recieve].chats.append(new_chat)
            print colored("YOUR MESSAGE IS SAVED SUCCESSFULLY",'green')

            #deleting friend from SPY friends if he/she speaks a lot
            if len(splited) > 100:
                print"YOUR FRIEND %s SPEAKS A LOT" % (friend[m_recieve].name)
                name=friend[m_recieve].name
                friend.pop(m_recieve)
                print colored("%s IS NOT YOUR FRIEND ANYMORE..",'cyan')%(name)



#Function to read chat history
def read_chat():
    read = select_friend()
    if friend[read].chats==[]:
        print "NO CHAT HISTORY"
    else:
        for chat in friend[read].chats:

            #Printing chats in desired colors
            if chat.sent_by_me==True:
                print('\033[1;34;0m %s \033[1;31;0m%s: \033[1;30;49m%s ')%(chat.time.strftime("%B %d, %Y [%X]"), 'YOU SAID:',chat.message)
            else:
                print('\033[1;34;0m %s \033[1;31;0m %s SAID: \033[1;30;49m%s')%(chat.time.strftime("%B %d, %Y [%X]"), friend[read].name.upper(),chat.message)



#Function to add status
def add_status(current_status):
    if current_status==None:
        print  colored("\nYOU HAVE NO STATUS YET",'blue')
    else:
        print colored("\nYOUR CURRENT STATUS IS %s",'blue')%(current_status)
    status=int(raw_input("\n WHAT YOU WANT TO DO? \n1.PRESS 1 TO ADD A NEW STATUS \n2.PRESS 2 TO UPDATE AN OLD STATUS"))

    #adding new status
    if status==1:
        new_status=raw_input("\nENTER YOUR STATUS")
        if len(new_status)==0:
            print colored("\nINVALID STATUS",'red')
        else:
            status_list.append(new_status)
            print colored("\n\nYOUR STATUS IS SUCCESFULLY UPDATED...",'green')
            return new_status

    #selecting old status
    elif status==2:
        if status_list==[]:
            print colored("\nYOU HAVE TO FIRST ADD SOME STATUS","yellow")
        else:
            position=1
            for i in status_list:
                print colored("%d. %s",'blue')%(position,i)
                position=position+1
            status_choice=int(raw_input("\n\nENTER YOU CHOICE"))
            current_status=status_list[status_choice-1]
            print colored("\nYOUR STATUS IS SUCCESFULLY UPDATED...","green")
            return current_status
    else:
        print colored("\nWRONG CHOICE","red")



#Function to provide multiple choices to SPY
def spy_choice(name,age,rate):
    current_status = None
    choice=1
    while choice != 6:
        choice = int(raw_input("\nWHAT YOU WANT TO DO???? \n1.UPDATE A STATUS \n2.ADD A FRIEND \n3.SEND A SECRET MESSAGE \n4.READ A SECRET MESSAGE \n5.READ CHATS FROM USER \n6.CLOSE APPLICATION"))
        if choice==1:
            current_status=add_status(current_status)
        elif choice==2:
            x=add_friend(spy.rate)
        elif choice==3:
            send_a_message()
        elif choice==4:
            read_a_message()
        elif choice==5:
            read_chat()
        elif choice==6:
            exit(colored("HAVE A NICE DAY ...BYE","red"))
        else:
           print colored("WRONG INPUT","red")
