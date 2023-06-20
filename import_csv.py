import csv
from db import drums, collection, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()


scv_file = '.csv'

with open(scv_file, mode ='r') as file:
  # reading the CSV file
  csvFile = csv.DictReader(file)
  # displaying the contents of the CSV file
  for lines in csvFile:

      ins = collection(artist = lines['Artist'], label = lines["Label"], album = lines["Title"], year = lines["Released"], release_id = lines["release_id"])
      session.add(ins)
      session.commit()
#print(lines)
