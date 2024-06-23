class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price

    def del_item(self, item_name):
        if self.items[item_name]:
            del self.items[item_name]

    def item_price(self, item_name):
        return self.items.get(item_name,None)

    def update_price_item(self, item_name,new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def print_store(self):
        print(self.name)
        print(self.address)
        print('________________________________')
        print('Прейскурант:')
        print('________________________________')
        for item, price in self.items.items():
            print(f'{item} - {price} руб.')


#Универсальный список товаров
items_dict = {'Яблоки':120, 'Бананы':107, 'Апельсины':150, 'Персики':250, 'Груши':200}
def main():
# Создание объектов класса 'Store'
    store_moscow = Store('Филиал "Москва"', 'г. Москва, ул. Тверская, д.1 ')
    store_chimki = Store('Филиал "Химки"', 'Московская обл., г. Химки, ул. Маяковского д.1.')
    store_dolg = Store('Филиал "Долгопрудный"','Московская обл., г. Долгопрудный, пр-т Пацаева д.1')
    store_zelenograd = Store('Филиал "Зеленоград"', 'Московская обл., г. Зеленоград, кв-л 1234, д.32')
# Заполнение списка товаров в созданных объектах
    for item, price in items_dict.items():
        store_moscow.add_item(item, price)
        store_chimki.add_item(item, price)
        store_dolg.add_item(item, price)
        store_zelenograd.add_item(item, price)
# Просмотр объекта store_chimki:
    store_chimki.print_store()
# Добавление довара в список объекта store_chimki:
    store_chimki.add_item('Клубника', '500')
# Просмотр изменненого объекта
    store_chimki.print_store()
# Изменение цены:
    store_chimki.update_price_item('Апельсины', 300)
    store_chimki.print_store()
# Удаление товара
    store_chimki.del_item('Яблоки')
    store_chimki.print_store()
# Запрос цены - товар есть в списке
    print('____________________________________')
    item_price= store_chimki.item_price('Клубника')
    print(f'Цена клубники  - {item_price}')
# Запрос цены - товара нет в списке
    print('____________________________________')
    item_price= store_chimki.item_price('Малина')
    print(f'Цена малины  - {item_price}')

if __name__ == '__main__':
    main()
