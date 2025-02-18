import datetime
class Logger:
    @staticmethod
    def log(messsage, level):
        print(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), level + ':', messsage)
        
    @staticmethod
    def log_func_decorator(func):
        def wrapper(*args, **kwargs):
            Logger.log(f'Вызван метод: {func}', 'INFO')
            try:
                res = func(*args, **kwargs)
                Logger.log(f'закончен метод: {func}', 'INFO')
                return res
            except Exception as e:
                Logger.log(f'Получена ошибка: {e}', 'ERROR')
                return {'code': 500, 'msg': e}
