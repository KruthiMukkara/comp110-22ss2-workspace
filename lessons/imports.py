"""Examples of importing Python."""


from lessons import helpers


# import names defined globally in a module.
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(powerful(2,4))
    print(f"The answer: {THE_ANSWER}")

if __name__ == "__main__":
    main()