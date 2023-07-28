# -*- coding: utf-8 -*-
"""

@author: IdrisIbrahimERTEN
"""

import speedtest

def internet_speed_test():
    st = speedtest.Speedtest()
    
    print("İnternet hızı testi yapılıyor... Lütfen bekleyin.")
    st.get_best_server()  # En iyi sunucuyu otomatik olarak seçmek için
    
    download_speed = st.download() / 10**6  # Mbps cinsinden indirme hızı
    upload_speed = st.upload() / 10**6  # Mbps cinsinden yükleme hızı
    ping = st.results.ping  # Ping süresi (ms)
    
    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
    internet_speed_test()
