#Copyright HSN_THE_LAMA
import os
import time
dosya_yolu_yoklama = "a"
dosya_yolu_resimler = "a"
dosya_yolu_kisiler ="a"

def ana_menu():
 


 os.system("cls")
 print("--------------GYTS HATA DÜZELTME SİSTEMİ--------------\n\n\n")

 ilk_gorev=input("-İlk Olarak Yapmak İstediğiniz İşlemi Seçin:\n\n   --> 1)Yoklama Dosyası Sıfırlama\n   --> 2)Kişilerin ve Fotoğrafların Sıfırlanması \n   --> 3)Tüm Sistemin Yeniden Yüklenmesi\n\n")

 if ilk_gorev in ["1","1)","İlk","Ilk","ilk","ılk","birinci","Birinci","bırıncı","Bırıncı"]:
     try:
         os.remove(r"C:\Users\hasan\OneDrive\Masaüstü\galYuzTanima\abcdefg.txt")
         print("Dosya başarıyla silindi.")
         abcd=5
         while abcd !=0:
          print (str(abcd)+(" Saniye Sonra Ana Ekran"))
          time.sleep(1)
          abcd= abcd-1
          if abcd == 0:
             ana_menu()
          
            
     except FileNotFoundError:
         print("Dosya bulunamadı{e}")
     except PermissionError:
         print("Bunu Yapma Yetkim Bulunmamakta. Lütfen Bir Yetkiliye Başvurun!")
     except Exception as e:
        print(f"Bir hata oluştu: {e}")
ana_menu()