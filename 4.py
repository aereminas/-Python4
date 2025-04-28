def trace_function_execution(original_function):
    def wrapped(*args, **named_args):
        print(f"Запуск функции {original_function.__name__} со следующими данными:")
        print(f"Позиционные параметры: {args}")
        print(f"Именованные параметры: {named_args}")
        outcome = original_function(*args, **named_args)
        return outcome

    return wrapped

@trace_function_execution
def rectangle_area(side1, side2):
    rectangle_area_value = side1 * side2
    print(f"Значение площади прямоугольника: {rectangle_area_value}")
    return rectangle_area_value


rectangle_area(4, 8)
rectangle_area(side1=6, side2=2)

