# **The Contact Management System**

*The Contact Management System is a software tool designed to help users organize and manage their contacts effectively. The purpose of a Contact Management System is to provide individuals or organizations with a centralized and organized way to store, manage, and access contact information.*

## User interaction

**Menu Preview (Command-Line):**  
*Users start by choosing the function they wish to use, by entering the number associated with the option.*
```
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
```
<br />
<br />

**1. Add a new contact:** *Users can add new contacts to the system by providing details such as name, phone number, email address, etc., once a user adds a contact to the (Add a new contact) function, it will redirect them to add another contact, and will be displayed as such:*

```
What is the name of the contact you would like to add? (Back)
 Haya

What's Haya's phone number?
 1234567890

What's Haya's email?
 Haya@github.com

What's Haya address?
 101 github

Any additional info about Haya?
 Test

Haya has been added to your contacts! 📞✨/n

What is the name of the contact you would like to add? (Back)
```
*When a user is done adding contacts and wishes to go back to the menu, they can achieve that by typing in 'back', as seen below:*

```
What is the name of the contact you would like to add? (Back)
back

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
```
<br />
<br />

**2. Edit an exisiting contact:** *This function is where users can edit existing contacts that can be modified or updated with new information as needed. By typing in the phone number then by selecting the number of one of the options they would like to edit, as seen below:* 

```
What is the phone number of the contact you would like to edit? (Back)
 1234567890

What would you like to edit about Haya? (Back)


    1. Name
    2. Phone Number
    3. Email
    4. Address
    5. Additional Info
    6. Back To Menu
```
*If a user typed in a different contact other than the one they wanted to edit, the user can type 'back' to enter in a different phone number, as seen below*

```
What is the phone number of the contact you would like to edit? (Back)
 1234567890

What would you like to edit about Haya? (Back)


    1. Name
    2. Phone Number
    3. Email
    4. Address
    5. Additional Info
    6. Back To Menu
    back

What is the phone number of the contact you would like to edit? (Back)
```

*When a user is done editing their contacts and wishes to go back to the menu, they can achieve that by typing in '6', as seen below:*
```
What would you like to edit about Haya? (Back)


    1. Name
    2. Phone Number
    3. Email
    4. Address
    5. Additional Info
    6. Back To Menu
    6

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
```
<br />
<br />

**3. Delete a contact:** *If a user wants to delete a contact for any reason, they achieve that in this function. Once they decide on the contact they wish to delete, they can simply type in the number of the contact, as seen below:*
```
What is the phone number you would like to delete? (Back)
 1234567890

1234567890 has been deleted from your contacts! 📞✨


What is the phone number you would like to delete? (Back)
```
*When a user is done deleting their contact and wishes to go back to the menu, they can achieve that by typing in 'back', as seen below:*
```
What is the phone number you would like to delete? (Back)
 back

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
```

<br />
<br />

**4. Search for a contact:** *This function allows users to search for a specific contact by using their phone number, the system will then display the contact information matching the phone number, as seen below:*
```
What is the phone number you would like to search? (Back)
1234567890

Contact📞✨

Name: Haya
Phone Number: 1234567890
Email: Haya@github.com
Address: 101 github
Additional Info: Test


What is the phone number you would like to search? (Back)
```
*When a user is done searching for contacts they can simply type in 'back' to be redirected to the main menu, as seen below:*
```
What is the phone number you would like to search? (Back)
back

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
```
<br />
<br />

**5. Display all contacts:** *Users can view a list of all contacts stored in the system, providing an overview of their contact list. The (Display all contacts) function is displays all contacts and users can pick the number of the contact they wish to view in a more detailed format, as seen below:*
```
Here are all your contacts: 📞✨
1. Haya: 1234567890

Enter the number of the contact you would like to view: (Back)
1
            Contact 📞✨
    Name: Haya
    Phone Number: 1234567890
    Email: Haya@github.com
    Address: 101 github
    Additional Info: Test

Would you like to view another contact? (Yes/No)
```

*If a user would like to view another contact in detail they can simply type in 'yes' and type in a number from the list provided before or if a user is done viewing contacts they can type in 'no' to go back to the main menu, as seen below:*

```
Would you like to view another contact? (Yes/No)
no

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
```
<br />
<br />

**6. Export contacts to a text file:** *This function enables the user to export all contacts from the system into a text file. This text file can then be saved and shared or used for backup purposes, the **(contacts_default.txt)** is in python format and can be used for importing purposes, the **(contacts.txt)** is for the user and is written in a more readable format. Once the contacts have been exported the user will be redirected to the main menu, as seen below:* 
```
Your contacts have been exported to contacts_default.txt!

and also exported to contacts.txt! 📞✨


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
```
<br />
<br />

**7. Import contacts from a text file:** *This function enables the user to import any contacts from a text file into the contact management system. This is useful for users who may have contacts stored in another format or who want to transfer contacts between systems. Once the contacts have been imported the user will be redirected to the main menu, as seen below:* 
```
Your contacts have been imported to contacts_default.txt! 📞✨


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
```
<br />
<br />

**8. Quit:** *When a user is done using the application and wishes to quit, they can achieve that by entering the number '8' in the menu screen, as seen below:* 
```
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

    8
    
>>
```

## Invalid Input

**Error Messages:** *If a user attempts to input or execute something that is not within the system's capabilities or requirements, the system would generate an error message for the user, as seen below:*
```
Invalid Input.. Try again! ༼ つ ◕_◕ ༽つ
```
**Possible Causes:** *The error message shown above could occur due to various reasons, such as entering, deleting, searching for a non-existent contact, creating a contact with no input, selecting an invalid option, encountering a technical glitch, etc.*

**Resolution:** *To resolve the issue, the user would need to review their input, ensure that it meets the system's capabilities, and correct any mistakes they may have inputted.*

## Authors

**This application was a group effort created by:**     

*Haya Mubaidin* https://github.com/Hiyuhh    
*Adam Cifelli* https://github.com/AdamC13    
