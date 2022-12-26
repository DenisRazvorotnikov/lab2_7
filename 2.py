#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Все согл
    a = set("bcdfghilkmnpqrstvwxz")
    mark = set(".?,!:;'`\" ")

    # Ввод строки
    x = set(input("Введите строку: ").lower())

    # Находим все гласные в строке
    gl = x.difference(a)
    gl = gl.difference(mark)

    count = len(gl)

    print(f"Все гласные буквы из введнной строки: = {gl}")
    print(f"Кол-во гласных букв: = {count}")
