class PasswordGenerator:
    def __init__(self, pass_length = 8):
        self.password_length = pass_length

    def generate(self):
        password = ''

        while (len(password) < self.password_length):
            password+= f'{len(password)}'

        return password