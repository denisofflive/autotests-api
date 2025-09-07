import allure
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет соответствие данных задания ожидаемым значениям.

    :param actual: Фактические данные задания
    :param expected: Ожидаемые данные задания
    :raises AssertionError: Если данные не соответствуют
    """
    assert_equal(actual.id, expected.id, "exercise_id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Check create exercise response")
def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на создание задания соответствует данным из запроса.

    :param request: Запрос на создание задания
    :param response: Ответ API с созданным заданием
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check get exercise response")
def assert_get_exercise_response(
        actual: GetExerciseResponseSchema,
        expected: CreateExerciseResponseSchema
):
    """
    Проверяет соответствие ответа на получение задания ожидаемым данным.

    :param actual: Ответ API с полученным заданием
    :param expected: Ожидаемые данные задания (из фикстуры создания)
    :raises AssertionError: Если данные не соответствуют
    """
    assert_exercise(actual.exercise, expected.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: GetExerciseResponseSchema
):
    """
    Проверяет соответствие ответа на обновление задания данным из запроса.

    :param request: Запрос на обновление задания
    :param response: Ответ API с обновленным заданием
    :raises AssertionError: Если данные не соответствуют ожидаемым
    """

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверяет, что ответ соответствует ошибке "Exercise not found".

    :param actual: Ответ API с ошибкой
    :raises AssertionError: Если сообщение об ошибке не соответствует ожидаемому
    """
    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercise_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет соответствие списка заданий ожидаемым значениям.

    :param  get_exercise_response: Ответ API со списком заданий
    :param create_exercise_responses: Список ожидаемых заданий
    :raises AssertionError: Если данные не соответствуют
    """
    assert_length(get_exercise_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercise_response.exercises[index], create_exercise_response.exercise)
