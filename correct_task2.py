from typing import List
import re

email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

def count_valid_emails(emails:List[str])->int:

    count = 0
    for email in emails:
        if not isinstance(email,str):
            continue
        if email_pattern.match(email.strip()):
            count +=1
        
    return count
    
valid_email_count = count_valid_emails([
    "kidus@mail.com",
        "john12@gmail.com",
        "jack@22",
        "kidus@@gmail.com"
])

print("valid email count:", valid_email_count)