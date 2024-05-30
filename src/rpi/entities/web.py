from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, Field


class PagesLimit(BaseModel):
    page_from: int = Field(description='с какой страницы печатать')
    page_to: int = Field(description='по какую страницу печатать')


class PagesPerList(StrEnum):
    one_page_per_list = 'one_page_per_list'
    two_pages_per_list = 'two_pages_per_list'
    four_pages_per_list = 'four_pages_per_list'


class PrintingParameters(BaseModel):
    page_limits: PagesLimit | None = Field(description='обрезка страниц')
    pages_per_list: PagesPerList = Field(description='сколько страниц на листе')
    double_sided_flg: bool = Field(description='двусторонняя печать')
    color_printing_flg: bool = Field(description='цветная печать')


class PrintingTaskWeb(BaseModel):
    id: UUID = Field(description='id-шник задачки на печать')
    parameters: PrintingParameters = Field(description='параметры печати', default=None)


class CompletionStatus(StrEnum):
    success = 'success'
    failed = 'failed'
