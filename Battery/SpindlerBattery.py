from battery import battery
from util import add_years

class SpindlerBattery(battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date


    def needs_service(self):
        service_date = add_years(self.last_service_date, 3)
        if service_date < self.current_date:
            return True
        else:
            return False

