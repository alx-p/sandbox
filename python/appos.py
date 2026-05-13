from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def git_status():
    try:
        # Выполняем команду git status
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Ошибка выполнения команды: {e.stderr}"
    except FileNotFoundError:
        output = "Команда git не найдена. Убедитесь, что git установлен."

    # Простой шаблон для вывода результата
    return render_template_string('''
        <h1>Результат git status:</h1>
        <pre>{{ output }}</pre>
    ''', output=output)

if __name__ == '__main__':
    app.run(debug=True)