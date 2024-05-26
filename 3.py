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