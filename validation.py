def validate_password(password: str):

        if not all([True for character in password if character.isascii() and character.isprintable() and not character.isspace()]):
            return False
        
        if not any([True for character in password if character.isupper()]):
            return False
        elif not any([True for character in password if character.islower()]):
            return False
        elif not any([True for character in password if character.isdigit()]):
            return False
        
        return True