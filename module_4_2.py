def test_function():
    def inner_function():
        print('Я')
    inner_function()


test_function()
inner_function() # функция находится только в области видимости функции test_function