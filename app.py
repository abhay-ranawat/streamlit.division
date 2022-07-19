import streamlit as st


def answer(text):
    return f'<h4 style=\'text-align: center; padding-top: 20px; color: green;\'>Answer: {text:.2f}</h4>'


st.markdown("<h1 style='text-align: center; padding-top: 60px; padding-bottom: 0px;'>Division</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; padding-top: 0px; padding-bottom: 40px;'>Divide Two Numbers using Streamlit</p>",
            unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    num_one = st.number_input('First Number', value=1.0)

with col2:
    num_two = st.number_input('Second Number', value=1.0)


with st.empty():
    if num_two == 0:
        st.error('Cannot Divide by Zero')
    else:
        if st.button('Divide'):
            if num_two != 0:
                st.write(answer(num_one / num_two),
                         unsafe_allow_html=True)
