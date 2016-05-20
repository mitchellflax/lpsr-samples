# a simple program for storing contacts
# author: mflax@leadps.org

print("Welcome to Contacts!")

# create a control variable
# set it to something non-zero
choice = 1

# create an empty dictionary
myContacts = {}

while choice != 0:

    print("What would you like to do?")
    print("(1) Add a phone number.")
    print("(2) Print the full list of contacts.")
    print("(3) Enter a name to retrieve that contact's phone number.")
    print("(0) Exit the Contacts app.")

    choice = int(raw_input())

    if choice == 1:

        print("What's the name of your contact?")
        name = raw_input()
        print("What's the phone number of your contact?")
        number = raw_input()

        myContacts[name] = number

    if choice == 2: 

        print(myContacts)

    if choice == 3:

        print("Whose number would you like?")
        name = raw_input()
        print("OK, here's the number: ")
        print(myContacts[name])
