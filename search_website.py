import re
import requests
import selenium

class GetPawnedStatus:
    def __init__(self):
        self.url = 'https://haveibeenpwned.com/api/v2/breachedaccount/'
        self.validation = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.IGNORECASE)

    def search_email(self,email):
        if not self.validation.match(email):
            return False, None
        
        email = email.lower()
        req_url = f'{self.url}{email}'
        
GetPawnedStatus().search_email('as112@gmail.com')