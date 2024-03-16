from random import randrange

class PasswordGenerator:
    def __init__(self, pass_length = 12):
        self.password_length = pass_length

    def generate(self):
        password = ''

        while (len(password) < self.password_length):
            password+= chr(randrange(33,127))

        return password