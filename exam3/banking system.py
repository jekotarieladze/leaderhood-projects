
accounts = {}

def make_account():
    #ავიღოთ ინფორმაცია მომხმარებლისგან
    name = input("what's your name? ")
    phone = input("enter your phone number: ")
    balance = input("enter your balance: ")
    #შევამოწმოთ აქაუნთი უკვე შექმნილია თუა რა.
    if phone in accounts:
        print("this account already exist's try logging in instead.")
    else:
        #ვქმნით აქაუნთს
        accounts[phone] = {"username" : name , "balance" : float(balance)}
        print("account made successfully")


def perform_transaction():
    #მომხმარებელს შემოვატანინოთ მათი სასურველი ტრანზაქციის დეტალები როგორიცაა:
    phone, transaction, amount = input("enter your number, transaction type: withdraw or deposit and amount: ")
    amount = float(amount)
    #შევამოწმოთ თუ არსებობს ეს აქაუნთი

    if phone in accounts:
        if transaction == "deposit":
            accounts[phone] ["balance"] += amount
        elif transaction == "withdraw":
            if accounts[phone] ["balance"] >= amount:
                accounts[phone] [balance] -= amount
            else:
                print("insufficient funds")
                return
        else:
            print("wrong transaction type! ")
            return
        print(f"transaction completed successfully. new balance : {accounts[phone] [Balance]}")
    else:
        print("account not found")



def update_account():
    #უნდა ავიღოთ ახალი ინფორმაცია მომხმარებლისგან
    phone , new_user = input("enter phone number , new username: ").split()
    if phone in accounts:
        accounts[phone] ["name"] = new_user
        print("successfully updated account credentials")
    else:
        print("could not find account! ")

def delete_account():
    phone = input("enter phone number: ")
    
    if phone in accounts:
        del accounts[phone]
        print("account deleted successfully")
    else:
        print("something went wrong try again later")

def choise():
    print("DRAGON BANK")
    print("1: create an account")
    print("2: perform a transaction")
    print("3: update account info")
    print("4: delete account")
    print("5: search account info")
    print("view customers list")
    print("exit the system")

    choise = input("enter your command from 1 to 7: ")

    if choise == "1":
        make_account()

    elif choise == "2":
        perform_transaction()

    elif choise == "3":
        update_account()

    elif choise == "4":
        delete_account()

    else:
        print("try again later")

choise()