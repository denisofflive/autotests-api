import platform
import sys

from config import settings


def create_allure_environment_file():
    os_info = f'{platform.system()}, {platform.release()}'
    python_version = sys.version
    # Создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]

    items.extend([
        f'os_info={os_info}',
        f'python_version={python_version}'
    ])

    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл
