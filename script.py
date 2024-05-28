import re
import pandas as pd
import os
import csv

date_pattern = r"^\d{2}/\d{2}/\d{4}"

output_file = 'output1.csv'

with open(output_file, 'w', encoding='utf-8') as output:
    with open('input.csv', 'r', encoding='utf-8') as file:
        previous_line = ""
        for line in file:
            
            if not re.match(date_pattern, line):
                previous_line = previous_line.strip() + "$@!" + line.strip()
            else:
                if previous_line:
                    output.write(previous_line + '\n')
                previous_line = line.strip()

            previous_line = previous_line.replace(',', '', 1)

        if previous_line:
            output.write(previous_line + '\n')


input_filename = 'output1.csv'
output_filename = 'output2.csv'

with open(input_filename, 'r', encoding='utf-8') as input_file, open(output_filename, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        line = line.strip() 
        line = line.replace('-', ',' , 1)  
        output_file.write(line + '\n') 

os.remove(input_filename)

with open('output2.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines() 

with open('output3.csv', 'w', encoding='utf-8') as file:
    for line in lines:
        first_dash_index = line.find(':')
        if first_dash_index != -1:
            second_dash_index = line.find(':', first_dash_index + 1)
            if second_dash_index != -1:
                line = line[:second_dash_index] + ',' + line[second_dash_index + 1:] 
        file.write(line)

os.remove('output2.csv')


with open("output3.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

modified_lines = [line.replace(' ', ',', 1) for line in lines]

with open("output.csv", "w", encoding="utf-8") as file:
    file.writelines(modified_lines)


os.remove('output3.csv')

