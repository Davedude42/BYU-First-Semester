import math
## CONSTANTS SHOULD GO BELOW THIS COMMENT ##

PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1
DIAMETER_LARGE = 20
DIAMETER_MEDIUM = 16
DIAMETER_SMALL = 12
COST_LARGE = 14.68
COST_MEDIUM = 11.48
COST_SMALL = 7.28
PI = 3.14159265

def main():
    ## YOUR CODE SHOULD GO IN THIS FUNCTION ##
    
    totalPeople = int(input('Please enter how many guests to order for:'))

    people = totalPeople

    large = people // PEOPLE_PER_LARGE
    people = people % PEOPLE_PER_LARGE
    medium = people // PEOPLE_PER_MEDIUM
    people = people % PEOPLE_PER_MEDIUM
    small = math.ceil(people / PEOPLE_PER_SMALL)
    people = people % PEOPLE_PER_SMALL

    print(f'{large} large pizzas, {medium} medium pizzas, and {small} small pizzas will be needed.\n')

    totalArea = PI * (large * (DIAMETER_LARGE/2)**2 + medium * (DIAMETER_MEDIUM/2)**2 + small * (DIAMETER_SMALL/2)**2)
    areaPerPerson = totalArea / totalPeople

    print(f'A total of {totalArea:.2f} square inches of pizza will be ordered ({areaPerPerson:.2f} per guest).')

    tip = float(input('Please enter the tip as a percentage (i.e. 10 means 10%):')) / 100

    totalCost = (COST_LARGE * large + COST_MEDIUM * medium + COST_SMALL * small) * (1 + tip)

    print(f'The total cost of the event will be: ${totalCost:.2f}.\n')

if __name__ == "__main__":
    main()
