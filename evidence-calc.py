'''This module takes multi-year reports from Evidence.com and calculates size of data uploaded.
Able to set filters by date range.
Note Evidence.com dates are not correctly formatted by default for CSV and must be edited
to remove time from date. I may add functionality to automatically do that in this code
but for now, I did it in Excel with find/replace.'''

import csv
import re

def calc_data(filename, start_date, end_date):

    filename = re.sub(r'\.[^.]*$|^', '', filename)
    filename += '.csv'
    
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        column_index = 15
        column_values = []
        for row in reader:
            try:
                date = row[6]
                if start_date <= date <= end_date:
                    value = float(row[column_index])
                    column_values.append(value)
            except ValueError:
                pass

            column_mb = sum(column_values)
            num_files = len(column_values)
            column_sum = column_mb / 1024
    
    return column_sum, num_files

def main():
    filename = input("Enter the filename: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    column_sum, num_files = calc_data(filename, start_date, end_date)
    print("Total data uploaded in GB: ", column_sum)
    print("Total files: ", num_files)

if __name__ == '__main__':
    main()