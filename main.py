import random

ideas_by_category = {
    "работа": [
        "Написать книгу",
        "Автоматизировать учёт расходов",
        "Подготовить презентацию"
    ],
    "хобби": [
        "Создать мобильное приложение для заметок",
        "Сделать Telegram-бота для погоды"
    ],
    "технологии": [
        "Открыть онлайн-курс по программированию",
        "Изучить новый фреймворк"
    ]
}

def main():
    category = input("Выберите категорию (работа / хобби / технологии): ").strip().lower()
    if category in ideas_by_category and ideas_by_category[category]:
        idea = random.choice(ideas_by_category[category])
    else:
        idea = random.choice([item for sublist in ideas_by_category.values() for item in sublist])
    print(f"Ваша идея ({category}): {idea}")

if name == "main":
    main()