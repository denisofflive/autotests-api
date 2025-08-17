from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from pydantic.alias_generators import to_camel


# Добавили описание структуры курса
class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema  # Вложенная структура файла
    estimated_time: str
    created_by_user: UserSchema  # Вложенная структура пользователяженная структура пользователя


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    user_id: str


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str
    preview_file_id: str
    created_by_user_id: str


# Добавили описание структуры запроса на создание курса
class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    title: str | None = None
    max_score: int | None = None
    min_score: int | None = None
    description: str | None = None
    estimated_time: str | None = None
