def tes_function ():
    def inner_function ():
        print('Я в области видимости функции tes_function')

    inner_function()

tes_function()
# inner_function() - имя функции только в локальном пространстве функции tes_function