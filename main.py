import nora

def main():
    #Service Token
    token = "token"
    #Service JSessionID
    jsessionid = "jsessionid"
    #Service StreamName
    streamname = "streamname"
    #Customer Test
    customerID =  "id"
    #Set the date to receive the credit 
    data= "2022-08-06T18:58"
    data = data[:-6]
    daysToGive = 1

    r = 99
    while r != 0:
        print("Choose an option: ")
        print("0 to exit")
        print("1 to add time to a customer")
        print("2 to duplicate a customer")
        print("3 to export to Json")
        print("4 to delete one customer")
        print("5 Nuke This Shit")

        r = int(input())
        if r == 3:
            print("Copying...")
            nora.noraJsonExport(token, jsessionid, streamname, data, daysToGive)
            print("Exporting Complete")
        elif r == 2:
            print("Type Customer ID")
            customerID = int(input())
            nora.duplicate(streamname, token, jsessionid, customerID)
        elif r == 1:
            print("Type How Many Days To Give")
            daysToGive = int(input())
            nora.noracheck(token, jsessionid, streamname, data, daysToGive)
        elif r == 4:
            print("Type Customer ID to delete")
            customerID = int(input())
            nora.delete_customer(streamname, token, jsessionid, customerID)
        elif r == 5:
            print("Are you sure you want to Nuke this shit? y/n")
            r = input()
            if r == "y":
                print("Once you nuke this, there is no going back. Are you sure? y/n")
                r = input()
                if r == "y":
                    print("Nuking This Shit")
                    nora.NukeThisShit(streamname, token, jsessionid)
                    print("Enjoy the devastation =)")

            if r == "n":
                print("Thanks for not nuk")
                exit()
        elif r == 0:
            print("Exiting...")
            exit()

        
if __name__ == "__main__":
    main()
