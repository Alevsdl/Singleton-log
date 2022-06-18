from cloudMeta import CloudMeta
from firebase import Firebase


class Cloud(metaclass=CloudMeta):
    def __init__(self, filename: str):
        self.__filename = filename
        self.tipo = Firebase(filename)

    def success(self, text: str):
        self.tipo.connection()
        self.tipo.write(self.__filename, text)
        self.tipo.upload(self.__filename)
        return

    def warning(self, text: str):
        self.tipo.connection()
        self.tipo.write(self.__filename, text)
        self.tipo.upload(self.__filename)
        return

    def error(self, text: str):
        self.tipo.connection()
        self.tipo.write(self.__filename, text)
        self.tipo.upload(self.__filename)
        return

    def message(self, text: str):
        self.tipo.connection()
        self.tipo.write(self.__filename, text)
        self.tipo.upload(self.__filename)
        return
