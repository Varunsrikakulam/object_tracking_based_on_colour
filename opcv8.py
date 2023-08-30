import cv2
import imutils
vs = cv2.VideoCapture(0)
orangelowervalue=(5, 50, 50)
orangeuppervalue=(15, 255, 255)
while True:
    grabbed,img = vs.read()
    resize = imutils.resize(img,width=600)
    gauss = cv2.GaussianBlur(resize,(11,11),0)
    grayimage = cv2.cvtColor(gauss,cv2.COLOR_BGR2HSV)
    gud = cv2.inRange(grayimage,orangelowervalue,orangeuppervalue)
    res = cv2.erode(gud,None,iterations = 2)
    res = cv2.dilate(res,None,iterations=2)
    cnts = cv2.findContours(res.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) [-2]
    center =None
    if len(cnts)>0:
        c = max(cnts,key = cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if radius>10:
            cv2.circle(img,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(img,center,5,(0,0,255),-1)
            if radius >250:
                print("stop")
            else:
                if(center[0]<150):
                    print("left")
                elif(center[0]>450):
                    print("right")
                elif(radius<250):
                    print("Front")
                else:
                    print("stop")
    cv2.imshow("Colour detection",img)
    key = cv2.waitKey(10)
    if(key == 27):
        break
vs.release()
cv2.destroyAllWindows()

