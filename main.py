import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('streamlit 超入門 write')


latest_iteration = st.empty()
bar = st.progress(0)

if st.checkbox('Interation'):
    'Start！'
    for i in range(100):
        latest_iteration.text(f'Interation{i+1}')
        bar.progress(i+1)
        time.sleep(0.05)
        '完了!!!'


left_column, right_column = st.columns(2)
button = left_column.button('Memo')
if button:
    right_column.write('やっとここまできた')

expander = st.expander('問い合わせ')
expander.write('どこまで進んでる？')

#if st.checkbox('Show Image'):
#    img = Image.open('sample2.jpg')
#    st.image(img, caption='犬', use_column_width=True)    

#text = st.text_input('あなたの趣味を教えてください。')
#'あなたの趣味:' , text

#condition = st.slider('あなたの今の調子は',0 ,100, 50)
#'コンディション：', condition

#option = st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1,11))
#)
#'あなたの好きな数字は', option, 'です'



