# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for target_item in ['банан', 'груша', 'персик']:
    result = items_list.index(target_item)  # TODO Вызовите функцию, что получить индекс товара
    if result is not None:
        print(f"Первое вхождение товара '{target_item}' имеет индекс {result}.")
    else:
        print(f"Товар '{target_item}' не найден в списке.")
