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
    # Выбор категории (из первой ветки)
    category = input("Выберите категорию (работа / хобби / технологии): ").strip().lower()
    if category in ideas_by_category and ideas_by_category[category]:
        idea = random.choice(ideas_by_category[category])
    else:
        all_ideas = [item for sublist in ideas_by_category.values() for item in sublist]
        idea = random.choice(all_ideas)
    
    print(f"Ваша идея ({category}): {idea}")
    
    # Сохранение в файл (из второй ветки)
    save = input("Сохранить идею в favorites.txt? (y/n): ").strip().lower()
    if save == "y":
        with open("favorites.txt", "a", encoding="utf-8") as f:
            f.write(idea + "\n")
        print("Идея сохранена в favorites.txt!")

if name == "main":
    main()