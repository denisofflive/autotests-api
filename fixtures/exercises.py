import pytest

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.users import UserFixture

from pydantic import BaseModel


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercise_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exercise_client=ExercisesClient,) -> ExerciseFixture:
    request = CreateExerciseRequestSchema()
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
