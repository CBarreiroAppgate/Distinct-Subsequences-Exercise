from fastapi import FastAPI

from app.domain.services.subsequence_counter import SubsequenceCounter
from app.domain.services.event_sequence_counter import EventSequenceCounter
from app.application.use_cases.count_subsequences import CountSubsequences
from app.application.use_cases.count_event_subsequences import CountEventSubsequences
from app.infrastructure.adapters.input.rest_api import create_router


def create_app() -> FastAPI:
    counter = SubsequenceCounter()
    event_counter = EventSequenceCounter()

    use_case = CountSubsequences(counter)
    event_use_case = CountEventSubsequences(event_counter)

    router = create_router(use_case, event_use_case)

    app = FastAPI(title="Distinct Subsequences API")
    app.include_router(router)
    return app