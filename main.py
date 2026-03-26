import random

ideas = [
    "Написать книгу",
    "Создать мобильное приложение для заметок",
    "Открыть онлайн-курс по программированию",
    "Автоматизировать учёт расходов",
    "Сделать Telegram-бота для погоды"
]

def main():
    idea = random.choice(ideas)
    print(f"Ваша идея: {idea}")
    
    save = input("Сохранить идею в favorites.txt? (y/n): ").strip().lower()
    if save == "y":
        with open("favorites.txt", "a", encoding="utf-8") as f:
            f.write(idea + "\n")
        print("Идея сохранена в favorites.txt!")

if name == "main":
    main()