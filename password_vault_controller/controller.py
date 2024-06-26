from os.path import isfile
from validation import validate_password


class PasswordController():
    def __init__(self, path) -> None:
        self.file_location = path
        self.file_exists = isfile(self.file_location)

    def retrieve_password(self):

        if self.file_exists:
            with open(self.file_location, 'r') as file:
                passwords_list = [password.strip() for password in file]

                if passwords_list:
                    return passwords_list
                else:
                    return 'No password in file'
        else:
            return f'File {self.file_location} not found.'

    def add_password_to_file(self, password: str, password_name: str):
        line = f'{password_name} : {password}'

        with open(self.file_location, 'a') as file:
            if validate_password(password):
                file.write(line)
                file.write('\n')
            else:
                return f'{password} does not meet the requirements for a strong password'

        return f'{line} added to password file succesfully!'
