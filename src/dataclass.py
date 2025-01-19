"""
Data validators.
"""
from pydantic import BaseModel, Field


class AiTitle(BaseModel):
    """
    Title validators.
    """

    title: str = Field(..., min_length=1, max_length=1000)


class AiAuthors(BaseModel):
    """
    Author validators.
    """

    author: str = Field(..., min_length=1, max_length=1000)


class AiLinks(BaseModel):
    """
    Link validators.
    """

    link: str = Field(..., min_length=1, max_length=1000)
