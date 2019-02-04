import re
test_email_1 = "shamehamilton@gmail.com"
test_email_2 = "23@23.com"
test_email_3 = "Shane.hamilton@me.info"
test_email_4 = "test@.2"
test_email_5 = "test@sub.domain.com"
user_email_test = input('Enter Your Email Address: ')

print(bool(re.match("(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", test_email_1)))
print(bool(re.match("(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", test_email_2)))
print(bool(re.match("(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", test_email_3)))
print(bool(re.match("(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", test_email_4)))
print(bool(re.match("(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", test_email_5)))

if bool(re.match("(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", user_email_test)):
    print('Your Email Address is Valid')
else:
    print('Your Email Address is NOT Valid')
