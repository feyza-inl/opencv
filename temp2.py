# %% kenar algılama 

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\user\Desktop\london.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()

# herhangı bır threshold uygulamadan yaptık bunu 
kenar = cv2.Canny(image =img,threshold1=0, threshold2=255)
plt.figure()
plt.imshow(kenar,cmap="gray")
plt.axis("off")
plt.show()

# ortalama medyan yontemı
medyan = np.median(img)
print(medyan)
low = int(max(0,(1-0.33)*medyan)) #alt treshold
high = int(min(255,(1+0.33)*medyan)) # ust treshold

kenar2 = cv2.Canny(image =img,threshold1=low, threshold2=high)
plt.figure()
plt.imshow(kenar2,cmap="gray")
plt.axis("off")
plt.show()

# bluring ve ortamala kenar bulma yontemi 
blur_img =cv2.blur(img, ksize=(5,5))
plt.figure()
plt.imshow(blur_img,cmap="gray")
plt.axis("off")
plt.show()


medyan2 =np.median(blur_img)

low=int(max(0,(1-0.33)*medyan2))
high =int(min(255,(1+0.33)*medyan2))

kenarlar = cv2.Canny(blur_img, threshold1=low, threshold2=high)
plt.figure()
plt.imshow(kenarlar,cmap="gray")
plt.axis("off")
plt.show()

# %% koşe algılama

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\user\Desktop\sudoku.jpg",0)
img = np.float32(img)
print(img.shape)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")

# harris corner detection kose algılayacagız
dst =cv2.cornerHarris(src=img, blockSize = 2, ksize=3, k=0.04)
plt.figure()
plt.imshow(dst,cmap="gray")
plt.axis("off")

# gorsellestırelım
dst = cv2.dilate(dst,None) # genişletme yaptık
img[dst>0.2*dst.max()] = 1
plt.figure()
plt.imshow(dst,cmap="gray")
plt.axis("off")

# shi tomasi desction ile köşe bulacagiz bunda hız tespıt edecegımız kose adedını belırlıyoruz
img2 = cv2.imread(r"C:\Users\user\Desktop\sudoku.jpg",0)
img2 =np.float32(img2)
köse = cv2.goodFeaturesToTrack(image=img2, maxCorners=100, qualityLevel=0.01, minDistance=10)
köse = np.int64(köse)

for i in köse:
    x,y = i.ravel()
    cv2.circle(img2, (x,y),3,(125,125,125), cv2.FILLED)
    
plt.imshow(img2)
plt.axis("off")

# %% kontur algılama

import matplotlib.pyplot as plt
import cv2
import numpy as np


img = cv2.imread(r"C:\Users\user\Desktop\contour.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")


# mode = internal yada extarnela yada ıc kontur ve dıs kontur bulmak ıstıorum dıyorum
cont,hierarch = cv2.findContours(image=img, mode = cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)

extranel_contur = np.zeros(img.shape)
internal_contur = np.zeros(img.shape)

for i in range(len(cont)):
    
    # extarnel anlamına gelır = hierarch[0][i][3]
    if hierarch[0][i][3] == -1:
        cv2.drawContours(extranel_contur, cont, i, 200,-1)

    else:
        cv2.drawContours(internal_contur, cont, i, 200,-1)

plt.figure()
plt.imshow(extranel_contur,cmap="gray")
plt.axis("off")   

plt.figure()
plt.imshow(internal_contur,cmap="gray")
plt.axis("off") 
 