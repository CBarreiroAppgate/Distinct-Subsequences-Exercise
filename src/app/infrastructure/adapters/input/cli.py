from app.application.ports.input.count_subsequences_use_case import CountSubsequencesUseCase
from app.domain.value_objects.subsequence_query import SubsequenceQuery


def run(use_case: CountSubsequencesUseCase) -> None:
    source = input("Enter source string: ")
    target = input("Enter target string: ")

    try:
        query = SubsequenceQuery(source, target)
        result = use_case.execute(query)
        print(f"Distinct subsequences: {result}")
    except ValueError as exc:
        print(f"Invalid input: {exc}")
