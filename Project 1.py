import re
check=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
print("Please select one of the following:\n1. Register\n2. Login\n3. Forgot Password")
fin=input()
if fin=="1":
    print("Please enter an E-mail ID:")
    nemail=input()
    if re.fullmatch(check,nemail):
        print("Valid E-mail")
        print("Enter Password:")
        npass=input()
        l,u,s,d=0,0,0,0
        upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower="abcdefghijklmnopqrstuvwxyz"
        digits="0123456789"
        schar="$@_!?()[]<>.,;:"
        if len(npass)>5 and len(npass)<16:
            for i in npass:
                if i in upper:
                    u+=1
                if i in lower:
                    l+=1
                if i in digits:
                    d+=1
                if i in schar:
                    s+=1
            if u>=1 and l>=1 and d>=1 and s>=1 and l+u+d+s==len(npass):
                print("Valid Password\nEnter password again:")
                npass1=input()
                if npass1==npass:
                    print("Successfully registered")
                    file=open("Email.txt","a")
                    file.write(nemail+" "+npass+" ")
                    file.close()
                else:
                    print("Password does not match")
            else:
                print("Invalid Password\nPassword must contain atleast one Capital letter, one Lowercase letter, one Number and one Special Character")
        else:
            print("Password length must be between 5-16 characters")
    else:
        print("Invalid ID")
if fin=="2":
    print("Enter your E-mail ID:")
    lemail=input()
    file=open("Email.txt","r")
    info=file.read()
    info=info.split()
    if lemail in info:
        print("Enter Password:")
        lpass=input()
        index=info.index(lemail)+1
        upass=info[index]
        if lpass==upass:
            print("You have logged in")
            file.close()
        else:
            print("Password does not match E-mail ID")
    else:
        print("E-mail ID does not exist. Please register first")
if fin=="3":
    print("Please enter your E-mail ID:")
    femail=input()
    file=open("Email.txt","r")
    info=file.read()
    info=info.split()
    if femail in info:
        print("Would you like to:\n1. Retrieve your password\n2. Create a new password")
        fchoice=input()
        if fchoice=="1":
            index=info.index(femail)+1
            upass=info[index]
            print("Your password is:\n"+upass)
            file.close()
        elif fchoice=="2":
            print("Enter your new password:")
            fpass=input()
            l,u,s,d=0,0,0,0
            upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lower="abcdefghijklmnopqrstuvwxyz"
            digits="0123456789"
            schar="$@_!?()[]<>.,;:"
            if len(fpass)>5 and len(fpass)<16:
                for i in fpass:
                    if i in upper:
                        u+=1
                    if i in lower:
                        l+=1
                    if i in digits:
                        d+=1
                    if i in schar:
                        s+=1
                if u>=1 and l>=1 and d>=1 and s>=1 and l+u+d+s==len(fpass):
                    print("Valid Password\nEnter Password again:")
                    fpass1=input()
                    if fpass1==fpass:
                        index=info.index(femail)+1
                        info[index]=fpass
                        file.close()
                        print("Password has been updated")
                    else:
                        print("Password does not match")
                        file.close()
                else:
                    print("Invalid Password\nPassword must contain atleast one Capital letter, one Lowercase letter, one Number and one Special Character")
            else:
                print("Password length must be between 5-16 characters")
        else:
            print("Invalid choice")
    else:
        print("E-mail ID does not exist\nPlease verify your E-mail ID")