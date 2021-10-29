import random


def tearDownRun(data):
    print("Final Data is : ")
    print(data)


def locationUpdate(data):

    x = int(data.split(':')[0]) + random.randint(-1, 1)
    y = int(data.split(':')[1]) + random.randint(-1, 1)
    xy = str(x) + ':' + str(y)
    return(xy)


class scs:
    def Start(self, data):
        if data["airplane_number"] == "0":
            data["airplane_number"] = str(random.randint(1, 100))
        pass

    def ATC(self, data):
        data['state'] = int(data['state']) + 1

    def Airplane(self, data):
        if data['airplane_visited'] == '0':
            data['airplane_visited'] = 1
            print("Airplane Number : ", data["airplane_number"])

    def Pilot(self, data):
        print("Pilot is sitting in Airplane Number : {}".format(
            data["pilot_number"]))

    def Runway(self, data):
        pass

    def assignRunway(self, data):
        print("Airplane Number : {} was assigned Runway {}".format(
            data["airplane_number"], data["runway_number"]))
        data["runway_status"] = "Free"
        data["runway_number"] = 0

    def start_operation(self, data):
        pass

    def getLocation(self, data):
        data['airplane_1_location'] = locationUpdate(
            data['airplane_1_location'])
        x = data['airplane_1_location'].split(':')[0]
        y = data['airplane_1_location'].split(':')[1]

        print(
            "Airplane Number : {} is at co-ordinate : {},{}".format(data["airplane_number"], x, y))

    def getPilot(self, data):
        data["pilot_number"] = data["airplane_number"]

    def makeConflictAmend(self, data):
        pass

    def predictConflict(self, data):
        pass

    def resolveConflict(self, data):
        pass

    def returnATCfromAir(self, data):
        pass

    def returnATCfromPilot(self, data):
        pass

    def returnATCfromRunway(self, data):

        pass

    def runwayAssignment(self, data):
        if data['runway_status'] == "Busy":
            print("Runway is busy, Try Again")
            pass
        data['runway_status'] = "Busy"
        data["runway_number"] = str(random.randint(1, 100))
