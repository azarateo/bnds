from enum import Enum

class TDays(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    
today = TDays.WEDNESDAY
tomorrow = TDays.THURSDAY

print(today.name)
print(today.value)