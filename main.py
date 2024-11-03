from vehicle_registration_system import Vehicle

  # Task 1

vehicles = {}

def log_vehicle(reg_num, type, owner):
    if reg_num in vehicles.items():
        print("Error: Please choose another number this number is already registered")
    else:
        vehicle = Vehicle(reg_num, type, owner)
        vehicles[reg_num] = vehicle

log_vehicle("QRS789", "MOTORCYCLE", "Charles Dixon")
log_vehicle("AED689", "SUV", "Angie Stellarose")
log_vehicle("675309", "SMART CAR", "Elon Musk")

for vehicle in vehicles.values():
    print(f"\n{vehicle}")

vehicles["AED689"].update_owner("Billie Stellarose")
vehicles["675309"].update_owner("Bill Gates")

print(f"\n*** Vehicle information after updates: ***")
for vehicle in vehicles.values():
    print(f"\n{vehicle}")

  # Task 2
from event_management_enhancement import Event

events = {}
        
def add_participant(e_name,e_date):
    if e_name in events:
        events[e_name].add_to_participants()
    else:
        event = Event(e_name,e_date)
        events[e_name] = event
        event.add_to_participants()

    

def participant_count(events):
    for event in events.values():
        print(f"Total participants for '{event.name}': {event.get_participant_count()}")

while True:
    action = input(f"\n Please type an action (add, get count, quit): ").lower()
    if action == "add":
        name = input("Please enter Event's name: ")
        date = input("Please enter the date of Event (format: MM/DD/YYYY): ")
        add_participant(name, date)
    elif action == "get count":
        participant_count(events)
    elif action == "quit":
        break

    
    