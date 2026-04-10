import sys
from app.domain.services.subsequence_counter import SubsequenceCounter
from app.domain.services.event_sequence_counter import EventSequenceCounter
from app.application.use_cases.count_subsequences import CountSubsequences
from app.application.use_cases.count_event_subsequences import CountEventSubsequences
from app.infrastructure.adapters.input.cli import run
from app.infrastructure.adapters.input.event_cli import run_event


def main() -> None:
    print("Select mode:")
    print("  1. String subsequences  (e.g. rabbbit / rabbit)")
    print("  2. Event subsequences   (e.g. LOGIN,ADD_TO_CART / ADD_TO_CART)")
    mode = input("Mode [1/2]: ").strip()

    try:
        if mode == "1":
            use_case = CountSubsequences(SubsequenceCounter())
            run(use_case)
        elif mode == "2":
            use_case = CountEventSubsequences(EventSequenceCounter())
            run_event(use_case)
        else:
            print("Invalid mode. Choose 1 or 2.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(0)


if __name__ == "__main__":
    main()