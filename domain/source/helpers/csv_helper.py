import csv

class CSVHelper:
  def __init__(self):
    pass

  @staticmethod
  def get_data_from_file(file_path):
    data = []

    with open(file_path) as file:
      reader = csv.DictReader(file, delimiter=',', quotechar='|')
      headers = reader.fieldnames

      for row in reader:
        item = {}
        for header in headers:
          item[header] = row[header] 

        data.append(item)

    return data