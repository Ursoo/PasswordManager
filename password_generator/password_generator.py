from random import randrange

class PasswordGenerator:
    def __init__(self, pass_length: int= 20):
        self.password_length = pass_length

    def generate(self):
        password = ''

        password_dict = self.__build_password_dict()
        used_character_types = {}

        while (len(password) < self.password_length):
            random_id = randrange(1,5)
            while random_id not in password_dict:
                random_id = randrange(1,5)
            character_type = password_dict.pop(random_id) #select a character type at random
            
            used_character_types.update({random_id: character_type})
            
            if (len(password_dict.keys()) == 0):
                password_dict = used_character_types.copy()
                       
            password_character = character_type[randrange(0, len(character_type))]
            
            password+= password_character

        
        return password
    
    def __build_password_dict(self):
        letters = [chr(nr) for nr in range(97,123)]
        capital_letters = [chr(nr) for nr in range(65,91)]
        digits = [str(nr) for nr in range (0,10)]
        symbols = [chr(nr) for nr in range (32,127) if nr in range (32,48) or nr in range(58,65) or nr in range(91,97) or nr in range(123,127)]

        password_dict = {1: letters,
                         2: capital_letters,
                         3: digits,
                         4: symbols}
        
        return password_dict