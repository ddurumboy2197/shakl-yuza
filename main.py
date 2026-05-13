class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Task number is out of range.")

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")


todo = ToDo()

while True:
    print("\nTo'do ro'yxati dasturi:")
    print("1. Qo'shish")
    print("2. O'chirish")
    print("3. Ko'rish")
    print("4. Chiqish")

    choice = input("Izoh: ")

    if choice == "1":
        task = input("Qo'shish uchun task kiriting: ")
        todo.add_task(task)
    elif choice == "2":
        try:
            task_number = int(input("O'chirish uchun task raqam kiriting: "))
            todo.delete_task(task_number)
        except ValueError:
            print("Task raqami son bo'lishi kerak.")
    elif choice == "3":
        todo.view_tasks()
    elif choice == "4":
        break
    else:
        print("Izoh: Xato tanlov.")
```

Bunda, biz `ToDo` klassi yaratib, unda `tasks` ro'yxati yaratamiz. `add_task` metodiga yangi task qo'shish uchun, `delete_task` metodiga taskni o'chirish uchun, `view_tasks` metodiga ro'yxatni ko'rish uchun funksiyalar yozamiz. Keyin, `while` tsiklida, foydalanuvchi tanlovni tanlab, shartga muvofiq harakat qilamiz.
