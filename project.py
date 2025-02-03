class User:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts)

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.balance += transaction.amount

class Transaction:
    def __init__(self, amount, category, account, description=""):
        self.amount = amount
        self.category = category
        self.account = account
        self.description = description

    def __str__(self):
        return f"{self.category.name}: {self.amount} ({self.description})"

class Category:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

class FinanceManager:
    def __init__(self, user):
        self.user = user
        self.categories = {}

    def add_category(self, category):
        self.categories[category.name] = category

    def create_transaction(self, amount, category_name, account_name, description=""):
        try:
            account = next(acc for acc in self.user.accounts if acc.name == account_name)
            category = self.categories.get(category_name)
            
            if not category:
                raise ValueError("Категория не найдена")
            
            transaction = Transaction(amount, category, account, description)
            account.add_transaction(transaction)
            category.add_transaction(transaction)
            print("Транзакция успешно добавлена!")
            
        except StopIteration:
            print("Ошибка: Счёт с таким названием не найден")
        except Exception as e:
            print(f"Ошибка: {str(e)}")

def main():
    # Создаём пользователя
    user_name = input("Введите ваше имя: ")
    user = User(user_name)
    manager = FinanceManager(user)
    
    # Основное меню
    while True:
        print("\n=== Учёт финансов ===")
        print("1. Создать новый счёт")
        print("2. Добавить категорию")
        print("3. Добавить транзакцию")
        print("4. Показать общий баланс")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            acc_name = input("Название счёта: ")
            balance = float(input("Начальный баланс: "))
            user.add_account(Account(acc_name, balance))
            print(f"Счёт '{acc_name}' создан!")
            
        elif choice == "2":
            category_name = input("Название категории: ")
            manager.add_category(Category(category_name))
            print(f"Категория '{category_name}' добавлена!")
            
        elif choice == "3":
            if not user.accounts:
                print("Сначала создайте счёт!")
                continue
                
            print("\nДоступные счета:")
            for acc in user.accounts:
                print(f"- {acc.name}")
                
            account_name = input("Выберите счёт: ")
            amount = float(input("Сумма (+ доход, - расход): "))
            description = input("Описание: ")
            
            print("\nДоступные категории:")
            for cat in manager.categories.values():
                print(f"- {cat.name}")
                
            category_name = input("Выберите категорию: ")
            
            manager.create_transaction(
                amount=amount,
                category_name=category_name,
                account_name=account_name,
                description=description
            )
            
        elif choice == "4":
            print(f"\nОбщий баланс: {user.get_total_balance()} руб.")
            for acc in user.accounts:
                print(f"{acc.name}: {acc.balance} руб.")
                
        elif choice == "5":
            print("Выход из программы...")
            break
            
        else:
            print("Неверный выбор, попробуйте снова")

if __name__ == "__main__":
    main()