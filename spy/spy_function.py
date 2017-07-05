from spy_detail import Spy,spy,chat_Message
from steganography.steganography import Steganography
from datetime import datetime

def spy_verification():
    spy.name=raw_input('\n\nENTER YOUR NAME...')
    #name verification
    spy.length= len(spy.name)
    if spy.length==0:
        exit("\n\nINVALID NAME")
    else:
        print "\n\nACCESS GARANTED "
#asking for the details
    print "\n\nENTER YOUR DETAILS..."
#asking for gender
    spy.gender =raw_input("\n\nENTER YOUR GENDER (MALE/FEMALE)...")
    spy.salutaion =raw_input("\n\nSHOULD I CALL YOU MR. OR MISS.")
    print "\nWELCOME " + spy.salutaion + spy.name
#asking for age
    spy.age =int(raw_input("\nENTER YOUR AGE"))
    if spy.age>12 and spy.age<50:
        print "\nVALID AGE"
    else:
        exit("\nINVALID AGE")
#asking for rating
    spy.rate = float(raw_input("\n\nENTER YOU RATING(OUT OF 5)"))
    if spy.rate >= 4.6 and spy.rate <= 5.0:
        print "\nYOU HAVE NO MATCH"
    elif spy.rate >= 3.5 and spy.rate <= 4.5:
        print "\nYOU ARE EXCELLENT"
    elif spy.rate >= 2.5 and spy.rate < 3.5:
        print "\nYOU ARE GOOD"
    else:
        print "\nYOU ARE NOT BAD"
    print "\n\nYOU WANT TO STAY ONLINE "
    spy_status=int(raw_input("\n1.PRESS 1 FOR YES \n2.PRESS 2 FOR NO"))
    if spy_status==1:
        spy.online=True
        print "\n\nSUMMARIZING YOUR DETAILS..."
        print "\n \n YOUR NAME IS %s. YOUR AGE IS %d. YOUR RATING IS %.2f. YOU ARE ONLINE."%(spy.name,spy.age,spy.rate)
    else:
        spy.online=False
        exit("\nBYE..... \n HAVE A GOOD DAY")



status_list=[]
friend=[]
spy.rate=float(spy.rate)
#addfriend
def add_friend(spy_rate):
    new_friend=Spy('','','',19,4.8)
    new_friend.name=raw_input("\nENTER YOUR NAME")
    new_friend.gender=raw_input("ENTER YOUR GENDER")
    new_friend.salutation=raw_input("SHOULD I CALL YOU MR OR MISS")
    new_friend.age=int(raw_input("ENTER YOUR AGE"))
    new_friend.rate=float(raw_input("ENTER YOUR RATING"))
    if len(new_friend.name)>0 and new_friend.age>12 and new_friend.age<50 and new_friend.rate>=spy.rate:
        friend.append(new_friend)
        print "\n%s IS SUCCESSFULLY ADDED TO YOUR FRIEND LIST"%(new_friend.name)
        print "\nCONGRATS NOW YOU HAVE %d FRIENDS"%(len(friend))
    else:
        print "\n\nSORRY DETAILS ARE NOT SUFFICIENT"
    return len(friend)

#select a friend
def select_friend():
    if friend==[]:
        print "\n\nYOU HAVE NO FRIENDS\nPLEASE ADD SOME"
    else:
        position=1
        print"\n YOUR FRIEND LIST IS...."
        for friends in friend:
            print "%d. %s aged %d having rating %.2f is online"%(position,friends.name,friends.age,friends.rate)
            position=position+1
        c=int(raw_input("SELECT ANY FRIEND"))
        if c<=position:
            return c-1
        else:
            print"WRONG INPUT"

#send a message
def send_a_message():
    m_sender=select_friend()
    if m_sender!=None:
        original_image=raw_input("PLEASE ENTER THE NAME OF THE IMAGE...")
        output_path=raw_input("ENTER THE OUTPUT PATH")
        text=raw_input("ENTER YOUR MESSAGE")
        Steganography.encode(original_image,output_path,text)
        new_chat=chat_Message(text,datetime.now(),True)
        friend[m_sender].chats.append(new_chat)
        print "\nYOUR SECRET MESSAGE IMAGE IS READY"



#read a message
def read_a_message():
    m_recieve=select_friend()
    if m_recieve != None:
        output_path=raw_input("\nPLEASE ENTER NAME OF THE IMAGE...\n")
        hidden_text=Steganography.decode(output_path)
        if len(hidden_text)==0:
            print "NO MESSAGE FOUND"
        else:
            splited=hidden_text.split()
            for x in splited:
                if x=="SOS" or x=="CREATE" or x=="DELETE":
                    print "SPECIAL CODE WORD IS IDENTIFIED %s"%(x)
            new_chat=chat_Message(hidden_text,datetime.now(),False)
            friend[m_recieve].chats.append(new_chat)
            print "YOUR MESSAGE IS SAVED SUCCESSFULLY"
            if len(splited) > 5:
                print"YOUR FRIEND %s SPEAKS A LOT" % (friend[m_recieve].name)
                name=friend[m_recieve].name
                friend.pop(m_recieve)
                print "%s IS NOT YOUR FRIEND ANYMORE.."%(name)
#read chat

def read_chat():

    read = select_friend()
    if friend[read].chats==[]:
        print "NO CHAT HISTORY"
    else:
        for chat in friend[read].chats:
            if chat.sent_by_me==True:
                print('\033[1;34;0m %s) \033[1;31;0m%s: \033[1;30;49m%s ')%(chat.time.strftime("%B %d, %Y [%X]"), 'You said:', chat.message)
            else:
                print('\033[1;34;0m %s) \033[1;31;0m %s said: \033[1;30;49m%s')%(chat.time.strftime("%B %d, %Y [%X]"), friend[read].name, chat.message)


#addstatus
def add_status(current_status):
    if current_status==None:
        print  "\nYOU HAVE NO STATUS YET"
    else:
        print ("\nYOUR CURRENT STATUS IS %s")%(current_status)
    status=int(raw_input("\n WHAT YOU WANT TO DO? \n1.PRESS 1 TO ADD A NEW STATUS \n2.PRESS 2 TO UPDATE AN OLD STATUS"))
    if status==1:
        new_status=raw_input("\nENTER YOUR STATUS")
        if len(new_status)==0:
            print "\nINVALID STATUS"
        else:
            status_list.append(new_status)
            print "\n\nYOUR STATUS IS SUCCESFULLY UPDATED..."
            return new_status
    elif status==2:
        if status_list==[]:
            print "\nYOU HAVE TO FIRST ADD SOME STATUS"
        else:
            position=1
            for i in status_list:
                print "%d. %s"%(position,i)
                position=position+1
            status_choice=int(raw_input("\n\nENTER YOU CHOICE"))
            current_status=status_list[status_choice-1]
            print "\nYOUR STATUS IS SUCCESFULLY UPDATED..."
            return current_status
    else:
        print "\nWRONG CHOICE"

#spychoice
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
        else:
            print "WRONG INPUT"
