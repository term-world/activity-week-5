from typing import List


def grab_votes(filename: str) -> List[str]:
    votes = []
    data = open(filename, "r")
    for line in data.readlines():
        votes.append(line.strip())
    return votes


# TO-DO: WRITE A FUNCTION THAT TAKES AS INPUT THE LIST OF VOTES
# AND PRODUCES AS OUTPUT A LIST OF STRINGS WHERE EACH CANDIDATE IS REPRESENTED ONLY ONCE


# TO-DO: WRITE A FUNCTION THAT TAKES TWO INPUTS--THE LIST OF VOTES, AND THE LIST OF CANDIDATES--
# AND PRODUCES AS OUTPUT A LIST OF INTS THAT CONTAINS THE NUMBER OF VOTES RECEIVED BY EACH CANDIDATE


# IMPORTANT: THE OUTPUT LISTS FROM THE ABOVE TWO FUNCTIONS SHOULD HAVE INDICES THAT CORRESPOND WITH EACH OTHER
# PLEASE REFER TO THE INSTRUCTIONS DOCUMENT FOR MORE DETAILED CLARIFICATION REGARDING THIS


def main():
    # TO-DO: CALL THE grab_votes() FUNCTION TO COLLECT VOTE DATA (YOU MAY WISH TO REFER TO PACKET #2)

    # TO-DO: CALL THE FUNCTION WRITTEN ABOVE THAT GENERATES A LIST OF CANDIDATES

    # TO-DO: CALL THE FUNCTION WRITTEN ABOVE THAT GENERATES THE NUMBER OF VOTES RECEIVED BY EACH CANDIDATE

    # TO-DO: USE THE TWO OUTPUT LISTS (AND THEIR CORRESPONDING INDICES) TO FIND THE WINNING CANDIDATE
    # HINT: THE .max() METHOD OF LISTS CAN FIND THE HIGHEST VALUE WITHIN A LIST



    # DO NOT TOUCH BELOW PRINT STATEMENTS
    print()
    print(f"The winner of the comptroller race is: {winning_candidate} with {highest_vote_count} votes!")
    print()


if __name__ == "__main__":
    main()