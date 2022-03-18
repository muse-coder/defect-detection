import  os
root_dir='output'
file_types=['crazing','inclusion','patches','pitted','rolled','scratches']
# os.mkdir('data_img')
# for types in file_types:
#     os.mkdir('data_img/'+types)
length=len(os.listdir(root_dir))
for file_name in os.listdir(root_dir):
    print(length)
    length-=1
    for types in file_types:
        if file_name.startswith(types):
            os.rename(os.path.join(root_dir,file_name),'data_img/'+types+'/'+file_name)
            break
