import  os
import cv2
def show_img(img_name,img_label):
    img=cv2.imread(img_name)
    W,H=img.shape[0],img.shape[1]
    with open (img_label , 'r') as file :
        for line in file.readlines () :
            str_split=line.split()
            x_loc,y_loc=float(str_split[1]),float(str_split[2])
            w,h=(float)(str_split[3]),(float)(str_split[4])
            x_center=(float)(x_loc)*W
            y_center=(float)(y_loc)*H
            rec_w,rec_h=W*w,H*h
            x1,y1=int(x_center-rec_w/2),int(y_center-rec_h/2)
            x2,y2=int(x_center+rec_w/2),int(y_center+rec_h/2)
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
    file.close()
    tmp='output\\'+img_name.split('\\')[-1]
    cv2.imwrite(tmp,img)
import os
rootdir = 'train/images'
length=len(os.listdir(rootdir))

for  filename in os.listdir(rootdir):
    img_name=os.path.join(rootdir,filename)
    label_name='train/labels/'+filename.split('.')[0]+'.txt'
    show_img(img_name,label_name)
    print(length)
    length-=1



















