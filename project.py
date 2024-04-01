import re
contact = { 1234567890 : {"Name" : "Haya Mubaidin", "Phone Number" : 1234567890,\
"Email" : "h.mubaidin@valorant.com",  "Address" : "Amman, Jordan", "Additional Info" : "Valorant Pro Player"}}   

def cli(): # Command Line Interface
    while True:
            user_input = input("""
            Welcome to the Contact Management System!

            Menu:
            1. Add a new contact
            2. Edit an existing contact
            3. Delete a contact
            4. Search for a contact
            5. Display all contacts
            6. Export contacts to a text file
            7. Import contacts from a text file
            8. Quit
                            
            """)

        
            if int(user_input) == 1: # 1. Add a contact
                add_contact()
            elif int(user_input) == 2: # 2. Edit a contact
                edit_contact()
            elif int(user_input) == 3: # 3. Delete a contact
                delete_contact()
            elif int(user_input) == 4: # 4. Search for a contact
                search_contact()
            elif int(user_input) == 5: # 5. Display all contacts
                display_contact()
            elif int(user_input) == 6: # 6. Export contacts to a text file
                export_contact()
            elif int(user_input) == 7: # 7. Import contacts from a text file
                import_contacts()
            elif int(user_input) == 8: # 7. Quit
                break
            else: # Error Handling when the user inputs an invalid number
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")


def add_contact():
        try:
            while True:
                name = input("\nWhat is the name of the contact you would like to add? (Back)\n ") # Adding the name of the contact
                if name.lower() == "back": # Back to the main menu
                    break # back to the cli function (main menu)
                phone_number = input(f"\nWhat's {name}'s phone number?\n ") # Adding phone number of the contact
                phone_number = re.sub(r"\D", "", phone_number) 
                phone_number = re.search(r"\b\d{10}\b" , phone_number).group() # Validating the phone number
                if phone_number == None :
                    print("\n\n\nInvalid phone number.. Try again! ༼ つ ◕_◕ ༽つ")
                    continue
                email = input(f"\nWhat's {name}'s email?\n ") # Adding email of the contact
                email = re.search(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z._-]{2,}" , email).group()
                if email == None:
                    print("\n\n\nInvalid email.. Try again! ༼ つ ◕_◕ ༽つ")
                    continue
                address = input(f"\nWhat's {name} address?\n ") # Adding address of the contact
                additional_info = input(f"\nAny additional info about {name}?\n ") # Adding additional info of the contact
                contact.update({phone_number: {"Name" : name, "Phone Number" : phone_number,\
                "Email" : email, "Address" : address, "Additional Info" : additional_info}}) # Adding the contact to the dictionary
                print(f"\n{name} has been added to your contacts! 📞✨/n")
        except (AttributeError, ValueError): # Error Handling when the user inputs an invalid number
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
         
# add_contact()

def edit_contact():
    while True:
        try:
            x = False
            phone_number = input("\nWhat is the phone number of the contact you would like to edit? (Back)\n ") # Editing the contact
            if phone_number.lower() == "back": # Back to the main menu
                break # back to the cli function (main menu)
            phone_number = re.sub(r"\D", "", phone_number) 
            phone_number = re.search(r"\b\d{10}\b" , phone_number).group() # Validating the phone number
            phone_number = int(phone_number) # Converting the phone number to an integer
            if phone_number == None :
                print("\n\n\nInvalid phone number.. Try again! ༼ つ ◕_◕ ༽つ")
                continue                        
            contact[phone_number]
        except (AttributeError, KeyError): # Error Handling when the user inputs an invalid number
            print(f"\n\n\n{phone_number} Does not exist in your contacts! 📞✨\n")
            for key, value in contact.items(): # Looping through the dictionary
                try:
                    if phone_number == key: # If the phone number is found in the dictionary
                        print(f"\nWhat would you like to edit about {value['Name']}? (Back)\n") # Editing the contact
                        edit_input = input("""
                        1. Name
                        2. Phone Number
                        3. Email
                        4. Address
                        5. Additional Info
                        6. Back To Menu
                        """)
                        if edit_input.lower() == "back": # Back to first input
                            break
                        elif int(edit_input) == 1: # Editing the name of the contact
                            new_name = input(f"\nWhat is the new name of {value['Name']}?\n ") # input the new name
                            print(f"\n{value['Name']} has been updated to {new_name}! 📞✨\n") # Updating the name
                            contact[phone_number]["Name"] = new_name
                        elif int(edit_input) == 2: # Editing the phone number of the contact
                            new_number = int(input(f"\nWhat is the new phone number of {value['Name']}?\n "))  # input the new phone number
                            new_number = re.sub(r"\D", "", phone_number) 
                            new_number = re.search(r"\b\d{10}\b" , new_number).group() # Validating the phone number
                            if new_number == None :
                                print("\n\n\nInvalid phone number.. Try again! ༼ つ ◕_◕ ༽つ")
                                continue                        
                            contact[phone_number]["Phone Number"] = new_number 
                            x = True 
                            print(f"\n{value['Phone Number']} has been updated to {new_number}! 📞✨\n")  # Updating the phone number
                        elif int(edit_input) == 3: # Editing the email of the contact
                            new_email = input(f"\nWhat is the new email of {value['Name']}?\n ") # input the new email
                            new_email = re.search(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z._-]{2,}" , new_email).group()
                            if new_email == None:
                                print("\n\n\nInvalid email.. Try again! ༼ つ ◕_◕ ༽つ")
                                continue
                            contact[phone_number]["Email"] = new_email
                            print(f"\n{value['Email']} has been updated to {new_email}! 📞✨\n") # Updating the email
                        elif int(edit_input) == 4: # Editing the address of the contact
                            new_address = input(f"\nWhat is the new address of {value['Name']}?\n ") # input the new address
                            contact[phone_number]["Address"] = new_address
                            print(f"\n{value['Address']} has been updated to {new_address}! 📞✨\n") # Updating the address
                        elif int(edit_input) == 5: # Editing the additional info of the contact
                            new_info = input(f"\nWhat is the new additional info of {value['Name']}?\n ") # input the new additional info
                            contact[phone_number]["Additional Info"] = new_info 
                            print(f"\n{value['Additional Info']} has been updated to {new_info}! 📞✨\n") # Updating the Additional Info
                        elif int(edit_input) == 6: # Back to the main menu 
                            cli()
                        else: # Error Handling when the user inputs an invalid number
                            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
                except (AttributeError, ValueError): # Error Handling when the user inputs an invalid number
                    print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
            if x == True: # If the phone number is found in the dictionary
                contact[new_number] = contact [phone_number] # Updating the phone number  
                del contact[phone_number] # Deleting the old phone number

# edit_contact()            
    
def delete_contact(): # Deleting a contact
    while True: # Looping through the dictionary
        try: 
            phone_number = input("\nWhat is the phone number you would like to delete? (Back)\n ") # input the phone number to delete
            if phone_number.lower() == "back": # Back to the main menu
                break
            else:
                del contact[int(phone_number)] # Deleting the contact
                print(f"\n{phone_number} has been deleted from your contacts! 📞✨\n") 
        except (ValueError, KeyError): # Error Handling when the user inputs an invalid number
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
            
# delete_contact()

def search_contact():
    while True:
        try:
            contacts = input("\nWhat is the phone number you would like to search? (Back)\n")
            if contacts.lower() == "back":
                break
            contacts = re.sub(r"\D", "", contacts) 
            contacts = re.search(r"\b\d{10}\b" , contacts).group() # Validating the phone number
            contacts = int(contacts) # Converting the phone number to an integer
            if contacts == None:
                print("\n\n\nInvalid phone number.. Try again! ༼ つ ◕_◕ ༽つ")
                continue                        
            contact[contacts]
        except (AttributeError, KeyError): # Error Handling when the user inputs an invalid number
            print(f"\n\n{contacts} Does not exist in your contacts! 📞✨\n")            
            for key, value in contact.items():
                try:
                    if int(contacts) == key:
                        print(f"\nContact📞✨\n \nName: {value['Name']}\nPhone Number: {value['Phone Number']}\
                        \nEmail: {value['Email']}\nAddress: {value['Address']}\nAdditional Info: {value['Additional Info']}\n")
                except (AttributeError, ValueError): # Error Handling when the user inputs an invalid number
                    print(".. Try again! ༼ つ ◕_◕ ༽つ")

# search_contact()

def display_contact():
    print("\nHere are all your contacts: 📞✨")
    contacts_list = list(contact.items())
    for index, (key, value) in enumerate(contacts_list, start=1):
        print(f"{index}. {value['Name']}: {key}")
    while True:
        try:
            choice = input("\nEnter the number of the contact you would like to view: (Back)\n")
            if choice.lower() == "back":
                break # back to the cli function (main menu)
            if 1 <= int(choice) <= len(contacts_list): # Displaying the contact as 1
                key, value = contacts_list[int(choice) - 1] # Reading the contact as 0
                print("\t\tContact 📞✨")
                print(f"\tName: {value['Name']}")
                print(f"\tPhone Number: {key}")
                print(f"\tEmail: {value['Email']}")
                print(f"\tAddress: {value['Address']}")
                print(f"\tAdditional Info: {value['Additional Info']}")
                user_input = input("\nWould you like to view another contact? (Yes/No)\n")
                if user_input.lower() == "no" or user_input.lower() == "n":
                    break # back to the cli function (main menu)
                elif user_input.lower() == "yes" or user_input.lower() == "y": 
                    continue # back to the display_contact function
            else:
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except (ValueError, IndexError): # Error Handling when the user inputs an invalid number
            print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")

# display_contact()
            
def export_contact(): # Exporting contacts to a text file
    try:
        with open ("contacts_files/default_contacts.txt", "w") as file: # Writing to the file
            for key in contact.keys():
                file.write(f"{[key]} : {contact[key]}\n")
            print("\nYour contacts have been exported to contacts_default.txt!\n")
        with open("contacts_files/contacts.txt", "w") as file:
            y = 0 
            for key, value in contact.items():
                file.write(f"\nContact {y+1}:\nName: {value['Name']}\nPhone Number: {key}\nEmail: {value['Email']}\nAddress: {value['Address']}\nAdditional Info: {value['Additional Info']}\n")
                y += 1
            print("and also exported to contacts.txt! 📞✨\n")
    except (PermissionError, IOError):  # Error Handling when the user inputs an invalid number
        print("You don't have permission to write to this file.")

# export_contact()
        
def import_contacts(): # Importing contacts from a text file
    try:
        with open("contacts_files/default_contacts.txt", "r") as file: # Reading from the file
            for line in file:
                print(line)
            print("\nYour contacts have been exported to contacts_default.txt!📞✨\n")
    except (PermissionError, IOError): # Error Handling when the user inputs an invalid number
        print("You don't have permission to read from this file.")

# import_contacts()

cli()
