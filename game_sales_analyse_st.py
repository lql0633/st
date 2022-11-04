import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st







def game_sales_analyse():
    df=pd.read_csv('vgsales.csv',header=0)
    game_genre=list(df['Genre'].value_counts().keys())
    print(game_genre)
    sales_with_game_genre=[]
    for index in range(len(game_genre)):
        df_data=df[df['Genre'].isin([game_genre[index]])]
        sales_with_game_genre.append(round(df_data['Global_Sales'].sum(),2))
    print(sales_with_game_genre)
    labels=['NA_Sales','EU_Sales','JP_Sales','Other_Sales']
    sales_with_region=[]
    sales_with_region.append(round(df['NA_Sales'].sum(),2))
    sales_with_region.append(round(df['EU_Sales'].sum(),2))
    sales_with_region.append(round(df['JP_Sales'].sum(),2))
    sales_with_region.append(round(df['Other_Sales'].sum(),2))
    fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.2,hspace=1)
    fig.set_size_inches(14,8)
    ax1 = plt.subplot(2,1,1)
    ax1.set_title("game sales with genre")
    ax1.set_xlabel('game name')
    ax1.xaxis.set_tick_params(rotation=20,labelsize=8)
    ax1.set_ylabel('copies uint (million)')
    for index in range(len(game_genre)):
        ax1.bar(game_genre[index],sales_with_game_genre[index])
        ax1.text(index-0.25,sales_with_game_genre[index],sales_with_game_genre[index])
    
    ax2 = plt.subplot(2,1,2)
    explode = (0.1, 0, 0, 0) 
    ax2.set_title('pct of game sales with region',y=1.2) 
    ax2.pie(sales_with_region, explode = explode, 
        labels = labels, autopct ='% 1.1f %%', 
        shadow = True, startangle = 90,radius=1.5) 
  
    st.pyplot(fig)
    # plt.show() 
    
if __name__=='__main__':
    game_sales_analyse()