import sqlite3
import re

"""A program that allows a user to perform CRUD operations on a database using the CLI"""

class CMS:
    

    """
    Creating the database
    """
    # Creating the database if it does not exist
    def create_database():

        # Creating a connection to the database
        con = sqlite3.connect('contacts.db')
        # Creating a cursor object
        cur = con.cursor()

        print('\nCreating the database...\n')
        cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
                        first_name TEXT,
                        last_name TEXT,
                        phone_number TEXT,
                        email TEXT
                )""")

        #Creating a list to insert many contacts in the contacts table
        many_contacts = [('Miles', 'Davis', '07780090011', 'Mile@Davis.com'),
                        ('Nina','Simone','07740050011','Nina@Simone.com'),
                        ('Cat','Stevens','07730050011','Cat@Stevens.com'),
                        ('Carol','King','07745525511','Carol@King.com'),
                        ('Smokey','Robinson','07710010011','Smokey@TheTemps.com'),
                        ('Ottis','Redding','07790010011','Ottis@thedockofthebay.com'),
                        ('Lauryn','Hill','07733322211','Lauryn@Hill.com'),
                        ('Stevie','Nicks','07760060011','Stevie@Nicks.com'),
                        ('Harry','Nilson','07711122211','Harry@Nilson.com'),
                        ('Peter','Gabriel','07700010011', 'Peter@SledgeHammers.com'),
                        ('Debbie','Harry','07707755511','Deborah@VideoDrome.com'),
                        ('Karen', 'Carpenter','07711111122', 'Karen@Carpenter.com'),
                        ('Andre', '3000', '07730001111', 'Andre3000@OutKast.com'),
                        ('Jeff', 'Buckley','07789982211', 'Jeff@lastGoodbye.com'),
                        ('Kim', 'Deal', '07700100211', 'Kim@cannonballs.com'),
                        ('Kim', 'Gordan', '07710113455', 'Gordan@coolthings.com'),
                        ('Damon', 'Albarn', '07723328911', 'Damon@DareDayz.com')]

        cur.executemany("""INSERT INTO contacts VALUES (?,?,?,?)""", many_contacts)
        con.commit()



    """
    fetching a list of contacts from the database table contacts
    """
    def fetching_data_from_database():
        print('\nfetching contacts...\n')
        con = sqlite3.connect('contacts.db')
        cur = con.cursor()

        #Select all data from database and ordering it alabetically
        cur.execute("SELECT * FROM contacts ORDER BY first_name ASC")
        contacts = cur.fetchall()

        #Printing out a row of contacts
        for contact in contacts:
            print(contact) 



    """
    A fuction that lets the user search for a contact by name, phone number or email
    """
    def search_contact():
        con = sqlite3.connect('contacts.db')
        cur = con.cursor()

        search_options = """\nChoose a search by option
        
1) Search by first name
2) Search by last name
3) Search by phone number
4) Search by email address
5) Go back
                        \n"""        
        
        # A while loop that returns user options, unless 5 is pressed
        while (input_option:= input(search_options)) != "5":
            if input_option == "1":
                first_name = input("\nEnter persons first name: ")
                cur.execute("SELECT * FROM contacts WHERE first_name LIKE '{}%'".format(first_name).title()) # formatting input to string and capitalizing names
                print(cur.fetchall())
            elif input_option == "2":
                last_name = input("\nEnter the persons last name: ")
                cur.execute("SELECT * FROM contacts WHERE last_name LIKE '{}%'".format(last_name).title())
                print(cur.fetchall())
            elif input_option == "3":
                phone_number = input("\nEnter the phone number you want to search: ")
                cur.execute("SELECT * FROM contacts WHERE phone_number LIKE '%{}%'".format(phone_number))
                print(cur.fetchall())
            elif input_option == "4":
                email = input("\nEnter the email address you want to search: ")
                cur.execute("SELECT * FROM contacts WHERE email LIKE '%{}%'".format(email))
                print(cur.fetchall())
            else:
                print("\nInvalid option")

    """
    A function for validating phone numbers
    """
    def validate_phone_number(phone_number):
        reg_pattern = r'07\d{9,13}|447\d{7,12}' #regex for uk mobile numbers
        if re.match(reg_pattern, phone_number): # if the phone number matches the reg_pattern then return value
            return phone_number


    """
    A function for validating email addresses
    """        
    def validate_email(email):
        reg_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' # regex for valid emails
        if re.match(reg_pattern, email): # if the email matches the reg_pattern then return value
            return email

    """
    A function that adds a contact to the database
    """
    def add_a_contact():
        con = sqlite3.connect('contacts.db')
        cur = con.cursor()

        first_name = input("First Name: ").capitalize() # Capitalizing names entered into the cli
        last_name = input("Last name: ").capitalize()


        valid_phone_number = False # False flag
        while not valid_phone_number: # while not a valid phone number return to input
        
            phone_number = input("Phone number: ")
            if CMS.validate_phone_number(phone_number):
                print("Valid phone number")
                valid_phone_number = True
            else:
                print("Invalid phone number")


        valid_email = False
        while not valid_email:

            email = input("Enter an email: ")
            if CMS.validate_email(email):
                print("Valid email")
                valid_email = True
            else:
                print("Invalid email")


        #Converting the arguments entered into the cli to string format
        cur.execute("INSERT INTO contacts VALUES ('{}', '{}', '{}', '{}')".format(
                    first_name, last_name, phone_number, email))    

        con.commit()
        print('\nNew Contact added\n')



    """
    A function that updates cantacts in the databse
    """
    def update_contact():
        con = sqlite3.connect('contacts.db')
        cur = con.cursor()

        update_options = """
        
        Choose an update option
        _______________________

1) Update first name
2) Update last name
3) Update phone number
4) Update email address 
5) See contacts table
6) Go back

              \n"""
        
        #Creating the user input variables that will update the contacts table
        while (input_option:= input(update_options)) != "6":
            if input_option == "1":
                original_name = input("\nEnter the first name of the person whos name you want to change: ")
                new_name = input("\nEnter their new first name: ").title()
                cur.execute("UPDATE contacts SET first_name = '{}' WHERE first_name LIKE '{}%' ".format(new_name, original_name))
                con.commit()
            elif input_option == "2":
                original_last_name = input("\nEnter the last name of the person whos last name you want to change: ")
                new_last_name = input("\nEnter their new last name: ").title()
                cur.execute("UPDATE contacts SET last_name = '{}' WHERE first_name LIKE '{}%' ".format(new_last_name, original_last_name))
                con.commit()
            elif input_option == "3":
                original_number = input("\nEnter the first name of the person whos phone number you want to change: ")
                new_number = input("\nEnter their new phone number: ")
                cur.execute("UPDATE contacts SET phone_number = '{}' WHERE first_name LIKE '{}%' ".format(new_number, original_number))
                con.commit()
            elif input_option == "4":
                original_email = input("\nEnter the first name of the person whos you email want to change: ")
                new_email = input("\nEnter their new email address: ").capitalize()
                cur.execute("UPDATE contacts SET email = '{}' WHERE first_name LIKE '{}%' ".format(new_email, original_email))
                con.commit()
            elif input_option == "5":
                CMS.fetching_data_from_database()
            else:
                print("Invalid option")
            
        print('\nContact has been updated. \n')



    """
    A function that deletes contacts from the database
    """
    def delete_contact():
        con = sqlite3.connect('contacts.db')
        cur = con.cursor()


        first_name = input("Enter the first name of the contact you want to delete: ")
        last_name = input("Enter the last name of the person you want to delete: ")

        cur.execute("""SELECT * FROM contacts WHERE first_name LIKE '{}%' 
                    AND last_name LIKE '{}%' """. format(first_name, last_name).title())
        print('\n', cur.fetchall(), 'has been deleted')

        cur.execute("""DELETE FROM contacts WHERE first_name LIKE '{}%' 
                    AND last_name LIKE '{}%' """. format(first_name, last_name).title())
        con.commit()



    """
    A function that closes the connection to the database
    """
    def close_connection_to_database():
        print('\nclosing connection to contacts.db...\n')
        con = sqlite3.connect('contacts.db')
        con.close()


    """
    Creating a User prompt
    """
    user_prompt = """

    
---Contact Management System----
________________________________

Please choose one of these options:

1) To see all contacts
2) To search a contact
3) To add a contact
4) To update a contact
5) To delete a contact
6) To quit
            
                \n"""


if __name__ == '__main__':

    # CMS.create_database()

    while (user_input:= input(CMS.user_prompt)) != "6":
        if user_input == "1":
            CMS.fetching_data_from_database()
        elif user_input == "2":
            CMS.search_contact()
        elif user_input == "3":
            CMS.add_a_contact()
        elif user_input == "4":
            CMS.update_contact()
        elif user_input == "5":
            CMS.delete_contact()
        else:
            print("Invalid input")

    CMS.close_connection_to_database()
