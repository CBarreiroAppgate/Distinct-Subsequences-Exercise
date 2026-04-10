from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.application.ports.input.count_subsequences_use_case import CountSubsequencesUseCase
from app.application.ports.input.count_event_subsequences_use_case import CountEventSubsequencesUseCase
from app.domain.value_objects.subsequence_query import SubsequenceQuery
from app.domain.value_objects.event_sequence_query import EventSequenceQuery


class SubsequenceRequest(BaseModel):
    source: str
    target: str


class EventSubsequenceRequest(BaseModel):
    source: list[str]
    target: list[str]


class SubsequenceResponse(BaseModel):
    count: int


def create_router(
    use_case: CountSubsequencesUseCase,
    event_use_case: CountEventSubsequencesUseCase,
) -> APIRouter:
    router = APIRouter()

    @router.post("/subsequences", response_model=SubsequenceResponse)
    def count_subsequences(req: SubsequenceRequest):
        try:
            query = SubsequenceQuery(req.source, req.target)
            return SubsequenceResponse(count=use_case.execute(query))
        except ValueError as exc:
            return JSONResponse(
                status_code=422,
                content={"detail": [{"field": "input", "message": str(exc)}]},
            )

    @router.post("/event-subsequences", response_model=SubsequenceResponse)
    def count_event_subsequences(req: EventSubsequenceRequest):
        try:
            query = EventSequenceQuery(req.source, req.target)
            return SubsequenceResponse(count=event_use_case.execute(query))
        except ValueError as exc:
            return JSONResponse(
                status_code=422,
                content={"detail": [{"field": "input", "message": str(exc)}]},
            )

    return router