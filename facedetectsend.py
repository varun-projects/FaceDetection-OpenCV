import os, sys, time ,cv2
import cv
minSize = (20, 20)
imageScale = 2
haarScale = 1.1
minNeighbors = 3
haarFlags = cv.CV_HAAR_DO_CANNY_PRUNING
    
   
def detectFace(img ,cascade):
    
    gray=cv.CreateImage((img.width,img.height),8,1)
    small_img=cv.CreateImage((cv.Round(img.width/imageScale),cv.Round(img.height/imageScale)),8,1)
    cv.CvtColor(img,gray,cv.CV_BGR2GRAY)
    cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)
    cv.EqualizeHist(small_img, small_img)
    #faceCascade = cv2.CascadeClassifier(cascade1)
    faces=cv.HaarDetectObjects(small_img,cascade,cv.CreateMemStorage(0),haarScale,minNeighbors,haarFlags,minSize)
    #faces =faceCascade.detectMultiScale(i,1,5,(30,30),cv.CV_HAAR_SCALE_IMAGE)
    print "now it would check if face detected or not"
    if faces :
        print "detected" ,len(faces)
        for ((x, y, w, h), n) in faces:
            pt1=(int(x*imageScale),int(y*imageScale))
            pt2=(int((x+w)*imageScale),int((y+h)*imageScale))
            cv.Rectangle(img,pt1,pt2,cv.RGB(255,0,0),3,8,0)
        return img	
    else:
    		print "no face"
    		return False
    	
    #cdir = "/usr/share/opencv/haarcascades/"
     
    #cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cascade=cv.Load("haarcascade_frontalface_default.xml")
cascade1="haarcascade_frontalface_default.xml"
image = cv.LoadImage("img232.jpg")    # get me the syntax of this    
match = detectFace(image, cascade)
    
if match:
    	cv.SaveImage("myfinalfacefile1.jpg",match)
    	
    	
    
    
    
    	 
    
    
    
    
    
    
    
