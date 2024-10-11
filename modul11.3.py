def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = dir(obj)

    # Получаем методы объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Получаем модуль, к которому принадлежит объект
    module = getattr(obj.__class__, '__module__', 'builtins')

    # Собираем данные в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


# Пример создания класса и объекта
class MyClass:
    def __init__(self):
        self.attribute_one = "Hello"

    def my_method(self):
        return "This is a method."


# Создание объекта класса
my_object = MyClass()

# Использование функции introspection_info
object_info = introspection_info(my_object)
print(object_info)

# Пример с числом
number_info = introspection_info(42)
print(number_info)