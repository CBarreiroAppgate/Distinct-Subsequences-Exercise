from app.application.ports.input.count_event_subsequences_use_case import CountEventSubsequencesUseCase
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


def run_event(use_case: CountEventSubsequencesUseCase) -> None:
    raw_source = input("Enter source events (comma-separated): ")
    raw_target = input("Enter target events (comma-separated): ")

    try:
        source = [s.strip() for s in raw_source.split(",")]
        target = [t.strip() for t in raw_target.split(",")]
        query = EventSequenceQuery(source, target)
        result = use_case.execute(query)
        print(f"Distinct subsequences: {result}")
    except ValueError as exc:
        print(f"Invalid input: {exc}")
