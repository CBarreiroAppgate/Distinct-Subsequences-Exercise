import sys
from app.domain.services.subsequence_counter import SubsequenceCounter
from app.application.use_cases.count_subsequences import CountSubsequences
from app.infrastructure.adapters.input.cli import run


def main() -> None:
    counter = SubsequenceCounter()
    use_case = CountSubsequences(counter)
    try:
        run(use_case)
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(0)


if __name__ == "__main__":
    main()