# %% resmi içeri aktarma

import cv2

img = cv2.imread(r"C:\Users\user\Desktop\gi1.webp",0) # resmı sıyah beyaz formatta okuduk
cv2.imshow("ilk resim gorsellestırme",img) # gorsellestırme

k = cv2.waitKey(0) &0xFF

if k == ord("s"):
    cv2.imwrite("ilk_deneme.jpg",img) 
    cv2.destroyAllWindows()
elif k==ord("q"):
    cv2.destroyAllWindows()
    
# %%  video içeri aktarma 

import cv2
import time

cap = cv2.VideoCapture(r"C:\Users\user\Desktop\line.avi")# videoyu içeri aktardık

if cap.isOpened() == False:# videoyu duzgun aktardıkmı kontrol
    print("Hata aktarmada sorun var.")

while True:
    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(0.01)
        cv2.imshow("Ilk Video",frame)
    else:
        break
    if cv2.waitKey(1) &0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()    


#%% Kamera Açma ve Video Kaydı

import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Hata kamera açılmasında hata var.")
    
widht =  int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   
hight =  int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter("ilk_video.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(widht,hight))

while True:
    ret, frame = cap.read()
    cv2.imshow("Video",frame) 
    writer.write(frame)

        
    if cv2.waitKey(1) &0xFF == ord("q"): break    

cap.realease()
writer.release()
cv2.destroyAllWindows()


# %% yeniden boyutlandırma ve kırpma

import cv2

img = cv2.imread(r"C:\Users\user\Desktop\ali.jpeg")
print("Resim Boyutu: ",img.shape)

cv2.imshow("Siyah Beyaz",img)

img_resize = cv2.resize(img,(800,800))
print("Yeniden Boyutlandırılmıs versiyon boyutu:",img_resize.shape)

cv2.imshow("Yeniden Buyotlandırılmıs",img_resize)

# kırpma işlemi

kırpılmıs = img[:200,0:300]
cv2.imshow("Kırpık Resim",kırpılmıs) 

# %% Sekıller ve Metınler ekleme gorsele yada vıdeoya

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # siyah bir resim
print("Boyutlari: ",img.shape)
# cizgi cizelim

#line(resim,baslagıc noktasi,bitiş noktasi,renk(bgr), kalınlık)

cv2.line(img,(0,0),(512,512),(0,255,0),1)

# dıkdortgen cizelim
#rectangle(resim,baslangıc noktası,bıtıs noktası, renk bgr)
cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED)

# CEMBER
# circle(resim,merkez,yarıcap,renk)
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED)

#METİN 
#(resim,yazı,baslangıc noktası,font,kalınlık,renk)
cv2.putText(img,"Ben Feyza",(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))

cv2.imshow("Siyah",img)

# %% görüntü birleştirme

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\user\Desktop\ali.jpeg")
print("Boyutları: ",img.shape)

img_yeniden_boyut = cv2.resize(img,(100,100))

# yatay birlestirme
hor = np.hstack((img_yeniden_boyut,img_yeniden_boyut)) 

# dikey birleştirme
ver = np.vstack((img_yeniden_boyut,img_yeniden_boyut))

cv2.putText(img,"Feyzaya Çiçek",(10,10),cv2.FONT_HERSHEY_COMPLEX,1,[0,0,0])

cv2.imshow("Resim Birleştirme",img)

if cv2.waitKey(0) &0xFF == ord("q"):
    cv2.destroyAllWindows()


#%% perspektıf carpıtma

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\user\Desktop\kart.png")
cv2.imshow("Orijinal",img)

widht = 400
height = 500

kart1 = np.float32([[230,1],[1,472],[540,150],[338,617]])
kart_varsayilan = np.float32([[0,0],[0,height],[widht,0],[widht,height]])

matrix = cv2.getPerspectiveTransform(kart1, kart_varsayilan)
print(matrix)

# nihai donusturulmus resım
imgOutput = cv2.warpPerspective(img,matrix,(widht,height)) 
cv2.imshow("Nihai ",imgOutput)


if cv2.waitKey(0) &0xFF == ord("q"):
    cv2.destroyAllWindows()
    
# %% goruntulerı bırbırıyle karıstırmak

import cv2
import matplotlib.pyplot as plt

#karıstırma
img1 = cv2.imread(r"C:\Users\user\Desktop\img1.JPG")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.imread(r"C:\Users\user\Desktop\img2.JPG")
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

img1  = cv2.resize(img1,(600,600))
print(img1.shape)

img2 = cv2.resize(img2,(600,600))
print(img2.shape)

# karıstırılmıs resım = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2 =img2, beta =0.5, gamma=0)
plt.figure()
plt.imshow(blended)


# %% goruntu eşikleme 

import cv2
import matplotlib.pyplot as plt

# resmi içe aktar
img = cv2.imread(r"C:\Users\user\Desktop\img1.JPG")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()

# esikleme yapacagız

_, thresh_img = cv2.threshold(img, thresh=60, maxval = 255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img,cmap="gray")
plt.axis("off")
plt.show()

# adaptıf threshold(uyarlamalı eşık degeri)
thresh_img2 = cv2.adaptiveThreshold(img, maxValue =255, adaptiveMethod = cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=8)
plt.figure()
plt.imshow(thresh_img2,cmap="gray")
plt.axis("off")

# %% BULANIKLASTIRMA 
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\user\Desktop\NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #OpenCV BGR formatında okur, ama matplotlib RGB bekler
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("orijinal")
plt.show()

# Ortalama bulanıklaştırma yöntemi
dst2 = cv2.blur(src=img, ksize=(3, 3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("ortalama bulanık")
plt.show()

# Gauss blur yöntemi
gb = cv2.GaussianBlur(src=img, ksize=(3, 3), sigmaX=7)
plt.figure()
plt.imshow(gb) 
plt.axis("off")
plt.title("gauss blur")
plt.show()

# Median blur ile bulanıklaştırma
mb = cv2.medianBlur(src=img, ksize=3)  # ksize tek sayı olmalı (tuple değil)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("median blur")
plt.show()

def gaussianNoise(image):
    row, col, kanal = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, kanal))
    gauss = gauss.reshape(row, col, kanal)
    noisy = image + gauss
    return noisy

# Gürültüyü ekleyebilmemiz için 0-255 arası değerleri 0-1 arasına taşıyacağız
img = cv2.imread(r"C:\Users\user\Desktop\NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255  # HATA: cv2.cv2 yerine cv2
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("orijinal")
plt.show()

gauss_noise_image = gaussianNoise(img)  # HATA: goauss yerine gauss (typo)
plt.figure()
plt.imshow(gauss_noise_image)
plt.axis("off")
plt.title("gaussnoisy")
plt.show()


# tuz karabıber goruntusu eklıycegız
def saltPaperNoise(image):
    row,col,kanal = image.shape
    s_vs_p = 0.5
    amount = 0.004
    
    noisy = np.copy(image)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords] = 1

    num_paper = np.ceil(amount * image.size *(1- s_vs_p))
    coords = [np.random.randint(0,i-1,int(num_paper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy


sp_image=saltPaperNoise(img)
plt.figure()
plt.imshow(gauss_noise_image)
plt.axis("off")
plt.title("sat-paper")
plt.show()

# %% marfolojık işlemler

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\user\Desktop\datai_team.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off") 
plt.title("Orjinal Resim")

# erezyon işlemi
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel,iterations=1)
plt.figure()
plt.imshow(result,cmap="gray")
plt.axis("off") 
plt.title("Erezyon")

# genişleme 

result2 = cv2.dilate((img), kernel,iterations=1)
plt.figure()
plt.imshow(result2,cmap="gray")
plt.axis("off") 
plt.title("Genişleme")


# açilma  = beyaz gurultuyu azaltmak ıcın uygularız
beyaz_gurultu = np.random.normal(0,2, size=img.shape[:2])
beyaz_gurultu = beyaz_gurultu*255
plt.figure()
plt.imshow(beyaz_gurultu,cmap="gray")
plt.axis("off") 
plt.title("Beyaz Gurultu")

noise_img = beyaz_gurultu+img
plt.figure()
plt.imshow(noise_img,cmap="gray")
plt.axis("off") 
plt.title("Beyaz Gurultulu Resim")


# acılma

openning=cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(openning,cmap="gray")
plt.axis("off") 
plt.title("Açılmıs Resim")


#kapatma sıyah noise gıderılır
siyah_gurultu = np.random.normal(0,2, size=img.shape[:2])
siyah_gurultu = siyah_gurultu*-255
plt.figure()
plt.imshow(siyah_gurultu,cmap="gray")
plt.axis("off") 
plt.title("siyah Gurultu")


siyah_gurultu_img = siyah_gurultu+img
siyah_gurultu_img[siyah_gurultu_img <= -245] = 0
plt.figure()
plt.imshow(siyah_gurultu_img,cmap="gray")
plt.axis("off") 
plt.title("siyah Gurultu")

# kapatma
closing = cv2.morphologyEx(siyah_gurultu_img.astype(np.float32),cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(closing,cmap="gray")
plt.axis("off") 
plt.title("siyah Gurultu")

# gradyan

gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient,cmap="gray")
plt.axis("off") 
plt.title("Gradyan")

# %% gradyan
 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\user\Desktop\sudoku.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()

# x gradyan x ekseni
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx=1, dy=0,ksize=5)
plt.figure()
plt.imshow(sobelx,cmap="gray")
plt.axis("off")
plt.show()

# y gardyan y ekseni
sobely = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure()
plt.imshow(sobely,cmap="gray")
plt.axis("off")
plt.show()

# yukarıda ayrı ayrı tespıt ettık 
# ben ikisini de aynı anda tespıt etmek ıstersek laplacian gradyan kullanmalıyız

# lablacian

lablacia= cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure()
plt.imshow(lablacia,cmap="gray")
plt.axis("off")
plt.show()

# %% histogram

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\user\Desktop\red_blue.jpg")
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img_rgb)

print(img.shape)

img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize = [256], ranges=[0,256])

print(img_hist.shape)
plt.figure()
plt.plot(img_hist)

# renk ayrımı yapalım

color = ("b","g","r")
plt.figure()
for i,c in enumerate(color):
    hist = cv2.calcHist([img], channels=[i], mask=None, histSize = [256], ranges=[0,256])
    plt.plot(hist,color = c)


# maskeleme de yapacagız burada
golden_gate = cv2.imread(r"C:\Users\user\Desktop\goldenGate.jpg")
golden_gate_rgb = cv2.cvtColor(golden_gate,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(golden_gate_rgb)

print(golden_gate_rgb.shape)

mask = np.zeros(golden_gate.shape[:2],np.uint8)
plt.figure()
plt.imshow(mask, cmap="gray")

mask[1500:2000, 1000:2000]= 255
mask_image = cv2.bitwise_and(golden_gate_rgb, golden_gate_rgb,mask = mask) 
plt.figure()
plt.imshow(mask_image)


masked_img = cv2.bitwise_and(golden_gate,golden_gate, mask=mask)
masked_img_hist = cv2.calcHist([golden_gate], channels = [0], mask = mask, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(masked_img_hist)

# hıstogram eşitleme = kontrastı arttırmaya calısıyoruz
img = cv2.imread(r"C:\Users\user\Desktop\hist_equ.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")

img_hist = cv2.calcHist([img], channels = [0], mask=None, histSize=[256], ranges=[0,256])
plt.figure()
plt.plot(img_hist)

eq_hist = cv2.equalizeHist(img)
plt.figure()
plt.imshow(eq_hist,cmap="gray")
# renklerın arasını actım koyu renklerı 0 a cektım acıkları 255 e

# %% hocanın odevi opencv kısmı sonu
# opencv kütüphanesini içe aktaralım
import cv2

# matplotlib kütüphanesini içe aktaralım
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak içe aktaralım
img = cv2.imread(r"C:\Users\user\Desktop\odev1.jpg",0)

# resmi çizdirelim
cv2.imshow("Orjinal",img)

# resmin boyutuna bakalım
print(img.shape)

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
img_resize = cv2.resize(img, dsize = (int(img.shape[1]*4/5),int(img.shape[0]*4/5)))
# orjinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim

yazı =cv2.putText(img=img, text ="This Is At", org=(200,200), fontFace =cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=[255,0,0])
cv2.imshow("Yazı Eklenmış Halı",yazı)

#  orjinal resme 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim

_,thres_img = cv2.threshold(src = img, thresh =50, maxval =255, type = cv2.THRESH_BINARY)
cv2.imshow("Threslenmiş",thres_img)

# orjinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim

blur = cv2.GaussianBlur(src=img ,ksize =(5,5), sigmaX=7)
cv2.imshow("Blurlanmıs",blur)

# orjinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
lap =cv2.Laplacian(src=img, ddepth = cv2.CV_16S)
plt.figure()
plt.imshow(lap,cmap = "gray")
plt.title("Laplacian")
plt.axis("off")

# orhinal resmin histogramını çizdirelim
img_hist = cv2.calcHist(images = [img], channels =[0], mask =None, histSize = [256], ranges=[0,256])
plt.figure()
plt.plot(img_hist)


if cv2.waitKey(0) &0xFF == ord("q"):
    cv2.destroyAllWindows()


 