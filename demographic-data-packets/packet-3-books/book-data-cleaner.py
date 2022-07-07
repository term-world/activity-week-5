from typing import List

# DO NOT TOUCH THE BELOW FUNCTION
def grab_book_data(filename: str,) -> List[str]:
    num_books_read_list = []
    data = open(filename, "r")
    for line in data.readlines():
        num_books_read_list.append(line.strip())
    return num_books_read_list

def main():
    # This calls the grab_book_data function, grabbing the data from the poll results and storing it in a list
    dirty_data_list = grab_book_data(".books-read-poll-results.txt")
    # The below line *proves* that the output from above line is a list by printing it to the terminal
    print(dirty_data_list)

    
    


if __name__ == "__main__":
    main()