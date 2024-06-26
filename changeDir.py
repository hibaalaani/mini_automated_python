import os
os.chdir("F:\\DCI-CLASSES\\DCI_WD21_03_02\\valid_directory_name\\records")
print(os.getcwd())

for f in os.listdir():
         f_name, f_ext = os.path.splitext(f).zfill(2)


         print(f_name )
  
     # print('{}-{}{}'.format(f_tit,f_tit2 , f_ext))
