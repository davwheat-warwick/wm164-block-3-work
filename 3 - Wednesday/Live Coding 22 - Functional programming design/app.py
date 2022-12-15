def startup() -> None:
    """Print info about the program."""
    print("This program tells you how to")
    print("disassemble an ACME laundry dryer.")
    print("There are 4 steps in the process.")


def step1() -> None:
    """Print info about step 1."""
    print("Step 1: Unplug the dryer and")
    print("move it away from the wall.")


def step2() -> None:
    """Print info about step 2."""
    print("Step 2: Remove the six screws")
    print("from the back of the dryer.")


def step3() -> None:
    """Print info about step 3."""
    print("Step 3: Remove the back panel")
    print("from the dryer.")


def step4() -> None:
    """Print info about step 4."""
    print("Step 4: Pull the top of the")
    print("dryer straight up.")


def main() -> None:
    """Main entrypoint of the application"""
    startup()
    step1()
    step2()
    step3()
    input("Press Enter to see Step 4.")
    step4()


if __name__ == "__main__":
    main()
