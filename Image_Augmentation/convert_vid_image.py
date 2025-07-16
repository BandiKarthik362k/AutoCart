import cv2

print('hello')
video_path = 'E:/shop/Images/videos'

dest = 'E:/shop/Images/images/dual_images/'

videos_num= [5,6]
image_num = 0
for i in videos_num:
    video = cv2.VideoCapture(video_path + '/' + str(i) + '.MOV')

    while True:
        a, frames = video.read()
        if  not a:
            break
        if image_num%25==0:
            frames = cv2.rotate(frames,cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(dest+str(image_num)+'.jpg',frames)
        image_num = image_num+1
   
#         # if cv2.waitKey(30) == ord('q'): 
#         #     video.release()
#         #     cv2.destroyAllWindows()
#         #     exit()