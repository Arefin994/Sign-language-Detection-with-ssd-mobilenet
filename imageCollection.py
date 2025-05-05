import cv2
import os 
import time 
import uuid


img_path = 'workspace/images/collected_images'


labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
num_imgs = 15

for label in labels:
    os.makedirs(os.path.join(img_path, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(5)

    for img_num in range(num_imgs):
        ret, frame = cap.read()
        img_name = os.path.join(img_path, label, f'{label}.{str(uuid.uuid1())}.jpg')
        cv2.imwrite(img_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    print(f'Collected {num_imgs} images for {label}')
