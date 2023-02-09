class CollegeEvent:

    def __init__(self, eventTitle, location, date):
        self.eventTitle = eventTitle
        self.location = location
        self.date = date

    def createInvitation(self):
        return "You are invited to " + self.eventTitle + " event which is happening at " + self.location + " on this " + self.date +"th"

CollegeEvent = CollegeEvent("recruitment", "Busch", "17")
print(CollegeEvent.createInvitation()) 
