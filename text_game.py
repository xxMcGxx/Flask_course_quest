from threading import Lock


# Класс игры будет реализован с использованием паттена "Одиночка"
# Так-же реализовано создание нового экземпляра класса, при передаче параметров в конструктор.
class SingletonMeta(type):
    '''
    Метаклас для реализации паттена "Одиночка"
    '''
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            # Новый экземпляр создается только при первом вызове или передачи параметра в конструктор.
            # Это требуется для пезапуска игры без перезапуска сервера.
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class TextQuest(metaclass=SingletonMeta):
    def __init__(self, new=False):
        '''
        Конструктор класса
        :param new: не используется, но конструктор должен иметь получаемый параметр, для создания
        нового экземпляра одиночки.
        '''
        # Начальная позиция игрока
        self._horizontal_position = 0
        self._vertical_position = 1
        # Счетчик перемещений
        self.moves = -1
        # Карта помещений, где вы уже были.
        self._rooms_map = [[0 for y in range(2)] for x in range(3)]
        self._rooms_map[self._horizontal_position][self._vertical_position] = 1
        # Краткие описания помещений
        self._rooms_desc = (
            ("В комнате стоит большая кровать и прочие спальные принадлежности, это явно спальня.",
             "В комнате много стеллажей со всяким барахлом и нет окон, это явно кладовка."),
            ("В комнате стоит большой диван и тумба с телевизором, это явно гостиная. "
             "С северной стороны комнаты имеется дверь на балкон, кажется она открыта.",
             "В комнате имется большой гардеробный шкаф, это прихожая."),
            ("В комнате имееется обеденный стол и кухонный гарнитур, это кухня",
             "В комнате стоит компьютер, стелаж с книгами, это явно рабочий кабинет.")
        )

    def end_text(self):
        '''
        :return: текст завершения игры
        '''
        return "Вы выходите на балкон, закуриваете долгожданную сигарету. " \
               "Мысли в голове начинают проясняться. Теперь можно достать почти севший" \
               " телефон, позвонить друзьям и разузнать подробности вчерашнего вечера. Конец"

    def check_visited(self):
        '''
        Проверяет был ли игрок в этом помещении, если не был то помечает, что он тут был.
        :return: Строка с сообщением, что игрок тут был, если игрок повторно зашел в это помещение
        '''
        if self._rooms_map[self._horizontal_position][self._vertical_position] == 1:
            return " Вам кажется, что вы здесь уже были."
        else:
            self._rooms_map[self._horizontal_position][self._vertical_position] = 1
            return ""

    def get_room_decs(self):
        '''
        Возвращает описание комнаты, где сейчас находится игрок
        :return: описание помещения
        '''
        return self._rooms_desc[self._horizontal_position][self._vertical_position]

    def move(self, direction):
        '''
        Движение игрока
        :param direction: направление:
        0 - Север
        1 - Восток
        2 - Юг
        3 - Запад
        :return: 1 если движение удачно, 2 если нельзя туда идти, 3 если вы пришли куда надо
        '''
        # Сначала проверим на прибытие в точку
        if direction == 0 and self._horizontal_position == 1 and self._vertical_position == 0:
            return 3
        # Проверяем можно ли туда двигаться
        if (direction == 0 and self._vertical_position == 0) or \
                (direction == 1 and self._horizontal_position == 2) or \
                (direction == 2 and self._vertical_position == 1) or \
                (direction == 3 and self._horizontal_position == 0):
            return 2
        # Раз можем, то двигаемся
        if direction == 0:
            self._vertical_position -= 1
        elif direction == 1:
            self._horizontal_position += 1
        elif direction == 2:
            self._vertical_position += 1
        elif direction == 3:
            self._horizontal_position -= 1
        self.moves += 1
        return 1

    def wrong_move_text(self):
        '''
        Текст о невозможности движения в этом направлении
        :return:
        '''
        return "Вы упираетесь в стену, дальше идти нельзя."

    def start_text(self):
        '''
        Стартовый текст
        :return: Описание начала игры.
        '''
        return "Вчерашний вечер явно удался, вы просыпаетесь на полу в непонятном промещении " \
               "без окон, но в помещении имеются две двери на севере и востоке. " \
               "Осмотрев помещение становиться понятно, что " \
               "это кладовка. У вас жутко болит голова, и вам " \
               "очень сильно хочется курить, благо после вчерашнего в кармане есть полупустая пачка сигарет " \
               "и зажигалка, осталось найти балкон на котором можно осуществить свое сокровенное желание."
