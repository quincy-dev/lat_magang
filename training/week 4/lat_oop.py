class mobil:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
    def info_mobil(self):
        return f"{self.merk} {self.model} ({self.tahun})"
class listrik:
    def __init__(self, kapasitas_baterai):
        self.kapasitas_baterai = kapasitas_baterai
    def info_baterai(self):
        return f"Kapasitas baterai: {self.kapasitas_baterai} kWh"
class mobil_listrik(mobil, listrik):
    def __init__(self, merk, model, tahun, kapasitas_baterai):
        mobil.__init__(self, merk, model, tahun)
        listrik.__init__(self, kapasitas_baterai)
    def info_mobil_listrik(self):
        return f"{self.info_mobil()}, {self.info_baterai()}"
def main():
    tesla_model_s = mobil_listrik("Tesla", "Model S", 2020, 100)
    print(tesla_model_s.info_mobil_listrik())
if __name__ == "__main__":
    main()
