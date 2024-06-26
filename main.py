from password_generator.password_generator import PasswordGenerator
from validation import validate_password
from configuration_controller.controller import UserConfigurationController
from password_file_controller.controller import PasswordController

user_controller = UserConfigurationController('resources/configuration/my_config.txt')

user_controller.read_user_configuration()

password_controller = PasswordController('resources/configuration/my_passwords.txt')

password_controller.read_passwords()

password_controller2 = PasswordController('resources/configuration/my_passwords_empty.txt')

password_controller2.read_passwords()

password_controller3 = PasswordController('resources/configuration/asdasy.txt')

password_controller3.read_passwords()

#password_generator = PasswordGenerator()

#password = password_generator.generate()