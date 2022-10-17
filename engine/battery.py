from datetime import datetime
import unittest

class battery(unittest.TestCase):
    def SplindlerBattery (self, last_service_date, current_date, needs_service):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        print (last_service_date)
    