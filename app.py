import streamlit as st
import random
import string
from datetime import datetime, timedelta

# Şifre oluşturma fonksiyonu
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit arayüzü
st.title("Tek Kullanımlık Şifre Üretici")

# Kullanıcıya mesaj gösterme
st.write("Merhaba, ben tek kullanımlık şifre üreticinim. Şifreni kullandıktan sonra değiştirmen gerektiğini ve 10 dakika sonra şifrenin geçersiz olacağını unutma! Güçlü parola, güvenliğin anahtarıdır!")

length = st.number_input("Şifre uzunluğunu seçin:", min_value=6, max_value=20)

if st.button("Şifre Oluştur"):
    password = generate_password(length)
    
    # Şifre geçerlilik süresi (10 dakika)
    expiration_time = datetime.now() + timedelta(minutes=10)
    expiration_time_str = expiration_time.strftime("%H:%M:%S")
    
    # Ekranda şifre ve süreyi göster
    st.write(f"Oluşturulan Şifre: {password}")
    st.write(f"Şifre geçerlilik süresi: {expiration_time_str}")
    st.success("Şifre başarıyla oluşturuldu!")
