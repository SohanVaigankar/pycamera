import cv2

cam = cv2.VideoCapture(0)   #specifying the camera one wants to use 0 --> n (depending on how many cameras one has)

# cv2.namedWindow("Camera") #   IDK why exactly this is needed

img_counter = 0

# keep displaying camera on screen until a key is pressed
while True:
    ret, frame = cam.read() #gettinng a frame from videocapture device, or 'ret'(return) False if not able to capture
    if not ret:
        print('Failed to grab a frame :(')
        break
    
    cv2.imshow('Camera', frame)  #displaying camera window
    
    key = cv2.waitKey(1) # takes a keypress as input every millisecond
    
    # To close the camera press `ESCAPE`
    if key%256 == 27:   # converting `key` to ASCII value and checking if it matches with required ASCII
        print("Closing...")
        break
    
    # To capture the picture press 'SPACE'
    elif key%256 == 32:
        img_name = "test_img_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)    # writing image to specified file
        print("{} written!".format(img_name))
        img_counter += 1


cam.release # dis-engages camera device 
cv2.destroyAllWindows() # closes all the windows created during the process