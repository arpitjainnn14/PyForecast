import streamlit as st 
import plotly.express as px
from backend import get_data


st.set_page_config(layout='centered')

st.title('PyForecast')

place=st.text_input('Place',placeholder='Write the name of the place...')

days=st.slider('Forecast Days',1,5,help="Choose the number of days for forecast.")

option=st.selectbox('Select data to view',('Temperature','Sky'),placeholder='Select')

st.subheader(f"{option} for the next {days} in {place}")

#if the place value is filled then execute this
try:
    if place:
        required_data=get_data(place,days)
        
        if option=="Temperature":
            temperature_data = []
            
            #fetches the temperature value
            for x in required_data:
                yy = x['main']['temp']/10
                temperature_data.append(yy)
            date_data=[]
            
            #fetches the date value
            for x in required_data:
                uu=x["dt_txt"]
                date_data.append(uu)
            
            #
            """
            px.line() expects the values who are array type of objects
            plots the line graph for the data above
            """
            figure=px.line(x=date_data,y=temperature_data,labels={"x":"Dates","y":"Temperature (C)"})
            
            st.plotly_chart(figure)
        
        # check if the user has selected sky, then find the all the values of sky and append them into the list
        if option=="Sky":
            #fetches the sky conditions from the api data
            sky_data = []
            for r in required_data:
                zz = r['weather'][0]['main']
                sky_data.append(zz)

            images={"Clear":"images/clear.png","Clouds":'images/cloud.png',"Rain":'images/rain.png',"Snow":'images/snow.png'}
            
            image_paths=[]
            for i in sky_data:
                pp=images[i]
                image_paths.append(pp)
            
            #fetching the date for writing the caption
            date_data=[]
            for x in required_data:
                uu=x["dt_txt"]
                date_data.append(uu)
            st.image(image_paths,width=100,caption=date_data)
            
except KeyError:
    st.info("No City found! Check your spelling again.")
