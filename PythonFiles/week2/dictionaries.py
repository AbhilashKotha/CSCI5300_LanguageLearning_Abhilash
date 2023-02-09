research = {
    "topic": "HCI research",
    "desc": "to conduct computer interaction study",
    "duration_in_days": 30
}

# To access a specifi element
print(research["topic"]) 

# Adding an element to the dictionary
research["funding"] = "30M"
print(research) 

# Removing an element from the dictionary
del research["desc"]
print(research)

# Iterating through a dictionary
for key in research:
    print(str(key) + ": " + str(research[key]))
