import datetime
class Logger:
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    @staticmethod
    def log(message: str, level):
        print(f'{datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")} -: {level} {message}')
        
    @staticmethod
    def log_func_decorator(func):
        def wrapper(*args, **kwargs):
            Logger.log(f'Вызван метод: {func}', Logger.INFO)
            try:
                res = func(*args, **kwargs)
                Logger.log(f'закончен метод: {func}', Logger.INFO)
                return res
            except Exception as e:
                Logger.log(f'Получена ошибка: {e}', Logger.ERROR)
                return {'code': 500, 'msg': e}
        return wrapper