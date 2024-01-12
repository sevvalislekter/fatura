
class fatura():
    def __init__(self):
        self.kalemler=[]

    def kalem_ekle(self, aciklama, miktar, birim_fiyat):

         self.kalemler.append({"aciklama": aciklama, "miktar": miktar, "birim_fiyat": birim_fiyat})


    def toplam_hesapla(self):
            toplam = sum(kalem['miktar'] * kalem['birim_fiyat'] for kalem in self.kalemler)
            return toplam

    def vergi_ekle(self, vergi_orani):
            toplam_vergi_dahil = self.toplam_hesapla() * (1 + vergi_orani / 100)

            return toplam_vergi_dahil

    def faturayi_yazdir(self):
            print("Fatura:")

            for kalem in self.kalemler:

                print(f"{kalem['aciklama']} - {kalem['miktar']} adet - {kalem['birim_fiyat']} TL birim fiyat")
                print(f"Toplam: {self.toplam_hesapla()} TL")


fatura = fatura()
fatura.kalem_ekle("Ürün1", 3, 20)
fatura.kalem_ekle("Ürün2", 2, 30)
fatura.faturayi_yazdir()
print(f"KDV (%18) Dahil Toplam: {fatura.vergi_ekle(18)} TL")

