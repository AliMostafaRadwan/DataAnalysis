import  numpy as np
import streamlit as st
import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.image('img.jpeg')

data =  st.file_uploader('upload Your "CSV" File',type = 'csv')




head = pd.read_csv(data)
st.dataframe(head.head())

text1 = st.text_input(label='First Input (Y axis)',placeholder='ex. col1')
text2 = st.text_input('Secound Input (X axis)',placeholder = 'ex. col2')



dfM = head


####################
chart_data = pd.DataFrame(dfM[text1],dfM[text2])

idl = pd.DataFrame(np.random.randn(1,3), columns=['a','b','c'])

#st.write(df.columns)
col1, col2, col3 = st.columns(3)

col2.title('THE PLOT')
def main():
    page = st.sidebar.selectbox(
         "Select a The Plot Type",
        ["Line Plot",'Point Plot',"Bar Plot",'Pair Plot','Scatter Plot','Regression Plot'])
    if page == "Line Plot":
          linePlot()

    elif page == "Point Plot":
         PointPlot()
    elif page == "Bar Plot":
         BarPlot()
    elif page == "Pair Plot":
         PairPlot()
    elif page == "Scatter Plot":
         ScatterPlot()
    elif page == "Regression Plot":
         RegressionPlot()


def linePlot():
    fig = plt.figure(figsize=(15, 5))
    sns.lineplot(y = dfM[text1], x = dfM[text2], data = dfM)
    
    st.pyplot(fig)
    with st.expander('Interactive Plot'):
         st.area_chart(chart_data)
         st.caption('Double Click To Reset')
         

def PointPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.pointplot(y = dfM[text1], x = dfM[text2], data = dfM)
    st.pyplot(fig)
    
    with st.expander('Interactive Plot'):
         st.bar_chart(chart_data)
         st.caption('Double Click To Reset')

def BarPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.barplot(y = dfM[text1], x = dfM[text2], data = dfM)
    st.pyplot(fig)

def PairPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.pairplot(dfM)
    st.pyplot(fig)


def ScatterPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.scatterplot(y = dfM[text1], x = dfM[text2], data = dfM)
    st.pyplot(fig)

def RegressionPlot():
    fig = plt.figure(figsize=(10, 4))
    sns.regplot(y = dfM[text1], x = dfM[text2], data = dfM)
    st.pyplot(fig)

if __name__ == "__main__":
    main()