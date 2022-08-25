import qrcode
import streamlit as st
import image
from PIL import Image

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

st.title("QR Code Generator")
st.write("Create your QR Code for free")
st.caption("BY HARSHSTAG")

title = st.text_input('Enter URL', 'https://github.com/Harshstag')
data = title

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_colour = "white")
img.save("test.png")

image = Image.open('test.png')

col1, col2, col3 = st.columns(3)

        # Widget (Cryptocurrency selection box)
with col1:
    st.write("⠀")
with col2:
    st.image(image, caption=title, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    
with col3:
    st.write("⠀")


with open("test.png", "rb") as file:
    btn = st.download_button(
        label="Download QR Code",
         data=file,
         file_name="qrcodeImg.png",
         mime="image/png"
        )
