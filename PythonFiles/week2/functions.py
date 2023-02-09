def draftGreeting(name):
    # drafts greeting for an email after passing a name
    print("Hello, " + name + ",")

nameOfRecipient = input("Who is the recipient: ")
draftGreeting(nameOfRecipient)