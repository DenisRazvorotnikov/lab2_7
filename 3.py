#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__== " main ":
    # Ввод строки
    x1 = set(input("Введите первую строку: ").lower())
    x2 = set(input("Введите вторую строку: ").lower())

    mark = set(".?,!:;'`\" ")

    gl = x1.intersection(x2)
    gl = gl.difference(mark)

    count = len(gl)

    print(f"Общие символы: = {gl}")
    print(f"Кол-во общих символов: = {count}")
