#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import argparse


# Добавляем обработку аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputFile", help="--inputFile <FILE> - путь к CSV-файлу", required=True)
parser.add_argument("-n", "--fieldName", help="--fieldName <NAME> - имя столбца (поля)", required=True)  # dataset for example
parser.add_argument("-v", "--fieldValue", help="--fieldValue <VALUE> - значение столбца (поля)", required=True) # Outcomes for example
args = parser.parse_args()


# Функция для чтения и проверки csv файла
def csv_reader(file):
    reader = csv.DictReader(file)
    counter = 0
    for row in reader:
        if args.fieldValue in row[args.fieldName]:
            counter += 1
    print("There is", counter, args.fieldValue, "in", args.fieldName)

try:
    with open(args.inputFile, newline='') as csvfile:
        csv_reader(csvfile)
except:
    print("There is no", args.inputFile)
