import dropbox
import time
import random
import cv2
start_time=time.time()
def takes_snapshot():
    number=random.randint(0,100)
#initializing cv2
    videocaptureobject=cv2.VideoCapture(0)

    result=True

    while(result):
#Read frames while the camera is on
        ret,frame=videocaptureobject.read()

#write the image to any storage device
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time 
        result=False
    return img_name
    print("snapshot taken")
#Close the webcam
    videocaptureobject.release()
#Close all the windows that might be open in this process
    cv2.destroyAllWindows()

def upload_file(img_name): 
    access_token='sl.A_LOXKzkJBwWZX6IPJFCDhX1bNmGU1FFEPT-ZU4e-4NzSy_hNQfnaKy2l1nM7Iz4VNzsSLQapRmBjgRXEjw2wOokAexbeXORNwK8irDkQMjTYA6Ua2yzmxHiHxoHnTItUiqW9U4'
    file =img_name 
    file_from = file 
    file_to="/testFolder/"+(img_name) 
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = takes_snapshot() 
            upload_file(name) 
            
main()

