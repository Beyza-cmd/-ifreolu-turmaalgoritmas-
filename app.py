import streamlit as st
import random
import string
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# --- Şifre oluşturma fonksiyonu ---
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- E-posta gönderme fonksiyonu ---
def send_email(to_email, password, expiration_time):
    your_email = "beyza.solmaz@stu.fsm.edu.tr"
    your_app_password = "pplgmumffhifjrqt"  # Google'dan alınan uygulama şifresi

    subject = "Tek Kullanımlık Şifreniz"
    body = f"""
Merhaba,

İstediğiniz tek kullanımlık şifreniz aşağıdadır:

Şifre: {password}
Geçerlilik süresi: {expiration_time.strftime('%H:%M:%S')}

Lütfen bu şifreyi kimseyle paylaşmayın. Şifre 10 dakika sonra geçersiz olacaktır.

GüvenBank
"""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = your_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(your_email, your_app_password)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"E-posta gönderimi başarısız: {e}")
        return False

# --- Arayüz tasarımı ---
st.markdown("""
    <style>
    .bank-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        max-width: 600px;
        margin: auto;
        margin-top: 40px;
        font-family: 'Segoe UI', sans-serif;
    }
    .bank-title {
        font-size: 32px;
        font-weight: bold;
        color: #003366;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="bank-container">', unsafe_allow_html=True)
st.markdown('<div class="bank-title">GüvenBank Giriş Paneli</div>', unsafe_allow_html=True)

# Kullanıcı Bilgileri
name = st.text_input("Ad Soyad")
email = st.text_input("E-posta Adresi")

length = st.slider("Şifre uzunluğunu seçin:", min_value=6, max_value=20, value=10)

if st.button("Şifre Oluştur ve Gönder"):
    if name and email:
        password = generate_password(length)
        expiration_time = datetime.now() + timedelta(minutes=10)

        if send_email(email, password, expiration_time):
            st.success(f"Şifre başarıyla {email} adresine gönderildi!")
        else:
            st.error("Bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
    else:
        st.warning("Lütfen tüm alanları doldurun.")

st.markdown('</div>', unsafe_allow_html=True)
