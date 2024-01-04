import re
print("Hello world")
email="nehanth783@gmail.com"
if re.search(r'^\w+@\w+\.\w{3}',email):
    print("Valid")
else:
    print("Invalid")