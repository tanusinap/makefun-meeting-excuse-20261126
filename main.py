"""Entry for make.fun bounty: The Funniest Excuse for Skipping a Meeting.

Prints a single sharp line (<=200 characters) with an excuse for skipping
an unimportant meeting.
"""


LINE = (
    "The meeting has no agenda, no decision, and a 100% chance of "
    "ending with another meeting. I am skipping it to do the work "
    "it was called to discuss."
)


def main() -> str:
    return LINE


if __name__ == "__main__":
    print(main())
