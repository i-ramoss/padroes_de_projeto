class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls.__create_instance()
        return cls.__instance

    @classmethod
    def __create_instance(cls):
        instance = super().__new__(cls)
        return instance


singleton = Singleton.get_instance()
singleton2 = Singleton.get_instance()

print(id(singleton))
print(id(singleton2))
