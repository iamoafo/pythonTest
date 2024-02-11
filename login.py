
# def read():
#     with open("Book2.csv", "r") as f:
#             for line in f:
#                 user_data = line.split()
import csv

def read():
    try:
        data=[]
        with open('Book2.csv', 'r') as f:
                for row in csv.reader(f):
                    data.append(row)
                return data
            
                
    except IOError as e:
        print("There is a problem with the subject CSV file" ,e)


loginData = read()

# print(loginData)



# def login():
     
inputNum = int(input("Please enter 1 if you have login details and 2 to sign up\n"))
if inputNum == 1:

    username = input("Please enter your username\n")
    pword = input("Please enter your password\n")

    for x in loginData:
        if username == x[0].lower():
            if pword == x[2].lower():
                    print("sucessful")

            else:
                    print("unsucessful")

elif inputNum ==2:
 x=0
while x==0:
    print ("Please sign up")

    sUsername = input("Please enter username to sign up\n")

    sPword = input("Please enter password to sign up\n")
    
    for n in loginData:
        if sUsername == n[0]:
            x=0
            print("Username exists, please try again")
            break
        elif "".__eq__(sUsername):
             x=0
             print("Username cannot be empty.Please try again") 
             break
        elif "".__eq__(sPword):
             x=0
             print("Password cannot be empty.Please try again") 
             break
        else:
                x=1
                    
with open("Book2.csv", "a",newline='') as file:
 f=csv.writer(file)
 f.writerow([sUsername,'',sPword])
# f.close()

print("You have successfully signed up!")
                

        #   update_to_spreadsheet =  SHEET.worksheet(user_info)
        #         update_to_spreadsheet.append_row(new_username)
        #         print('worksheet has updated successfully') 

    


# login()

