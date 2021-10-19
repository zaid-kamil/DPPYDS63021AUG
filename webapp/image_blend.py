import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')
st.title("Image Blend")
c1,c2 = st.columns(2)

c1.header("Upload 1st image ")
c2.header("Upload 2nd image ")
file1 = c1.file_uploader("select any image to upload",type=['jpg','png','gif'])
file2 = c2.file_uploader("select any image 2 to upload",type=['jpg','png','gif'])

if file1 and file2:
    img1 = Image.open(file1)
    img2 = Image.open(file2)
    img_area1 = c1.empty()
    img_area2 = c2.empty()
    img_area1.image(img1,use_column_width=True)
    img_area2.image(img2,use_column_width=True)

    blend_value = st.slider("Blend value",0.0, 1.0, 0.5)
    img2 = img2.resize((img1.width,img1.height))
    st.write(img1.format,img2.format)
    try:
        mix_image = Image.blend(img1,img2,blend_value)
        st.image(mix_image, use_column_width=True)
    except:
        st.write("try something else")