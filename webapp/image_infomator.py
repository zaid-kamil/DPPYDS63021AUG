import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

st.title("Upload image stuff")
file = st.file_uploader("select any image to upload",type=['jpg','png','gif'])
if file:
    img = Image.open(file)
    img_area = st.empty()
    img_area.image(img)

    st.sidebar.header("Options")
    st.sidebar.subheader("resize image")    
    st.sidebar.text(img.size)
    nw = st.sidebar.slider("image width(px) ",100,img.width*3)
    nh = st.sidebar.slider("image height(px) ",100,img.height*3)
    if st.sidebar.button("Apply"):
        img_new = img.resize((nw,nh))
        st.success("resized image")
        img_area.image(img_new)

    st.sidebar.subheader("enhance image") 
    val_contrast = st.sidebar.slider("Contrast",-10,10)
    if st.sidebar.button("Apply enhancement"):
        imgen = ImageEnhance.Contrast(img)
        img = imgen.enhance(val_contrast)
        img_area.image(img)

