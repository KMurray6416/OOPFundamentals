

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, updated_owner):
        self.owner = updated_owner

    def __str__(self):
        return (f"Vehicle Registration #: {self.registration_number}, "
                f"Type: {self.type}, Owner: {self.owner}")
