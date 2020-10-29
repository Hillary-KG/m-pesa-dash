import csv

from gmplot import *

class PinLocation():
    """a class that represents the implementation of reading the 
    facilities location  coordinates and maps them to respective google maps location markers """
    locations_data = []
    
    def get_locations(self):
        """a function that reads the csv file for location coordinates"""
        with open('res/Coordinates.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # row = json.dumps(row)
                # print(row['Latitude'])
                if (row['Latitude'] != '#N/A' and row['Longitude'] != '#N/A' and row['Facility_Name'] != ''):

                    self.locations_data.append((row['Latitude'], row['Longitude'], row['Facility_Name'], row['Category']))

        return self.locations_data


    def place_pins(self):
        """a function that consumes the location data to place markers on the map"""
        gmap = gmplot.GoogleMapPlotter(-1.28891, 36.86299, 10)
        gmap.apikey = 'AIzaSyA0VLK6IbDGJ7XP66srkPqPL3W-R4oPxDw'
        locations = self.get_locations()

        for loc in locations:
            #category A === red
            if loc[3] == 'A':
                gmap.marker(float(loc[0]), float(loc[1]), color='red', title=loc[2])   
            #category B === green
            elif loc[3] == 'B':
                gmap.marker(float(loc[0]), float(loc[1]), color='green', title=loc[2])   
            #category C === blue
            else:
                gmap.marker(float(loc[0]), float(loc[1]), color='blue', title=loc[2])

        gmap.draw('output/map.html')#writing the map into the current directory


if __name__ == '__main__':
    pinLocObj = PinLocation()
    pinLocObj.place_pins()



