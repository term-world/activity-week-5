from typing import List

# DO NOT TOUCH THE BELOW FUNCTION
def grab_book_data(filename: str) -> List[str]: 
    num_books_read_list = []
    data = open(filename, "r")
    for line in data.readlines():
        num_books_read_list.append(line.strip())
    return num_books_read_list

def main():
    # This calls the grab_book_data() function, grabbing the data from the poll results and storing it in a list
    data_list = grab_book_data(".books-read-poll-results.txt")
    # The below lines *prove* that the output from above line is a list by printing it to the terminal
    print("The original data is as follows:")
    print(data_list)


    # TO-DO: IMPLEMENT A while LOOP THAT RUNS AS LONG AS THE STRING "2+" IS CONTAINED in data_list

        # TO-DO: USING THE .index(), .pop(), AND .insert() METHODS, "CLEAN" THE DATA
        # REFER TO THE SPECIFICATIONS IN THE INSTRUCTIONS DOCUMENT
    

    # DO NOT TOUCH THESE PRINT STATEMENTS
    print("The data after it has been 'cleaned' is as follows:")
    print(data_list)

if __name__ == "__main__":
    main()