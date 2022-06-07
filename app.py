
from helpers.welcome import welcome
from helpers.querySelector import *

welcome()

print("Enter Alias")
alias = input("Alias: ")

print("Enter Password")
password = input("Password: ")


# Function to login - must be done by query SELECT
def login():
    if run_query(statement="SELECT alias, password FROM hackers WHERE alias=? and password = ?", args=(alias, password)):
        run_query("SELECT alias, password, id FROM hackers WHERE alias=? and password = ?", [alias, password])
        
    else:
        exit()
    
login()
id = run_query("SELECT id FROM hackers WHERE alias=? and password = ?", [alias, password])
print(id)
alias = int(''.join(map(str, id[0])))

# Post log-in Present 4 options, enter a new exploit, see all exploits, see all other exploits by everyone except for the logged in user, exit application(loop)

print("To create a new Exploit: " + "Enter 1")
print("To view all Exploits: " + "Enter 2")
print("To view all Exploits by other Hackers: " + "Enter 3")
print("To Exit Select: " + "Enter 4")

while True: 
    selection = input("Select here: ")
    # Function to create a new exploit
    if selection == "1":
        content = input("Enter new Exploit here: ")
        def createExploit():
            alias_id = alias
            print(alias_id)
            new_exploit = run_query("INSERT INTO exploits (alias_id, content) VALUE (?,?)", [alias_id, content])
            print(new_exploit)
        createExploit()
    
    #Function to View all exploits, including the user
    elif selection == "2":
        def viewAllExploits():
            
            viewAllExploits = run_query("SELECT  content, alias_id from exploits")
            print(viewAllExploits)
        viewAllExploits()
        
    #Function to View only exploits made by other users
    elif selection == "3":
        def viewOtherUsersExploits():
            alias_id = alias
            print(alias_id)
            otherUsersExploits = run_query("SELECT content, alias_id from exploits  WHERE not alias_id=?", [alias_id])
            print(otherUsersExploits)
        viewOtherUsersExploits()
    elif selection == "4":
        exit()