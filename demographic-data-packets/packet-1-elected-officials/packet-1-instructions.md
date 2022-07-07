INSTRUCTIONS FOR ELECTED OFFICIAL REGISTRY REBUILDER

During the attack on city hall it appears as though we lost data pertaining to
the identity of each neighborhood's elected official.

We need a simple tool that will allow us to quickly reconstruct this data in case this ever happens again.

The `registry-rebuilder.py` should contain a list of all the `neighborhoods` in `term-world`;
we don't anticipate this list to change, so it can be hard-coded directly into the program.
The program should then check its list of `elected_officials` and,
if the number of `elected_officials` is less than the number of `neighborhoods`,
it should prompt the user to enter the name of another elected official.
The process should repeat until the number of `elected_officials` matches the number of `neighborhoods`.

This will allow our staff to quickly rebuild data on the representatives of `term-world`
should an attack of this magnitude ever occur again.