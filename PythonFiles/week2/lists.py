subjects = ["Software Engineering", "Computing and Society", "Human Computer Interaction"]

print("Here are the list of subjects available for spring semester")
print(subjects)

choice = input("What do you want to do: 1: add a subject 2: remove a subject ")
subName = input("what is the subject?")
if(choice=="1"):
    subjects.append(subName)
    print("subject added")
    print(subjects)
else:
    subjects.remove(subName)
    print("subject removed")
    print(subjects)
