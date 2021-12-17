import pandas as pd
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

st.set_page_config(page_title= 'Bankruptcy Prediction', page_icon = '💰', layout= 'wide',
                   initial_sidebar_state= 'collapsed')
model = load_model('neural_model_4-23-Nov-2021-15_56_31.h5')

@st.cache
def model_prediction(input_list):
    values = [input_list]
    # model = load_model('neural_model_4-23-Nov-2021-15_56_31.h5')
    prediction = np.round(model.predict(values))
    probability = model.predict(values)
    return prediction, probability

# @st.cache

# The order of variable is:
# industrial_risk, management_risk, financial_flexibility, credibility, competitiveness,  operation_risk


# User input Function
def user_input_values():
    st.write("""
    ** *0* Denotes the parameter is weak.** 
    """)
    st.write(" ** *1* Denotes the parameter is Strong**")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    irisk = col1.radio('Industrial Risk', [0, 0.5, 1])
    mrisk = col2.radio('Management Risk', [0, 0.5, 1])
    ff = col3.radio('Financial Flexibility', [0, 0.5, 1])
    crd = col4.radio('Credibility', [0,0.5,1])
    comp = col5.radio('Competitiveness', [0, 0.5, 1])
    orisk = col6.radio('Operation Risk', [0, 0.5, 1])
    return [irisk, mrisk, ff, crd, comp, orisk]


def side_bar_func():
    st.sidebar.text('## About')

# @st.cache(suppress_st_warning= True)
def more_detain_expander():
    with st.expander("More information"):
        info_file = open('more_info.txt', encoding='utf8').read()
        st.write(info_file)


# @st.cache(suppress_st_warning=True)
def main():
    st.title('Bankruptcy Prediction Model')
    col_first, col_end = st.columns([3,1])
    bankruptcy_image = Image.open('Smith-Debnam-Articles-and-Insights-68-900x350-c-default.png')
    col_first.image(bankruptcy_image,)
    col_end.markdown('''
    **Bankruptcy is a legal process through which people or 
    other entities who cannot repay debts to creditors may 
    seek relief from some or all of their debts.**
    ''')
    col_end.write('''
    This model uses various parameters that used to predict bankruptcy of company, which are:
    ''')
    col_end.write("""
    1. Industrial risk
    2. Management risk
    3. Operational risk
    4. Financial risk.
    5. Credibility.
    6. Competitiveness.
    """)
    more_detain_expander()
    input_values = user_input_values()
    if st.button('Predict'):
        pred, prob = model_prediction(input_values)
        if pred == 0:
            col1, col2 = st.columns([1,2])
            col1.write('Sorry you are going to be bankrupt')
            col1.write('The probability of getting bankrupt is {} %'.format(int(100-(prob*100))))
            image_1 = Image.open('Dont-Give-Up-Quotes.jpg')
            col2.image(image_1, width = 700)

        else:
            col1, col2 = st.columns([1,2])
            col1.write('Congratulation you are safe')
            col1.write('The probability of getting bankrupt is {} %'.format(int(100- (prob * 100))))
            image_1 = Image.open('congratulation.jpg'
                                 )
            col2.image(image_1)

if __name__ == '__main__':
    main()