#Задача #1,2

from pprint import pprint
from typing import Counter

cook_book = {}

def get_data(file_name):
    

    with open(file_name, encoding='utf8')as file:
        for line in file:
            dish = line.strip()
            counter = int(file.readline())
            tmp_arr = []
            for i in range(counter):
                ingredient_name, quantity, measure  = file.readline().split('|')
                tmp_arr.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            
            cook_book[dish] = tmp_arr
            file.readline()
    return cook_book

get_data('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count):
    ret_obj = {}
    for dish in dishes:
        for item in cook_book[dish]:
            tmp_obj = dict(item)
            tmp_obj['quantity'] = int(tmp_obj['quantity']) * person_count
            if tmp_obj['ingredient_name'] not in ret_obj:
                 ret_obj[tmp_obj['ingredient_name']] = tmp_obj
            else:
                ret_obj[tmp_obj['ingredient_name']]['quantity'] += tmp_obj['quantity']

    return ret_obj


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
# pprint(get_data('recipes.txt'))

#Задача #3


def take_content(file_name_1, file_name_2,file_name_3, result):
    
    
    def write_file(file_name, node, encode, counter=0):
        
        with open(file_name)as file:
            str_arr = []
            for line in file:
              str_file = line.strip().replace(' ', '')
              counter += 1
              str_arr.append(f' строка номер {counter} файла {file_name}: {str_file}')

            with open(result, f'{node}', encoding=f'{encode}' ) as out_file:
                out_file.write(f'{file_name}\n')
                out_file.write(f'{counter}\n')

            with open(result, f'{node}', encoding=f'{encode}' ) as out_file:
                for i in str_arr:
                    out_file.write(f'{i}\n')

    write_file(file_name_2, 'a', 'cp1251')
    write_file(file_name_1, 'a', 'cp1251')
    write_file(file_name_3, 'a', 'cp1251')
    



   
take_content('1.txt','2.txt','3.txt', 'result.txt')





            


        
    














