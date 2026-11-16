# Üretim oturumu kuralları (yalın profil)

Bu oturum srv21'de başsız bir üretim oturumudur (Linux x86_64, kullanıcı sef). İstem görevi tanımlar; bu kurallar her
görevde geçerlidir ve istemle çelişirse güvenlik maddeleri kazanır.

1. Silme yok. `rm` kullanma; gereksiz dosyayı `/home/sef/Silinecekler/<GG.AA>-<konu>/` altına taşı.
2. `.env`, `*.key`, `*.pem` dosyalarını okuma, yazma. Jeton, anahtar, parola basma; gerekirse yalnız değişken adını yaz.
3. İstem açıkça istemedikçe git commit, push, dal değişikliği yapma.
4. Yazma yalnız istemin izin verdiği dizinlerde. Başka paketin dosyasına dokunma.
5. Türkçe metinde Türkçe karakterler zorunlu (ç ö ü ğ ı ş İ). ASCII karşılık yazma.
6. Kod: 2 boşluk girinti, satır en çok 100 karakter. TypeScript'te `any` yok. Python'da tip ipucu zorunlu, `/usr/bin/python3 -I`.
7. Yalnız isteneni yap: istenmeyen dosya, seçenek, soyutlama ekleme.
8. Uzun komutu ön planda `timeout <sn>` ile sınırla. Ön planda `sleep` ile bekleme döngüsü kurma.
9. Ağır adımdan önce bak: sonuç zaten diskte varsa (kare, ses, rapor) yeniden üretme.
10. Bir iddiayı (geçti, eşit, N/N) komut çıktısıyla yaz; çıktısı olmayan iddia yazma.
11. Son mesaj istemin istediği uzunlukta ve biçimde; ek özet, altbilgi yazma.
