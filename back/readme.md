# 🚀 Запуск проекта на FastAPI

## 📋 Описание проекта
Проект создан на базе **FastAPI** с использованием **Uvicorn** для запуска веб-сервера. В данном руководстве описаны шаги по установке зависимостей и запуску проекта.

---

## 📂 Структура проекта
```
📂 back/
├── 📂 .venv/                # Виртуальное окружение
├── 📂 DataBaseManager/      # Управление базой данных
│   ├── __init__.py
│   └── models.py           # Описание моделей БД 
├── 📂 utils/                # Утилиты
│   └── logger.py           # Логирование
├── 📄 .gitignore            # Игнорируемые файлы
├── 📄 main.py               # Основной файл приложения
├── 📄 models.py             # Модели для API
└── 📄 requirements.txt      # Файл зависимостей
```

---

## ⚙️ Установка и запуск проекта

### 1️⃣ Установить Python 3.10+
[Скачать Python](https://www.python.org/downloads/)

### 2️⃣ Клонировать репозиторий
```bash
git clone https://github.com/LastNightMoon/ToDo
```

### 3️⃣ Перейти в папку проекта
```bash
cd back
```

### 4️⃣ Создать виртуальное окружение и активировать его
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\\Scripts\\activate   # Windows
```

### 5️⃣ Установить зависимости
```bash
pip install -r requirements.txt
```

### 6️⃣ Запустить проект
```bash
cd back
python main.py
```

---

## 🚀 Проверка работы сервера
- **Swagger UI:** http://127.0.0.1:8000/docs  
- **Root Endpoint:** http://127.0.0.1:8000  

---

## 📌 Полезные команды
- **Создать файл зависимостей:**
  ```bash
  pip freeze > requirements.txt
  ```
- **Установить зависимости из файла:**
  ```bash
  pip install -r requirements.txt
  ```
- **Деактивировать виртуальное окружение:**
  ```bash
  deactivate
  ```
