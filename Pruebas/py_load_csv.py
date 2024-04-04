import csv

def load_csv_to_dict(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key, value in row.items():
                if key in data:
                    data[key].append(value)
                else:
                    data[key] = [value]
    return data

# Replace 'file_path' with the actual path to your CSV file
file_path = '/path/to/your/csv/file.csv'
csv_data = load_csv_to_dict(file_path)
print(csv_data)

sorted_keys = sorted(csv_data.keys())
print(sorted_keys)