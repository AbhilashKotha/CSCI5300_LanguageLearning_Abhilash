import re

email_pattern_reg = re.compile(r'[\w.-]+@[\w.-]+\.[\w]+')

def extract_emails(text):
    return email_pattern_reg.findall(text)


text = input("Enter the text you want to extract emails from")
print("Emails:", extract_emails(text))
