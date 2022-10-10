import os
import pickle
from termcolor import colored


## Create a dictionary to save contacts
contacts = {}
#################################################################################

class contact:
    def __init__(self, number, firstname, lastname, address):
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

##################### Save Contact ###############################################

def save_contact():
    ## For use pickle you should open file in Binary-Write Mode
    ## "Phonebook.dat" file will be create after first run this project
    with open("phonebook.dat", "bw") as  file_handler:
        ## Save Contact in Handler file by "Dump" Function
        pickle.dump(contacts, file_handler)

        ### Run this Function after every change ###

##################### Display Menu ###############################################

def display_menu():
    print(colored("Welcome to my phonebook", attrs=["bold"]))
    print("Total contact: {0}".format(len(contacts)))
    print("-----------------------------")
    print(colored("1. Add contact", "blue"))
    print(colored("2. Remove contact", "blue"))
    print(colored("3. Update contact", "blue"))
    print(colored("4. Find contact", "blue"))
    print(colored("5. List", "blue"))
    print(colored("6. Exit", "blue"))

##################### 1. Add Contact #################################################

def add_contact():
    os.system("cls")
    add_number = input("Enter phone number: ")
    if add_number in contacts:
        input(colored("The number is exist, Press enter to back menu ...", "red"))
    else:
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        address = input("Address: ")
        contacts[add_number] = contact(add_number, firstname, lastname, address)
        save_contact()

        print()
        input(colored("Contact created successfully, Press enter to back menu ...", "green"))

##################### 2. Remove Contact ###############################################

def remove_contact():
    os.system("cls")
    number = input("Number: ")
    if number in contacts:
        del contacts[number]
        save_contact()
        input(colored("The contact remove successfully, press enter to back menu ...", "green"))
    else:
        input(colored("The number does not exist in the list, press enter to back menu ...", "red"))

##################### 3. Update Contact ###############################################

def update_contact():
    os.system("cls")
    number = input("Number: ")
    if number in contacts:
        firstname = input("Firstname: ("+contact[number].firstname+"): ")  ## Save old content of contact
        lastname = input("Lastname: ("+contact[number].lastname+"):")
        address = input("Address: ("+contact[number].address+")")
        contacts[number].firstname = firstname
        contacts[number].lastname = lastname
        contacts[number].address = address
        save_contact()
        input(colored("The contact updated successfully, press enter to back menu ...", "green"))
    else:
        input(colored("The number does not exist in the list, press enter to back to menu ...", "red"))

##################### 4. Find Contact ################################################

def find_contact():
    os.system("cls")
    find = input("What contact you want to find: ")
    if find in contacts:
        contact = contacts[find]
        print("{0}, {1}, {2}, {3}".format(contact.number, contact.firstname, contact.lastname, contact.address))
        input(colored("Press enter to back main menu ...", "green"))
    else:
        print(colored("The number does not exist, press enter to back menu ...", "red"))

##################### 5. List Contact ################################################

def list_contact():
    os.system("cls")
    print(colored("Your Phonebook list is: ", "green"))
    print()
    for key in contacts:
        contact = contacts[key]
        print("{0}, {1}, {2}, {3}".format(contact.number, contact.firstname, contact.lastname, contact.address))
        print()
        input(colored("Press enter to back menu ...", "green"))

##################### If File exist ################################################

if os.path.exists("contact.dat"):
    with open("contact.dat", "r") as file_handler:
        contacts = pickle.load(file_handler)     ## Load by pickle

#####################################################################################

while True:
    ## First Clear the screen after that show the Menu
    os.system("cls")
    display_menu()
    print()
    user_input = input(colored("Please enter an option: ", "green", attrs=["bold"]))
    if user_input == "1":
        add_contact()
    if user_input == "2":
        remove_contact()
    if user_input == "3":
        update_contact()
    if user_input == "4":
        find_contact()
    if user_input == "5":
        list_contact()
    if user_input == "6":
        break
    else:
        print(colored("Wrong input", "red"))