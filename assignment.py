import streamlit as st
import random
page_bg_img = '''
<style>
body {
background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9_eXcz9ATGlyxvAs-3A-NT9SAB7g-qJ8Nsw&usqp=CAU");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


a=['Barcelona','Bayern','Benfica','Chelsea','Juventus','Paris','PSV','Zenit']
b=['Arsenal','Astana','Atletico','Bate','CSKA Moskva','Dinamo Zagreb','Dynamo Kyiv','Galatasary','Gent','Leverkusen','Lyon','M. TEL','Malmo','Man. city','Man. United',
   'Monchengladbach','olympiacosh','porto','Real Madrid','Romo','Sevilla','Shakhtar Donetsk','Valencia','Wolfsburg']
random.shuffle(b)
random.shuffle(a)
st.markdown("<h1 style='text-align: left; color: white;'>GROUP A</h1>", unsafe_allow_html=True)
st.title(a[0])
st.title(b[0])
st.title(b[1])
st.title(b[2])
st.markdown("<h1 style='text-align: left; color: white;'>GROUP B</h1>", unsafe_allow_html=True)
st.title(a[1])
st.title(b[3])
st.title(b[4])
st.title(b[5])
st.markdown("<h1 style='text-align: left; color: white;'>GROUP C</h1>", unsafe_allow_html=True)
st.title(a[2])
st.title(b[6])
st.title(b[7])
st.title(b[8])
st.markdown("<h1 style='text-align: left; color: white;'>GROUP D</h1>", unsafe_allow_html=True)
st.title(a[3])
st.title(b[9])
st.title(b[10])
st.title(b[11])
st.markdown("<h1 style='text-align: left; color: white;'>GROUP E</h1>", unsafe_allow_html=True)
st.title(a[4])
st.title(b[12])
st.title(b[13])
st.title(b[14])
st.markdown("<h1 style='text-align: left; color: white;'>GROUP F</h1>", unsafe_allow_html=True)
st.title(a[5])
st.title(b[15])
st.title(b[16])
st.title(b[17])
st.markdown("<h1 style='text-align: left; color: white;'>GROUP G</h1>", unsafe_allow_html=True)
st.title(a[6])
st.title(b[18])
st.title(b[19])
st.title(b[20])
st.markdown("<h1 style='text-align: left; color: white;'>GROUP H</h1>", unsafe_allow_html=True)
st.title(a[7])
st.title(b[21])
st.title(b[22])
st.title(b[23])

