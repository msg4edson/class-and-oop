from employee import Employee

class Manager(Employee):
    def __init__(self, name, email_address, title, phone_number=None):
        super().__init__(name, email_address, title, phone_number)
        self.meetings = []
    
    def schedule_meeting(self, invitees, time):
        self.meetings.append({"time": time, "invitees": invitees})
        self.meetings.sort(key=lambda x: x["time"])

    def run_next_meeting(self):
        return self.meetings.pop(0) if self.meetings else None
    
