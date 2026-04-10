from app.application.ports.input.count_subsequences_use_case import CountSubsequencesUseCase


def run(use_case: CountSubsequencesUseCase) -> None:
    source = input("Enter source string: ")
    target = input("Enter target string: ")

    try:
        result = use_case.execute(source, target)
        print(f"Distinct subsequences: {result}")
    except ValueError as exc:
        print(f"Invalid input: {exc}")
