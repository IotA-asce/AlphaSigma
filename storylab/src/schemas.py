"""Pydantic schemas for the API."""

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class PlanRequest(BaseModel):
    topic: str


class PlanData(BaseModel):
    title: str
    scenes: List[str]


class RenderRequest(BaseModel):
    plan: PlanData
    style: str | None = None


class RenderResponse(BaseModel):
    video: str


class PlanResponse(PlanData):
    pass


class RunDailyRequest(BaseModel):
    topic: str


class RunDailyResponse(BaseModel):
    plan: PlanData
    video: RenderResponse
    publication: str
