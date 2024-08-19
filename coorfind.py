import cv2 

cam = cv2.VideoCapture("./demo/test_xe_o_to_l.mp4") 
while(True): 
    ret,frame = cam.read() 
    if ret:  
        break 
cv2.imshow('image', frame) 

def click_event(event, x, y, flags, params): 
    if event == cv2.EVENT_LBUTTONDOWN: 
        print(x, ' ', y) 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(frame, str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (255, 0, 0), 2) 
        cv2.imshow('image', frame) 
  

cv2.setMouseCallback('image', click_event) 

# wait for a key to be pressed to exit 
cv2.waitKey(0) 

# close the window 
cv2.destroyAllWindows() 