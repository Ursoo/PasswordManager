from os.path import isfile


class UserConfigurationController():
    def __init__(self, path_to_config) -> None:
        self.path = path_to_config

    def read_configuration_file(self):
        if isfile(self.path):
            with open(self.path, 'r') as file:
                content = file.readlines()

                if not content:
                    self._handle_invalid_config_file()
        else:
            self._handle_invalid_config_file()


    def _handle_invalid_config_file(self):
        user_input = input('File doesn\'t exist, do you want to create? (Y\N)')

        if not isinstance(user_input, str) or user_input.lower() != 'y' or user_input.lower() != 'n':
            print('Only valid answers are Y\N')
            self._handle_invalid_config_file()
        else:
            self.create_user_configuration()

        
    
    def create_user_configuration(self, data):
        with open(self.path, 'w') as file:
            file.write(data)
        

    def update_user_configuration_file(self, path):
        with open(path, 'w+') as file:
            pass
