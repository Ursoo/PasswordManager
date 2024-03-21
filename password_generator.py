from random import randrange

class PasswordGenerator:
    def __init__(self, pass_length: int= 12):
        self.password_length = pass_length
        self.bad_passwords = 0

    def generate(self):
        password = ''

        while (len(password) < self.password_length):
            password+= chr(randrange(33,127))

        check_result = self.__check_pass_requirements(password= password)

        if check_result is False:
            self.bad_passwords += 1
            password, check_result = self.generate()

            print(f'bad passwords generated: {self.bad_passwords}')

        return (password, check_result)
    
    @staticmethod
    def __check_pass_requirements(password: str):

        if not all([True for character in password if character.isascii() and character.isprintable() and not character.isspace()]):
            return False
        
        if not any([True for character in password if character.isupper()]):
            return False
        elif not any([True for character in password if character.islower()]):
            return False
        elif not any([True for character in password if character.isdigit()]):
            return False
        
        return True