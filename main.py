from password_generator.password_generator import PasswordGenerator
from validation import validate_password
from configuration_controller.controller import UserConfigurationController
from password_file_controller.controller import PasswordController

#user_controller = UserConfigurationController('resources/configuration/my_config.txt')

#user_controller.read_user_configuration()

password_controller = PasswordController('resources/configuration/my_passwords.txt')

#print(password_controller.read_passwords())
print(password_controller.add_password_to_file('psldapxzcvz', 'google'))
print(password_controller.add_password_to_file('psld1a,pxzcvZ', 'google'))

password_controller2 = PasswordController('resources/configuration/my_passwords_empty.txt')

print(password_controller2.read_passwords())

password_controller3 = PasswordController('resources/configuration/asdasy.txt')

print(password_controller3.read_passwords())

#password_generator = PasswordGenerator()

#password = password_generator.generate()