## INSTRUCTIONS FOR VOTE COUNTING MACHINE

As you already know, we have collected the votes from the special comptroller election.
These votes are stored in the file `comptroller-votes.txt`.

You'll need to rig up a `vote-counter.py` that can read the votes stored in the aforementioned file
and determine the winner of the election.

The rules are simple: **whoever has the highest number of votes is the winner**.

We have some ideas for how you could rig up this machine.
We already wrote a function to *read in the vote data and present it as a list of strings*.
This will allow you *iterate* through the list and process the votes one by one.
We also suggest you write two additional functions:
1) a function that takes as input the list of votes and produces a list where each candidate is named once;
2) a function that takes as input both the list of votes and the output from the prior function,
and as a result produces a list that contains the number of votes scored by each candidate.

This means that the indices of the two output lists ought to match, or correspond.

For example, if the vote data looked like this:
`vote_data = ["Tim", "Jim", "Tim", "Clem", "Clem", "Tim"]`

Then the output of the first function might look like this:
`candidates = ["Tim", "Jim", "Clem"]`

And the output of the second function might look like this:
`num_votes = [3, 1, 2]`

Wherein `candidates[0]` corresponds with `num_votes[0]`, `candidates[1]` corresponds with `num_votes[1]`,
and of course, `candidates[2]` corresponds with `num_votes[2]`.

With a setup like this, if you found the index of the highest number in `num_votes`,
then you could use that same index to determine who the winning candidate was!

This is a pretty big ask, we know--but as per usual, our city is counting on you!