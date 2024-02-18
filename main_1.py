import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

option = st.sidebar.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は', option ,'です。'

text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味は', text
'コンディション：', condition

df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [5, 6, 7, 8]
})

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='FX AUDJPY', use_column_width=True)

st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

st.table(df) # 静的なテーブル

"""

# 大
## 中
#### 小

```python
import streamlit as st
import pandas as pd
```
"""

df_l = pd.DataFrame(np.random.randn(20,3),columns=['a', 'b', 'c'])

st.line_chart(df_l)

df_m = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
    )

st.map(df_m)