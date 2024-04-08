class UserConfigurationController():
    def __init__(self, path_to_config) -> None:
        self.configuration_location = path_to_config

    def read_user_configuration(self):
        try:
            with open(self.configuration_location, 'r') as file:
                for line in file:
                    if line is not None:
                        print(line)
                    else:
                        print('File is empty')
        except OSError:
            print('file not exist boss')
            

    
    def create_user_configuration_file(self, path, master_password, path_to_decrypt_key = '/configuration/security/priv_key.txt'):
        with open(path, 'w') as file:
            pass

    def update_user_configuration_file(self, path):
        with open(path, 'w+') as file:
            pass