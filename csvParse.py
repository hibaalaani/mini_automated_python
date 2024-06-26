import csv
# with open ("names.csv", "r") as csv_file: # with is from content manager
#     csv_reader = csv.reader(csv_file)

#     with open("new_names.csv","w")as new_file:
#          csv_writer = csv.writer(new_file , delimiter='\t') 

#          for line in csv_reader:
#               csv_writer.writerow(line)
#     with open ("new_names.csv") as new_file:
#          for line in new_file:
#               print(line)          
     #  next(csv_reader)   to step over the first line
       
# with open ("new_names.csv", "r") as csv_file: # with is from content manager
#     csv_reader = csv.reader(csv_file , delimiter='\t')
#     for line in csv_reader:
#       print(line)
              
            #   better way is to use the dictionary
with open('names.csv', 'r', newline='') as file_reader:
    csv_reader = csv.DictReader(file_reader)

    with open ("names_new2.csv","w",newline='') as file_writer:
     fieldnames = ["name", "age","city"]
     csv_writer = csv.DictWriter(file_writer , fieldnames=fieldnames , delimiter='\t')
     csv_writer.writeheader()
     for line in csv_reader:
        # del line['name'] if you want to delete the name and not include that field
        csv_writer.writerow(line)