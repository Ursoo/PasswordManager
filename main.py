from password_generator import PasswordGenerator

password_generator = PasswordGenerator()

password, check_result = password_generator.generate()

print(password, check_result)