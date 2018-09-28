#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputFile", help="--inputFile <FILE> - путь к CSV-файлу", action="store", required=True)
parser.add_argument("-n", "--fieldName", help="--fieldName <NAME> - имя столбца (поля)", required=True)  # dataset for example
parser.add_argument("-v", "--fieldValue", help="--fieldValue <VALUE> - значение столбца (поля)", required=True) # Outcomes for example
args = parser.parse_args()


def csv_reader(file):
    reader = csv.DictReader(file)
    counter = 0
    for row in reader:
        if args.fieldValue in row[args.fieldName]:
            counter += 1
    print(counter)

try:
    with open(args.inputFile, newline='') as csvfile:
        csv_reader(csvfile)
except:
    print("There is no", args.inputFile)
