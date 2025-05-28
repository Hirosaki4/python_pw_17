import datetime

class UkrainianCalendar:
    # Метод повертає список основних державних свят
    def get_holiday_list(self):
        return [
            "01-01",  # Новий Рік
            "07-01",  # Різдво
            "08-03",  # Міжнародний жіночий день
            "01-05",  # День праці
            "09-05",  # День перемоги
            "28-06",  # День Конституції
            "24-08",  # День Незалежності
            "14-10"   # День захисників і захисниць України
        ]

    # Метод перевіряє, чи є вказана дата робочим днем
    def is_working_day(self, date):
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        holidays = self.get_holiday_list()
        date_str = date.strftime("%d-%m")
        return date.weekday() < 5 and date_str not in holidays
