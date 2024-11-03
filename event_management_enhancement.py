
class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participants_count = 0

        def add_to_participants(self):
            self.participants_count += 1
            print(f"Participant added. Current count for '{self.name}': {self.participants_count}")
        
        def get_participant_count(self):
            return self.participants_count
        
        def __str__(self):
            return f"Event: {self.name}, Date: {self.date}, Participants: {self.participants_count}"
        
        