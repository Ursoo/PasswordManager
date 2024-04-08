class PasswordController():
    def __init__(self, path) -> None:
        self.file_location = path

    def read_passwords(self):
        file_exists = self.__check_password_file_exists()

        if file_exists:
            with open(self.file_location, 'r') as file:
                passwords_list = [password.strip() for password in file]

                if passwords_list:
                    for password in passwords_list:
                        print(password)
                else:
                    print('No password in file')
        else:
            print('No file boss')
    
    def add_password_to_file(self, password):
        pass

    def __check_password_file_exists(self):
        try:
            with open(self.file_location):
                return True
        except OSError:
            return False
