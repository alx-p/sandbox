import os
import subprocess
from flask import Flask, render_template_string
from markupsafe import escape

app = Flask(__name__)

# Путь к репозиторию. Можно вынести в переменную окружения GIT_REPO_PATH
REPO_PATH = os.getenv('GIT_REPO_PATH', '/app') 
TIMEOUT_SECONDS = 5

def get_git_status(repo_path: str) -> str:
    """
    Выполняет команду 'git status --porcelain' в указанном каталоге.
    Возвращает вывод команды или сообщение об ошибке.
    """
    try:
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_path, # Указываем рабочую директорию
            timeout=TIMEOUT_SECONDS
        )
        return result.stdout or "Репозиторий чист. Изменений нет."

    except subprocess.TimeoutExpired:
        return f"Ошибка: Команда git status не завершилась за {TIMEOUT_SECONDS} секунд."
    except subprocess.CalledProcessError as e:
        # Код возврата не 0 (например, не git-репозиторий)
        return f"Ошибка git: {e.stderr or 'Неизвестная ошибка при выполнении команды'}"
    except FileNotFoundError:
        return "Ошибка: Команда 'git' не найдена. Убедитесь, что Git установлен и доступен в PATH."
    except Exception as e:
        return f"Неожиданная ошибка: {str(e)}"

@app.route('/')
def git_status():
    """
    Веб-эндпоинт, отображающий статус git-репозитория.
    """
    raw_output = get_git_status(REPO_PATH)
    
    # Экранируем вывод для безопасного отображения в HTML
    safe_output = escape(raw_output)

    return render_template_string('''
        <h1>Статус репозитория ({{ repo_path }})</h1>
        <pre style="background-color: #f4f4f4; padding: 10px; border-radius: 5px;">
            {{ output }}
        </pre>
    ''', repo_path=REPO_PATH, output=safe_output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
