"""
Data validators.
"""
from pydantic import BaseModel, Field


class Ai_Title(BaseModel):
    """
    Title validators.
    """

    title: str = Field(..., min_length=1, max_length=1000)


class Ai_Authors(BaseModel):
    """
    Author validators.
    """

    author: str = Field(..., min_length=1, max_length=1000)


class Ai_Links(BaseModel):
    """
    Link validators.
    """

    link: str = Field(..., min_length=1, max_length=1000)
