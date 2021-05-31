import os
# os.getcwd()
import datetime
#Python Mini-Project->Library Management System Made by Roll no 91 and 92

class Library:
    def __init__(self,lib_data,lib_money):
        #init functions initializes files to program and makes a books dictionary by assigning book id to each book
        self.lib_data="lib_data.txt"
        self.lib_money="lib_money.txt"
        self.books_dict={}
        book_id=1
        with open(self.lib_data) as lb:
            all_lines=lb.readlines()
            for line in all_lines:
                l=line.split("~!!~")
                if l[1]=="A":
                    self.books_dict.update({str(book_id):{'b_name':l[0],'lend_name':l[2],'current_status':'Available','lend_date':l[3].replace("\n","")}})
                else:
                    self.books_dict.update({str(book_id):{'b_name':l[0],'lend_name':l[2],'current_status':'Un-Available','lend_date':l[3].replace("\n","")}})
                book_id+=1
    def display(self):
        #By accessing book id and book name and current status we display the books in tabular format
        print("Books Id","\t","Title")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get('b_name'), "-[",value.get('current_status'),"]")
    def add_book(self):
        #Adds the book name in both File as well as books dictionary
        book_tobe_added=input("Enter the book name to be added : ")
        with open(self.lib_data,"a") as lb:
            lb.writelines(f"{book_tobe_added}~!!~A~!!~-~!!~-\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'b_name':book_tobe_added,'lend_name':'-','current_status':'Available','lend_date':'-'}})
        print("Thank you for adding!! Data updated Successfully\n")
    def issue_book(self):
        #By taking book id we can assign book to customer and successfully update name and date in file and dictionary using datetime module
        issue_id=input("Enter book ID : ")
        aajkadin=datetime.date.today()
        if issue_id in self.books_dict.keys():
            if not self.books_dict[issue_id]['current_status']=='Available':
                print(f"This book is already issued to {self.books_dict[issue_id]['lend_name']} on{self.books_dict[issue_id]['lend_date']}. Please check after some days or Issue a different book!")
            elif self.books_dict[issue_id]['current_status']=='Available':
                issue_name=input("Enter your name : ")
                if '1' in issue_name or '2' in issue_name or '3' in issue_name or '4' in issue_name or '5' in issue_name or '6' in issue_name or '7' in issue_name or '8' in issue_name or '9' in issue_name or '0' in issue_name or '-' in issue_name:
                    print("You have entered wrong name! Please try again!")
                    return self.issue_book()
                else:
                    with open(self.lib_data) as lb:
                        issue_list=lb.readlines()
                    with open(self.lib_data,"w") as lb:
                        get_issue_bname=self.books_dict[issue_id]['b_name']
                        issue_list[int(issue_id)-1]=f"{get_issue_bname}~!!~U~!!~{issue_name}~!!~{aajkadin.year}-{aajkadin.month}-{aajkadin.day}\n"
                        lb.writelines(issue_list)
                    self.books_dict[issue_id]['lend_name']=issue_name
                    self.books_dict[issue_id]['current_status']='Un-Available'
                    self.books_dict[issue_id]['lend_date']=f"{aajkadin.year}-{aajkadin.month}-{aajkadin.day}"
                    print("Book issued Successfully!!!\n")
        else:
            print("Invalid book id chosen. Please try again")
    def return_book(self):
        #By accessing the date from file we can find the date when the book was issued and compared with todays date and charge the customer when he/she returns the book and also make changes in both file and book dictionary
        book_tobe_returned=input("Enter book id : ")
        t2=datetime.date.today()
        if book_tobe_returned in self.books_dict.keys():
            if self.books_dict[book_tobe_returned]['current_status']=='Available':
                print("Book is already available in library! Please check book id!")
            elif not self.books_dict[book_tobe_returned]['current_status']=='Available':
                with open(self.lib_data) as lb,open(self.lib_money) as lm:
                    return_list=lb.readlines()
                    ini_money=lm.readlines()
                x1=return_list[int(book_tobe_returned)-1]
                x1_l=x1.split("~!!~")
                x1_l1=x1_l[3].split("-")
                issue_y=int(x1_l1[0])
                issue_d=int(x1_l1[2].replace("\n",""))
                issue_m=int(x1_l1[1])
                t1=datetime.date(year=issue_y,month=issue_m,day=issue_d)
                money_m=(t2-t1)
                money_x=int(money_m.days)+1
                money=money_x*10
                with open(self.lib_data,"w") as lb:
                    get_issue_bname=self.books_dict[book_tobe_returned]['b_name']
                    return_list[int(book_tobe_returned)-1]=f"{get_issue_bname}~!!~A~!!~-~!!~-\n"
                    lb.writelines(return_list)
                self.books_dict[book_tobe_returned]['lend_name']='-'
                self.books_dict[book_tobe_returned]['current_status']='Available'
                self.books_dict[book_tobe_returned]['lend_date']='-'
                with open(self.lib_money,"w") as lm:
                    curr_money=int(ini_money[0].replace("\n",""))+money
                    lm.writelines(str(curr_money))
                print(f"Thank you for returning! Book issue charges is Rs {money}\n")
        else:
            print("Book ID not found!!")
    def donation(self):
        # It takes input money from user which adds up to the total money file and it can take only positive integers
        try:
            don_money=int(input("Enter the money to be donated in Rs : "))
            if don_money<=0:
                print("Wrong input given. Please try again")
                return self.donation()
            with open(self.lib_money) as lm:
                init_money=lm.readlines()
            with open(self.lib_money,"w") as lm:
                current_money=int(init_money[0].replace("\n",""))+don_money
                lm.writelines(str(current_money))
            print("Thank you for your Valuable donation\n")
        except ValueError as ve:
            print("Wrong input given. Please try again")
            return self.donation()
#---------------------------Main function-------------------------------------
if __name__=="__main__":               
    try:
        l=Library("lib_data.txt","lib_money.txt")            #Makes object of class Library
        print("Welcome to our library")
        print("How can we help you\n")
        while True:                                        #Infinite while loop
            print("\n")
            print("Press D to display books")
            print("Press A to add books")
            print("Press I to issue books")        
            print("Press R to return books")
            print("Press M to donate")
            print("Press Q to exit\n")
            choices=input("Enter your choice : ")
            print("\n")
            if choices=='D' or choices=='d':
                print("You have chosen to display books\n")
                l.display()
            elif choices=='A' or choices=='a':
                print("You have chosen to Add book\n")
                l.add_book()
            elif choices=='I' or choices=='i':
                print("Here is the list of books avilable right now:")
                l.display()              #Calling display function to show books id to user
                print("\n")
                print("You have chosen to Issue books\n")
                print("Note : Per day charges of any book is 10 Rupees\n")
                l.issue_book()
            elif choices=='R' or choices=='r':
                print("Here is the list of books:")
                l.display()               #Calling display function to show books id to user
                print("\n")
                print("You have chosen to Return books\n")
                l.return_book()
            elif choices=='M' or choices=='m':
                print("You have chosen to donate money\n")
                l.donation()
            elif choices=='Q' or choices=='q':
                break
            else:
                print("In-correct option chosen. Please try again\n")
    except Exception as e:
        print("OOPS!! Something went wrong!!\n")










































        
