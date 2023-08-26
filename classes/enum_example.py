from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4

def main():
    print(Season.SPRING is Season.FALL)
    print(Season.SPRING.name)
    print(Season.SPRING.value)

    for season in Season: 
        print(f"number: {season.value}, season: {season.name}")

    attributes_season = {}
    attributes_season[Season.SPRING] = "Flowers"
    attributes_season[Season.SUMMER] = "Vacations"
    for val in attributes_season: 
        print(f"{val.name}:{attributes_season[val]}")

if __name__ == "__main__":
    main()