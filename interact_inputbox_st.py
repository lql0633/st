import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st




def draw_histogram(ax,df,publisher='Nintendo'):
    ax.set_title(f"vg sales of {publisher} with region ")
    df_data=df[df['Publisher'].isin([publisher])]
    df_data=df_data.reset_index()
    data_list=[]
    NA_Sales=round(df_data['NA_Sales'].sum(),2)
    EU_Sales=round(df_data['EU_Sales'].sum(),2)
    JP_Sales=round(df_data['JP_Sales'].sum(),2)
    Other_Sales=round(df_data['Other_Sales'].sum(),2)
    Global_Sales=round(df_data['Global_Sales'].sum(),2)
    data_list.append(NA_Sales)
    data_list.append(EU_Sales)
    data_list.append(JP_Sales)
    data_list.append(Other_Sales)
    data_list.append(Global_Sales)
    # print(df_data['Publisher'])
    # print(data_list)
    region=['NA','EU','JP','Other','Global']
    ax.set_xlabel('region')
    ax.set_ylabel('copies uint (million)')
    for index in range(len(region)):
        ax.bar(region[index],data_list[index])
        ax.text(index-0.25,data_list[index],str(data_list[index]))

def interact_inputbox():
    df=pd.read_csv('vgsales.csv',header=0)
    publishers=list(df['Publisher'].value_counts().keys())
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    input_publisher=st.text_input('Input Publisher ')
    if input_publisher!='' and input_publisher in publishers:
        draw_histogram(ax,df,input_publisher)
    else:
        draw_histogram(ax,df)
    
  
    st.button('Submit')
    st.pyplot(fig)
    # plt.show() 

if __name__=='__main__':
    interact_inputbox()