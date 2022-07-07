## INSTRUCTIONS FOR INTELLECTUAL POTENTIAL ASSESSMENT DATA

It's important to the mayor that `term-world` stay populated by the best and the brightest.
He has been collecting polling data on the number of books that people read annually.
Naturally, this metric has been scientifically proven to be the
best possible assessment of an individual's intellectual potential.

That same scientific literature has found that the brightest folks read an average of 364.25 books per year.
(Of course, that's one book a day, with one day off
for any major scheduled surgeries that may make reading difficult.
Like laser eye surgery.)

The mayor asked residents to share how many books they read in an average month.
(You'd hope for at least 30.354167 books per month to meet the 364.25/year threshold, obviously.)
However, our in-house pollster must not have read the latest scientific literature
on the number of books that ought to be read, and he disappointingly only asked if participants read
`0`, `1`, `2`, or `2+` (more than 2) books per month.

Of course, these figures spectacularly fail to capture the sort of data we're looking for,
so we need you to, er, *clean* this data up.

We're going to assume that anyone that has read `2+` books per month has *actually* read
`31` books per month (or 30.354167 rounded up). This is a natural assumption to make, of course,
given the aforementioned research on the average number of books read by intelligent people.

*We need you to write a program that will replace every instance of `2+`*
*in our list of number of books read with `31`.*

As with the packet on preferred food, we already have a program that can read in the data
from the relevant poll and store that information in a list.
It's your job to find a way to manipulate that list so it resembles our desired outcome.

It's important to note that the **order** of items in the list is important to maintain in this particualr instance.
So if the original data list was `[2, 1, 2+, 0]` then the end result must be `[2, 1, 31, 0]`.

I'm also told it's important to protect the original data file, so unfortunately this time
*we have to withhold the original data file from you*. You'll still be able to `print()`
its contents like normal, but the `.txt` file itself will be unavailable to you.
For security purposes, of course.