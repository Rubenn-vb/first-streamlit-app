import streamlit
import pandas as pd

file = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_fruit_list = pd.read_csv(file)

streamlit.title("My Moms New Healthy Diner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 And Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast") 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# display fruit selector
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list['Fruit']), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[my_fruit_list['Fruit'].isin(fruits_selected)]

# display table
streamlit.dataframe(fruits_to_show)
