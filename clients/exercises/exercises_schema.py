from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from pydantic.alias_generators import to_camel

class ExerciseSchema(BaseModel):
    """
    Описание структуры задания
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа вывода списка заданий
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа вывода задания
    """
    exercise: ExerciseSchema


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание задания
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    course_id: str


class CreateExerciseQueryRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class UpdateExerciseQueryRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    title: str | None     = None
    max_score: int | None = None
    min_score: int | None = None
    order_index: int | None = None
    description: str | None = None
    estimated_time: str | None = None


class UpdateExerciseQueryResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление упражнения
    """
    exercise: ExerciseSchema
