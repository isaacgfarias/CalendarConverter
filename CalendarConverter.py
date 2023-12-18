
import os


class CalendarConverter:
     # BCE

    def to_holocene(self, gregorian_year):
        HOLOCENE_FIRST_YEAR = -10_000 # Before common era
        """
        Note:
            This function uses the starting point of 10,000 BCE for the Holocene calendar, or Human Era Calendar.
        """
        return abs(HOLOCENE_FIRST_YEAR - gregorian_year)
    
    def to_huangdi(self, gregorian_year):
        HUANGDI_FIRST_YEAR = -2698 # Before common era


        return abs(HUANGDI_FIRST_YEAR - gregorian_year)
    

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    calendar = CalendarConverter()
    print(calendar.to_holocene(2023))
    print(calendar.to_huangdi(2023))