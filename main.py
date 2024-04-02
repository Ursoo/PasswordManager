from password_generator.password_generator import PasswordGenerator
from validation import validate_password

password_generator = PasswordGenerator()

check_result = True

while check_result == True:
    password = password_generator.generate()

    check_result = validate_password(password)

    print(password, check_result)