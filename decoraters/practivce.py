
def decorated_account(func):
    def wrapper(*args, **kwargs):
        pass



@decorated_account
def account(self, account_number, name, contact):
    self.account_number = account_number
    self.name = name
    self.contact = contact
    print("")
