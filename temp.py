#%% temel python ıslemler
toplam = 10+5
cıkarma = 10-5
carp = 10*5
bol = 10/5

print("Toplam: {} ve fark: {}".format(toplam,cıkarma))
print("carpma: %d ve bolme: %.4f" % (carp, bol))

"""
yorum satırı olusturma
"""
# %% NUMPY LİB

import numpy as np

#1*15 boyutunda bir array dizisi olusturalım
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape) # numpy arrayının boyutu

dizi2 = dizi.reshape(3,5)
print("Sekil: ",dizi2.shape)
print("Boyut: ",dizi2.ndim)  
print("Veri tipi: ",dizi2.dtype.name)
print("Boy: ",dizi2.size)

# array type
print("Type: ",type(dizi2))

#ıkı boyutlu array

dizi2d = np.array([[1,2,3,4],[1,3,4,9],[3,4,5,6]])
print(dizi2d)

# sıfırlardan olusan bır array
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

#birlerden olsuan dızı
birlerde_dizi = np.ones((3,4))
print(birlerde_dizi)

# bos bır dızı
bos_dizi = np.empty((3,4))
print(bos_dizi)


#arrange(x,y,basamak)

dizi_aralik=np.arange(10,50,5)
print(dizi_aralik)

#linspace(x,y,basamak)
dizi_bosluk = np.linspace(10,20,5) # 10 ve 20 arasını 5 e bolmus
print(dizi_bosluk)

#float array
float_array = np.float32([[1.2,2.3],[1.3,4.5]])
print(float_array)

# matematıksel ıslemler
a=np.array([1,2,3])
b=np.array([2,3,4])
print(a+b)
print(a-b)
print(a*b)

# dizi elemanları toplama
print(np.sum(a))

# dizi ıcındekı max deger
print(np.max(a))

# ortalamasına bakma(mean)
print(np.mean(a))

# random degerler olusturma[0,1] arasında olusturalım

rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)


# ındex
dizi = np.array([1,2,3,4,5,6,7,8,9])
print(dizi[0])
print(dizi[:4])

#dizinin tersine cevirme
print(dizi[::-1])

dizi2DD = np.array([[1,2,3,4,5],[3,4,5,6,6]])
print(dizi2DD)

# dizinin 1.satır 1. sutunundakı elemanı yazdırma
print(dizi2DD[1,1])

#dizinin 1. sutun ve tum satırlar 
print(dizi2DD[:,1])

# 1. satırındakı 1,2,3 elemanlarını almak ıstoyorum
print(dizi2DD[1,1:4])

# dızının son satır ve tum sutunları
print(dizi2DD[-1,:])

dizi2Dd = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2Dd)

#ıkı boyutlu bır dızıyı vektor halıne getırıyor cnn de kullanıyor
vektor = dizi2Dd.ravel()
print(vektor)

# max sayının ındexını buluyoruz
max_sayının_indexi = vektor.argmax()
print(max_sayının_indexi)

# %% PANDAS LİB

import pandas as pd

# sozluk olustur
sozluk = {
    "isim":["Ali","Veli","Kenan","Murat","Ayse","Hial"],
    "yas": [15,16,17,33,45,66],
    "maas": [100,140,150,360,200,190]
    }

# ben bu sozluk yapısını dataframe yapısına yanı veri yapısına cevirecegim 

veri = pd.DataFrame(sozluk)
print(veri)

#ilk 5 satir yadırır
print(veri.head())

# verinin sutunlarını yazdır
print(veri.columns)

# veri bilgisi
print(veri.info())

print("-------*****")

#istatistiksel ozellıkler
print(veri.describe())

# yas sutunu yadırmak ıstersem
print(veri["yas"])

# sutun eklemek ıcın
veri["sehir"] = ["Ankara","İstanbul","Antep","Barak","Nizip","Konya"]
print(veri)

#yas sutunu(locasyon kısaltılması)
print(veri.loc[:,"yas"])

#yas sutunu ve ilk 4 satır
print(veri.loc[:3,"yas"])

#yas ve sehir arası sutunu ve ilk 4 satır
print(veri.loc[:3,"yas":"sehir"])

#yas ve sehir sutunu ve ilk 4 satır
print(veri.loc[:3,["yas","sehir"]])

# satırları terseten yazdır
print(veri.loc[::-1,:])

#yas sutununu iloc tan yazdıralim(indexlocation)
print(veri.iloc[:,1])

#ilk uc satır ve yas ve ısım iloc tan yazdıralim(indexlocation)
print(veri.iloc[:2,[0,1]])
print("-----------****---------")

#DATAFRAMLERIN EN ONEMLI OZELLIKLERINDEN BIRI FILTRELEMEDIR

sozluk2 = {
    "isim":["Ali","Veli","Kenan","Murat","Ayse","Hial"],
    "yas": [15,16,17,33,45,66],
    "sehir": ["Ankara","İstanbul","Ankara","Barak","Ankara","Konya"]
    }


veri2 = pd.DataFrame(sozluk2)
print(veri2)

#ilk olarak yasa gore bır fıltre uygulayalım
filtre1 = veri2.yas>22
filtrelenmıs_veri = veri[filtre1]
print(filtrelenmıs_veri)

#ortalama yası bulalım

ortalama_yas = veri2.yas.mean()

veri2["Yas_grubu"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri2.yas]
print(veri)

#veri birleştirme
veri3 = pd.DataFrame(sozluk2)

# dıkeyde bırlestırme
veri_dıkey = pd.concat([veri,veri2],axis=0)

# veriyi yatay bırlestırme
veri_yatay = pd.concat([veri,veri2],axis=1)

# %% MATPLOTLİB LİB 

 
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,5,6,7])

plt.figure() # gorsellestırmeyı baslatma
plt.plot(x,y,color = "red",alpha = 0.3,label = "line") # cızgı cızer kosegene 
plt.scatter(x,y,color="blue",alpha =0.4,label="scatter") # nokta cızer kosegene

plt.title("Matplotlib giris") # baslık ısımlendırme
plt.xlabel("x") # x sutunu ısmlendırme
plt.ylabel("y") # y sutunu ısımlendırme

plt.grid(True) # ızgara yapısını gosterme true dersek gosterır

plt.xticks([0,1,2,3,4,5]) # x eksenındekı degerlerı senın ıstedıgın dızı yapısına gore aralıklandırır

plt.legend() # scatter plot czgı ve noktalarını gorsellestırmede kullanılır verdıgımız label ısımlerını gosterır
plt.show() # gorsellestırmeyı bıtırme gıbı dusunebılırsın


print("---------***********--------")

fig, axes=plt.subplots(2,1, figsize=(9,7))
fig.subplots_adjust(hspace=0.5) #ıkı resmın arasında bosluk olsun demek

x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]

axes[0].scatter(x,y)
axes[0].set_title("sub_1")
axes[0].set_ylabel("sub_1_y")
axes[0].set_xlabel("sub_1_x") 

axes[1].scatter(y,x)
axes[1].set_title("sub_2")
axes[1].set_ylabel("sub_2_y")
axes[1].set_xlabel("sub_2_x") 

# random resım olusturma

plt.figure()
img = np.random.random((50,50))
plt.imshow(img,cmap="gray")# sıfır sıyah 1beya 0.5 grı degerı gray yazarsak
#plt.axis("off") kenarlardakı degerlerı kaldırır
plt.show()

# %% OS LİB 

import os 

print(os.name) # ısletım sıstemımızın turunu ogrenmemeızı saglar

currentdir=os.getcwd()
print(currentdir)

# yenı dosya olusturma

folder_name="yeni_folder"
os.mkdir(folder_name)

# ısım degıstırme
new_folder_name = "new_folder_2"
os.rename(folder_name,new_folder_name)

#farklı klasor ıcınde gırme
os.chdir(currentdir+"\\"+new_folder_name)
print(os.getcwd())

files = os.listdir() # dosyaları yadırma

# dosyaların ıcerısınde dolas ve dosyanın sonu py ıle bıtıyorsa yazdır

for f in files:
    if f.endswitch(".py"):
        print(f)

os.rmdir(new_folder_name) # dosyayı sılme

for i in os.walk(currentdir):
    print(i)
    
os.path.exists("python_hatirlatma.py")  # boyle bır  dosya varmı bunu kontrol et  

