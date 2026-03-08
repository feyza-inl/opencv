import cv2
import mediapipe as mp
import time

# satatic_image_mode el sayisi parametresi
# multi_hand_landmarks = elın kordınatlarını verıyor 

cap = cv2.VideoCapture(0)

el = mp.solutions.hands
eller = el.Hands(static_image_mode=1)

elcizme =mp.solutions.drawing_utils

pTime = 0
cTime = 0

if cap.isOpened() == False:
    print("Hata Acilamadaı Kamera")
    
while True:
    ret,frame = cap.read()
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    result = eller.process(framergb)
    print(result.multi_hand_landmarks)
    
    if result.multi_hand_landmarks:
        for ellms in result.multi_hand_landmarks:
          elcizme.draw_landmarks(frame,ellms,el.HAND_CONNECTIONS)  
          for id,lm in enumerate(ellms.landmark): 
              #print(id,lm)
              h,w,c =frame.shape
              cx,cy = int(lm.x *w),int(lm.y*h)
              
              # bilek İD = 0
              if id == 0:
                  cv2.circle(frame,(cx,cy),9,(255,0,0),cv2.FILLED)
        
    #fps hesaplayalım
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(frame, "FPS:"+str(int(fps)), (70,20), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0),)
    
    cv2.imshow("Frame",frame)
    
    if cv2.waitKey(0) &0xFF == ord("q"):
        break    
    
cap.release()
cv2.destroyAllWindows()    
    