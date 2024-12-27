import streamlit as st
#import time


def par(p):
    m = 0
    rus = 0
    eng = 0
    qe = 0
    sem = 0
    # localtime = time.localtime(time.time())
    # hour = localtime.tm_hour
    # min = localtime.tm_min
    # checktime = f'{hour}:{min}'
    for s in p:
        if s in "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
            rus += 1
        if s in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            eng += 1
        if s in "1234567890":
            qe += 1
        if s in "@,. :":
            sem += 1

    if len(p) < 3:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "в вашем пороле должно быть минимум 3 символа</p>", unsafe_allow_html=True)
    elif len(p) > 100:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "в вашем пороле должно быть максимум 100 символов</p>", unsafe_allow_html=True)
    elif "Ваня" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "толькао мой пароль может содержать маё имя</p>", unsafe_allow_html=True)
    elif "123" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "интересно скосько сикунд мне понадобится чтобы отгадать этот патоль</p>", unsafe_allow_html=True)
    elif "1234" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "интересно скосько сикунд мне понадобится чтобы отгадать этот патоль</p>", unsafe_allow_html=True)
    elif "12345" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "интересно скосько сикунд мне понадобится чтобы отгадать этот патоль</p>", unsafe_allow_html=True)
    elif "ваня" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "толькао мой пароль может содержать маё имя</p>", unsafe_allow_html=True)
    elif "Карев" in p:
        print("толькао мой пароль может содержать маю фамилию")
        st.markdown("<p style='text-align: center; color: black;'>"
                    "толькао мой пароль может содержать маю фамилию</p>", unsafe_allow_html=True)
    elif "карев" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "толькао мой пароль может содержать маю фамилию</p>", unsafe_allow_html=True)
    elif "Vanya" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "толькао мой пароль может содержать маё имя</p>", unsafe_allow_html=True)
    elif "vanya" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "толькао мой пароль может содержать маё имя</p>", unsafe_allow_html=True)
    elif "Karev" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "толькао мой пароль может содержать маю фамилию</p>", unsafe_allow_html=True)
    elif "karev" in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "толькао мой пароль может содержать маю фамилию</p>", unsafe_allow_html=True)
    elif "@"not in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "ваш пароль должен содержать символ @</p>", unsafe_allow_html=True)
    elif "Pe"not in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "ваш пароль должен содержать символ Pe</p>", unsafe_allow_html=True)
    elif "Minecraft"not in p:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "ваш пароль должен содержать слово Minecraft</p>", unsafe_allow_html=True)
    elif rus < 10:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "в вашем пароле должно быть минимум 10 руских букв</p>", unsafe_allow_html=True)
    elif len(p) > rus + eng + qe + sem:
        st.markdown("<p style='text-align: center; color: black;'>"
                    "вы используете запретные символы</p>", unsafe_allow_html=True)
    # elif checktime not in p:
        # st.markdown("<p style='text-align: center; color: black;'>"
                    # "в пароле нужно укозать время указываемое на вашем устройстве</p>", unsafe_allow_html=True)
        # st.markdown("<p style='text-align: center; color: black;'>"
                    # "используя символ :</p>", unsafe_allow_html=True)
    else:
        m += 1
    if m == 0:
        # time.sleep(1)
        print( )
    else:
        st.markdown("<h2 style='text-align: center; color: green;'>ваш пароль подходит!</h2>", unsafe_allow_html=True)
        st.image("mmm.webp")


st.markdown("<h1 style='text-align: center; color: blue;'>привет. попробуй отгодать пароль!</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>"
            "правила сделаны по приколу.</p>", unsafe_allow_html=True)
o = st.text_input("ведите пароль")
par(o)