from os.path import isfile

from password_generator.password_generator import PasswordGenerator
from validation import validate_password
from manager_configuration.controller import UserConfigurationController
from password_vault_controller.controller import PasswordController

SECURITY_FILE_NAME = '/security.txt'

user_config = UserConfigurationController(SECURITY_FILE_NAME)

while (True):
    user_input = input()
