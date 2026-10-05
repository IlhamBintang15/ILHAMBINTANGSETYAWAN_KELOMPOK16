# Ilham Bintang-Kelompok-16
STOK_KRITIS = 10


def cetak_watermark():
    print(" ==>>SYSTEM INVENTARIS TOKO HARDWARE KELOMPOK 16<<== ")


def input_pilihan_menu(min_pilihan, max_pilihan):
    try:
        pilihan = int(input(f"Pilih Menu ({min_pilihan}-{max_pilihan}): "))
        if min_pilihan <= pilihan <= max_pilihan:
            return pilihan
        else:
            print("❌ Error: Pilihan di luar jangkauan menu.")
            return -1
    except ValueError:
        print("❌ Error: Input harus berupa angka valid.")
        return -1


class Barang:
    def __init__(self, nama, stok):
        self.nama = nama
        self.stok = stok

    def get_status(self):
        if self.stok < STOK_KRITIS:
            return "Kritis"
        return "Aman"

    def update_jumlah_stok(self, jumlah, is_restock):
        if is_restock:
            self.stok += jumlah
            print(f"✅ Restock berhasil! Stok {self.nama} bertambah {jumlah}.")
        else:
            if self.stok >= jumlah:
                self.stok -= jumlah
                print(f"✅ Barang keluar berhasil! Stok {self.nama} berkurang {jumlah}.")
            else:
                print(f"⚠️ Gagal! Stok {self.nama} ({self.stok}) tidak mencukupi untuk dikeluarkan {jumlah}.")


class InventarisToko:
    def __init__(self):
        self.daftar_barang = [
            Barang("Monitor", 15),
            Barang("Keyboard", 20),
            Barang("Mouse", 8),
            Barang("Casing PC", 4)
        ]

    def cari_barang(self, nama):
        for barang in self.daftar_barang:
            if barang.nama.lower() == nama.lower():
                return barang
        return None

    def tampilkan_stok(self):
        print("\n--- DAFTAR STOK BARANG [ KELOMPOK 16 ] ---")
        print(f"{'No.':<3} | {'Nama Barang':<12} | {'Jumlah Stok':<11} | Status")

        for i, barang in enumerate(self.daftar_barang, start=1):
            status = barang.get_status()
            print(f"{i:<3} | {barang.nama:<12} | {barang.stok:<11} | {status}")

    def olah_stok(self, nama, jumlah, is_restock):
        if jumlah <= 0:
            print("❌ Error: Jumlah barang harus lebih dari 0.")
            return

        barang_ditemukan = self.cari_barang(nama)

        if barang_ditemukan:
            barang_ditemukan.update_jumlah_stok(jumlah, is_restock)
        else:
            if is_restock:
                barang_baru = Barang(nama.title(), jumlah)
                self.daftar_barang.append(barang_baru)
                print(f"✨ Barang baru '{nama.title()}' berhasil ditambahkan ke inventaris [KELOMPOK 16]!")
            else:
                print(f"❌ Error: Barang '{nama}' tidak ditemukan dalam inventaris.")


def main():
    toko = InventarisToko()
    pilihan = 0

    while pilihan != 4:
        cetak_watermark()
        print("1. Tampilkan Semua Stok Barang")
        print("2. Restock Barang (Barang Masuk)")
        print("3. Catat Barang Keluar")
        print("4. Keluar Program")

        pilihan = input_pilihan_menu(1, 4)

        if pilihan == 1:
            toko.tampilkan_stok()

        elif pilihan == 2:
            nama = input("Masukkan Nama Barang untuk Restock: ").strip()
            try:
                jumlah = int(input("Masukkan Jumlah Masuk: "))
                toko.olah_stok(nama, jumlah, is_restock=True)
            except ValueError:
                print("❌ Input jumlah tidak valid.")

        elif pilihan == 3:
            nama = input("Masukkan Nama Barang Keluar: ").strip()
            try:
                jumlah = int(input("Masukkan Jumlah Keluar: "))
                toko.olah_stok(nama, jumlah, is_restock=False)
            except ValueError:
                print("❌ Input jumlah tidak valid.")

        elif pilihan == 4:
            print("\nTerima kasih! Program Inventaris Toko Hardware Kelompok 16 Selesai.")


if __name__ == "__main__":
    main()
