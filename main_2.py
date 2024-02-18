import streamlit as st
import numpy as np
import pandas as pd
import time

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ１の回答')
expander2 = st.expander('問い合わせ２')
expander2.write('問い合わせ２')
expander3 = st.expander('問い合わせ３')
expander3.write('問い合わせ３')