"""FastAPI application providing planning and rendering endpoints."""

from fastapi import FastAPI

from .gpt_planner import GPTPlanner
from .veo_client import VeoClient
from .styles import StyleRotator
from .publisher import Publisher
from .scheduler import Scheduler
from . import schemas

app = FastAPI()

_planner = GPTPlanner()
_renderer = VeoClient()
_rotator = StyleRotator()
_publisher = Publisher()
_scheduler = Scheduler(_planner, _renderer, _rotator, _publisher)


@app.post("/plan", response_model=schemas.PlanResponse)
def plan(req: schemas.PlanRequest) -> schemas.PlanResponse:
    plan_data = _planner.plan(req.topic)
    return schemas.PlanResponse(**plan_data)


@app.post("/render", response_model=schemas.RenderResponse)
def render(req: schemas.RenderRequest) -> schemas.RenderResponse:
    style = req.style or _rotator.get_style()
    video = _renderer.render(req.plan.dict(), style)
    return schemas.RenderResponse(**video)


@app.post("/run-daily", response_model=schemas.RunDailyResponse)
def run_daily(req: schemas.RunDailyRequest) -> schemas.RunDailyResponse:
    result = _scheduler.run_daily(req.topic)
    return schemas.RunDailyResponse(
        plan=schemas.PlanData(**result["plan"]),
        video=schemas.RenderResponse(**result["video"]),
        publication=result["publication"],
    )
