import csv
from typing import Any
import os

def get_script_dir():
    return os.path.dirname(os.path.abspath(__file__))

def read_csv_memory(path):
    full_path = os.path.join(get_script_dir(), path)
    students = {}
    headers = ["section", "spanish", "english", "history", "science"]
    try:
        with open(full_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'Name' not in row:
                    raise KeyError("CSV is missing required 'Name' column")
                name = row.pop('Name')
                # Convert average_score to float if it exists
                if 'average_score' in row:
                    try:
                        row['average_score'] = float(row['average_score'])
                    except ValueError:
                        pass  # Keep as string if conversion fails
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

def write_csv_memory(path, students):
    full_path = os.path.join(get_script_dir(), path)
    # Define fixed columns in desired order
    ordered_columns = ["section", "spanish", "english", "history", "science", "average_score"]
    
    fieldnames = ['Name'] + ordered_columns
    
    try:
        with open(full_path, 'w', newline='', encoding='utf-8') as csvfile:
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
