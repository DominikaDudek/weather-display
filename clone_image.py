import urllib
import datetime
import Image


class ManageDate(object):
    def __init__(self):
        self.current_date = datetime.datetime.now()
        self.day = self.current_date.day
        self.month = self.current_date.month
        self.year = self.current_date.year
        self.hour = self.current_date.hour


class GetMeteogramByDate(ManageDate):
    def __init__(self):
        super(GetMeteogramByDate, self).__init__()
        self.url_to_meteogram = "http://www.meteo.pl/um/metco/mgram_pict.php?ntype=0u&fdate={}{}{}{}&row=436&col=181&lang=pl"

    def adapt_hour_and_day(self):
        first_part_of_a_day = [1, 2, 3]
        second_part_of_a_day = range(4, 11)
        third_part_of_a_day = range(11, 17)
        fourth_part_of_a_day = range(17, 23)
        last_part_of_a_day = [23, 24]

        if self.day < 10:
            self.day = '0' + str(self.day)
        if self.month < 10:
            self.month = '0' + str(self.month)

        if self.hour in first_part_of_a_day:
            self.hour = '18'
            self.day -= 1
        elif self.hour in second_part_of_a_day:
            self.hour = '00'
        elif self.hour in third_part_of_a_day:
            self.hour = '06'
        elif self.hour in fourth_part_of_a_day:
            self.hour = '12'
        elif self.hour in last_part_of_a_day:
            self.hour = '18'

    def get_current_meteogram(self):
        self.adapt_hour_and_day()
        meteogram = urllib.URLopener()
        meteogram.retrieve(self.url_to_meteogram.format(self.year, self.month, self.day, self.hour), "myFile.jpg")
        image = Image.open('myFile.jpg')
        image.show()


a = GetMeteogramByDate()
a.get_current_meteogram()

