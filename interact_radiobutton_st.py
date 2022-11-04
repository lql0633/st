import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st



def draw_plot(ax,df,by='Global_Sales'):
    region=by.split('_')[0]
    print(by)
    ax.set_title(f"top 10 game saled within {region}")
    df=df.sort_values(by=[by],ascending=False).reset_index()
    game_name=[]
    sales=[]
    for index in range(10):
        game_name.append(df.loc[index,'Name'])
        sales.append(df.loc[index,by])
    print(game_name)
    print(sales)
    ax.set_xlabel('game name')
    ax.xaxis.set_tick_params(rotation=45,labelsize=8)
    ax.set_ylabel('copies uint (million)')
    ax.plot(game_name,sales,marker='o')
    for index in range(len(game_name)):
        ax.text(index,sales[index],sales[index])




def interact_radiobutton():
    df=pd.read_csv('vgsales.csv',header=0)
    fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.2,bottom=0.3)
    genre = st.radio(
    label="Region",
    options=('NA', 'EU', 'JP','Other','Global'),

    )
    if genre=='':
        draw_plot(ax,df)
    else:
        region=genre+'_Sales'
        draw_plot(ax,df,region)
        plt.draw()

   
    st.pyplot(fig)

if __name__=='__main__':
    interact_radiobutton()