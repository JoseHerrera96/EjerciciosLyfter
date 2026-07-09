import csv
from typing import Any

def read_csv_memory(path):
    students = {}
    headers = ["section", "spanish", "english", "history", "science"]
    try:
        with open(path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'Name' not in row:
                    raise KeyError("CSV is missing required 'Name' column")
                name = row.pop('Name')
                students[name] = row
            if reader.fieldnames:
                headers = [h for h in reader.fieldnames if h != 'Name']
    except FileNotFoundError:
        pass
    except KeyError as e:
        print(f"Error reading CSV file: {e}")
    except PermissionError:
        print(f"Error: Permission denied when trying to read file {path}")
    except csv.Error as e:
        print(f"Error parsing CSV file: {e}")
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
    return students, headers

def write_csv_memory(path, students, headers):
    # Define base columns in desired order
    base_columns = ["section", "spanish", "english", "history", "science"]
    
    # Collect all unique keys from student data
    all_keys = set()
    for data in students.values():
        all_keys.update(data.keys())
    
    # Build ordered column list: start with base columns, then add any extra keys, then average_score at the en
    ordered_columns = []
    # Add base columns that exist in our data
    for col in base_columns:
        if col in all_keys:
            ordered_columns.append(col)
            all_keys.remove(col)
    
    # Add any remaining columns except average_score
    for col in all_keys:
        if col != "average_score":
            ordered_columns.append(col)
    
    # Add average_score at the end if it exists
    if "average_score" in all_keys or any("average_score" in data for data in students.values()):
        ordered_columns.append("average_score")
    
    fieldnames = ['Name'] + ordered_columns
    
    try:
        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            for name, data in students.items():
                row = data.copy()
                row['Name'] = name
                writer.writerow(row)
    except PermissionError:
        print(f"Error: Permission denied when trying to write to file {path}")
    except TypeError as e:
        print(f"Error formatting data for CSV: {e}")
    except csv.Error as e:
        print(f"Error writing CSV file: {e}")
    except Exception as e:
        print(f"Unexpected error writing file: {e}")
