from typing import List

# TO-DO: EXAMINE THE preferred-food-poll-results.txt FILE, AND BUILD A LIST THAT HAS CONTAINS ONE OF EACH POSSIBLE OPTION
# HINT: THERE SHOULD ONLY BE FOUR ITEMS IN THE LIST YOU CONSTRUCT

# DO NOT TOUCH THE BELOW FUNCTION
def grab_food_data(filename: str) -> List[str]:
    food_list = []
    data = open(filename, "r")
    for line in data.readlines():
        food_list.append(line.strip())
    return food_list

def main():
    # This calls the grab_food_data() function, grabbing the data from the poll results and storing it in a list
    preferred_foods = grab_food_data("preferred-food-poll-results.txt")
    # The below line *proves* that the output from the above line is a list by printing it to the terminal
    print(preferred_foods)


    # TO-DO: ITERATE THROUGH EACH item IN THE LIST OF POSSIBLE CHOICES (FROM THE TOP OF THIS PROGRAM)

        # TO-DO: FOR EACH ITEM, COUNT THE NUMBER OF TIMES IT OCCURS IN THE LIST preferred_foods AND STORE THIS COUNT IN num_votes
        
        
        # DO NOT TOUCH THE BELOW PRINT STATEMENT!
        print(f"{item} received {num_votes} votes")


if __name__ == "__main__":
    main()