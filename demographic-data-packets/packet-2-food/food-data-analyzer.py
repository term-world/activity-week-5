from typing import List

def grab_food_data(filename: str) -> List[str]:
    food_list = []
    data = open(filename, "r")
    for line in data:
        food_list.append(line.strip())
    return food_list

def main():
    # This retrieves the data from the poll results and stores it in a list
    preferred_foods = grab_food_data("preferred-food-poll-results.txt")
    
    
    print(preferred_foods)

if __name__ == "__main__":
    main()