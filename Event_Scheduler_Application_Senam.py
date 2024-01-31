import datetime

events = []

class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time

def authenticate_date_time(date_str, time_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        datetime.datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def add_an_event():
    title = str(input("Enter the title of the event: "))
    description = str(input("Enter the description of the event: "))
    date = input("Enter the event's date (YYYY-MM-DD): ")
    time = input("Enter the time of the event (HH:MM): ")

    if authenticate_date_time(date, time):
        events.append(Event(title, description, date, time))
        print(f"The event '{title}' was successfully added.")
    else:
        print("Date or time format is invalid. Please use the format YYYY-MM-DD for the date and HH:MM for the time.")

def list_of_events():
    sorting_of_events = sorted(events, key=lambda x: (x.date, x.time))
    if sorting_of_events:
        for event in sorting_of_events:
            print(f"{event.title} - {event.description} - {event.date} {event.time}")
    else:
        print("There are no events available.")

def delete_an_event():
    title_to_delete = str(input("Please enter the title of the event you want to delete: "))
    for event in events:
        if event.title.lower() == title_to_delete.lower():
            events.remove(event)
            print(f"Event '{title_to_delete}' has been successfully deleted.")
            return
    print(f"Event '{title_to_delete}' is not found.")

def main():
    while True:
        print("\nEvent Scheduler Menu:")
        print("1. Add an event")
        print("2. List all events")
        print("3. Delete an event")
        print("4. Exit event scheduler application")

        choice = input("Please enter your choice (1-4): ")

        if choice == "1":
            add_an_event()
        elif choice == "2":
            list_of_events()
        elif choice == "3":
            delete_an_event()
        elif choice == "4":
            print("Event schedular exited.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
