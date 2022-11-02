"""
In this section we will about how the voting app work.......
________________________________________________________________
question : there is a voting in village and government has made a online platform where anyone can check that he or she
is eligible for voting or not.
________________________________________________________________________________________________________________________
approach : first we take an input from user in form of integer and check the number whether the number is greater than
           18 or not . if number is greater, than person is eligible for voting else not.
"""
A = int(input("Enter your age : "))
if(A > 18):
    print("Eligible for voting.")
else:
    print("Not eligible for voting.")
