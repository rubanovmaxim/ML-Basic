class MediaFile:
    """Базовый класс для медиафайлов"""

    def __init__(self, name, size, creation_date, owner):
        """Инициализация свойств файла."""
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner

    def _check_(self):
        # Тут должны быть разные проверки атрибутов
        raise NotImplementedError

    def read(self):
        # Чтение файла
        raise NotImplementedError

    def write(self, data):
        # Создание или перезапись файла
        raise NotImplementedError

    def udpate(self, name, size, creation_date, owner, **kwargs):
        #Обновление аттрибутов файла
        raise NotImplementedError



class   AudioFile(MediaFile):
    """Класс для работы с аудиофайлами, наследник MediaFile."""

    def __init__(self, name, size, creation_date, owner, **kwargs):
        """Инициализация свойств файла с проверкой для данного типа.
        В **kwargs передаются дополнительные атрибуты для каждого типа """
        super.__init__(name, size, creation_date, owner  )
        self.kwargs = kwargs
        self._check_()

    def _check_(self):
        #Тут должны быть разные проверки атрибутов аудиофайлов, например, возможные типы и другие. "
        pass

    def read(self):
        #Чтение файла
        pass

    def write(self, data):
        # Создание или перезапись файла
        pass

    def udpate(self, name, size, creation_date, owner, **kwargs):
        # Обновление аттрибутов файла
        pass



class   VideoFile(MediaFile):
    """Класс для работы с видеофайлами, наследник MediaFile."""

    def __init__(self, name, size, creation_date, owner, **kwargs):
        """Инициализация свойств файла с проверкой для данного типа.
        В **kwargs передаются дополнительные атрибуты для каждого типа """
        super.__init__(name, size, creation_date, owner  )
        self.kwargs = kwargs
        self._check_()

    def _check_(self):
        #Тут должны быть разные проверки атрибутов видеофайлов, например, возможные типы и другие. "
        pass

    def read(self):
        # Чтение файла
        pass

    def write(self, data):
        # Создание или перезапись файла
        pass

    def udpate(self, name, size, creation_date, owner, **kwargs):
        # Обновление аттрибутов файла
        self._check_()



class   ImageFile(MediaFile):
    """Класс для работы с изображениями, наследник MediaFile."""

    def __init__(self, name, size, creation_date, owner, **kwargs):
        """Инициализация свойств файла с проверкой для данного типа
        В **kwargs передаются дополнительные атрибуты для каждого типа """
        super.__init__(name, size, creation_date, owner  )
        self.kwargs = kwargs
        self._check_()

    def _check_(self):
        # Тут должны быть разные проверки атрибутов картинок, например, возможные типы и другие. "
        pass

    def read(self):
        # Чтение файла
        pass

    def write(self, data):
        # Создание или перезапись файла
        pass

    def udpate(self, name, size, creation_date, owner, **kwargs):
        # Обновление аттрибутов файла.
        self._check_()