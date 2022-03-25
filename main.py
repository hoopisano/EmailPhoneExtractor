import re, pyperclip

phoneRegex = re.compile(r'''
(                           # Put the whole expression into one large group, so that findall() resturns a single string
((\(\d\d\d\))|(\d\d\d))?    # Area code could have perens or might not. ? means appears 0 or 1 times
(\s|-)                      # Could be dash or space btwn area code and main num
\d\d\d-\d\d\d\d             # Main phone num
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+    # Name part,  (need '+' for one or more of these characters).
@                 # @ symbol
[a-zA-Z0-9_.+]+    # Domain part, (need '+' for one or more of these characters).
''', re.VERBOSE)

# Get text off of the clipboard
text = pyperclip.paste()

# Extract the emails/phones from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# print(extractedPhone)   # Test. returns list of tuples. Append whole phones to new list (below)
# print(extractedEmail)   # Test. This one works as planned.


allPhoneNumbers = []
for phone in extractedPhone:
    allPhoneNumbers.append(phone[0])

# print(allPhoneNumbers)


# Copy the extracted emails/phones to the clipboard
results = '\n'.join(extractedEmail) + '\n\n' + '\n'.join(allPhoneNumbers)    # Joins email list and phone list with newlines
pyperclip.copy(results)
