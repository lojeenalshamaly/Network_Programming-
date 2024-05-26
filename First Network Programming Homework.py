###Question 1:
    #A

L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]

d = dict(zip(L1, L2))

print(d)
   
    #B
    
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)

num = int(input("Enter a Number : "))

result = factorial(num)

print("The factoreal of :" , (num) ,"is ", (result))

  #c
  
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in L:
    if item.startswith('B'):
        print(item)

   #D

d = {i:i+1 for i in range(11)}
print(d)

    ###Question 2:
        

binary_num = input("Enter a binary Number : ")

if not binary_num.isdigit() or any(int(digit) not in [0, 1] for digit in binary_num):
    print("Error, this number is not a binary number ")
    exit()

decimal_num = 0
for i, digit in enumerate(binary_num[::-1]):
    decimal_num += int(digit) * 2 ** i

print("Equivalent decimal number is : ", decimal_num)

     ###Question 3:

import json
questions = { }
#define a variable for the score
scores = 0
#define the question number
number=1
#loading question to the program
f = open("questions.txt",'r')
questions = json.load(f)
f.close()

print("python quiz programm")
print("Enter t for True or f for False")
name = input("Enter your full name: ")
#display the questions
for ques in questions.keys():
    #displaying the question
    print("Question",number,": ", ques)
    ans = input("The answer is ")
    #testing the result
    if ans.upper() == questions[ques].upper():
        scores = scores + 1
        print("Correct ")
    else:
        print ("Wrong")
    number = number + 1

#write the name and the score is a separate file
result={name:scores}
m = open("score.txt",'w')
result = json.dump(result,m)
m.close()


       ###Question 4:
           
class BankAccount:
    def init(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def init(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().init(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return interest_amount

    def print(self):
        print(f"Current Balance: ${self.balance} | Interest Rate: {self.interest_rate}%")

# Create an instance of BankAccount
bank_acc = BankAccount("12345", "Alice")
print("Initial Balance:", bank_acc.get_balance())

# Perform a deposit of $1000
deposit_amount = bank_acc.deposit(1000)
print("After depositing $1000:", bank_acc.get_balance())

# Perform a withdrawal of $500
withdraw_amount = bank_acc.withdraw(500)
print("After withdrawing $500:", bank_acc.get_balance())

# Create an instance of SavingsAccount
savings_acc = SavingsAccount("54321", "Bob", interest_rate=0.05)
print("\nInitial Balance for Savings Account:", savings_acc.get_balance())

# Apply interest and print the current balance and rate
interest_amount = savings_acc.apply_interest()
savings_acc.print()



