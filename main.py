import webbrowser
import os



print("**********WELCOME TO LIBRARY MANAGEMENT SYSTEM**********")



#Signup Page
print("SignUP")

user_name=input("Enter Your Username: ")
password=input("Enter Password: ")

os.system("cls")

if(user_name and password):
    print("You have successfully signed up")
    
    print("Login")

    user=input("Enter Username: ")
    pass1=input("Enter Password: ")


    if(user == user_name and pass1 == password):
        print("Login Successful")
        os.system("cls")
        books={} #Dictionary to store book_names


        try:

            with open("books.txt","r") as file:

                for line in file:
                    if "|" in line:
                        name,link=line.strip().split("|")
                        books[name.strip().lower()]=link.strip()
            if not books:
                print("No book found")
            else:
                print("Available books: ")
                
                for name in books:
                    print(name.title())
  

                choice=input("Enter the name of book: ").strip().lower()
                if choice in books:
                    print(f"opening {choice}")
                    webbrowser.open(books[choice])
                else:
                    print("Book not found")
            

        except FileNotFoundError:
            print("No book available.'books.txt' not found.")

        
    else:
        print("Invalid username or password")
    





