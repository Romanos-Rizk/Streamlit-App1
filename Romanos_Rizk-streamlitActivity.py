# Importing relevant libraries for the project:
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Setting a title for the project
st.title('Grocery Store Sales data')

#Importing the data set: sales of a multinational grovery store
#df_sales = pd.read_csv("C:/Users/Lenovo/OneDrive/01_Education/02_AUB/01_Fall2023/MSBA325-Data Visualization and Communication/Projects/DataSets/supermarket_sales.csv")
df_sales = pd.read_csv('data/supermarket_sales.csv')
st.subheader('Display of the Dataset:')
st.dataframe(df_sales)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# plot 1: 

st.subheader('Gross Income per Product Category:')

#Preparing the data: by calculating the gross income of each category of products in each city and calculating the gross income of each product category accross the cities:

#Gross income from the sales of electronic accessories in the city of Yangon
df_electronicAccessories_Yangon = df_sales.query("`City` == 'Yangon' and `Product line` == 'Electronic accessories'")
electronicAccessories_Yangon = df_electronicAccessories_Yangon["gross income"].sum()

#Gross income from the sales of electronic accessories in the city of Naypyitaw
df_electronicAccessories_Naypyitaw = df_sales.query("`City` == 'Naypyitaw' and `Product line` == 'Electronic accessories'")
electronicAccessories_Naypyitaw = df_electronicAccessories_Naypyitaw["gross income"].sum()

#Gross income from the sales of electronic accessories in the city of Mandalay
df_electronicAccessories_Mandalay = df_sales.query("`City` == 'Mandalay' and `Product line` == 'Electronic accessories'")
electronicAccessories_Mandalay = df_electronicAccessories_Mandalay["gross income"].sum()

#Gross income from the sale of electronic accessories accross cities
electronicAccessories = electronicAccessories_Yangon + electronicAccessories_Naypyitaw + electronicAccessories_Mandalay

#-------------------------------

#Gross income from the sales of Fashion accessories in the city of Yangon
df_fashionAccessories_Yangon = df_sales.query("`City` == 'Yangon' and `Product line` == 'Fashion accessories'")
fashionAccessories_Yangon = df_fashionAccessories_Yangon["gross income"].sum()

#Gross income from the sales of fashion accessories in the city of Naypyitaw
df_fashionAccessories_Naypyitaw = df_sales.query("`City` == 'Naypyitaw' and `Product line` == 'Fashion accessories'")
fashionAccessories_Naypyitaw = df_fashionAccessories_Naypyitaw["gross income"].sum()

#Gross income from the sales of fashion accessories in the city of Mandalay
df_fashionAccessories_Mandalay = df_sales.query("`City` == 'Mandalay' and `Product line` == 'Fashion accessories'")
fashionAccessories_Mandalay = df_fashionAccessories_Mandalay["gross income"].sum()

#Gross income from the sale of fashion accessories accross cities:
fashionAccessories = fashionAccessories_Yangon + fashionAccessories_Naypyitaw + fashionAccessories_Mandalay

#-------------------------------

#Gross income from the sales of Food and Beverages in the city of Yangon
df_foodAndbeverages_Yangon = df_sales.query("`City` == 'Yangon' and `Product line` == 'Food and beverages'")
foodAndbeverages_Yangon = df_foodAndbeverages_Yangon["gross income"].sum()

#Gross income from the sales of Food and Beverages in the city of Naypyitaw
df_foodAndbeverages_Naypyitaw = df_sales.query("`City` == 'Naypyitaw' and `Product line` == 'Food and beverages'")
foodAndbeverages_Naypyitaw = df_foodAndbeverages_Naypyitaw["gross income"].sum()

#Gross income from the sales of Food and Beverages in the city of Mandalay
df_foodAndbeverages_Mandalay = df_sales.query("`City` == 'Mandalay' and `Product line` == 'Food and beverages'")
foodAndbeverages_Mandalay = df_foodAndbeverages_Mandalay["gross income"].sum()

#Gross income from the sale of Food and Beverages accross cities:
foodAndbeverages = foodAndbeverages_Yangon + foodAndbeverages_Naypyitaw + foodAndbeverages_Mandalay

#-------------------------------

#Gross income from the sales of Health and Beauty products in the city of Yangon
df_healthAndBeauty_Yangon = df_sales.query("`City` == 'Yangon' and `Product line` == 'Health and beauty'")
healthAndBeauty_Yangon = df_healthAndBeauty_Yangon["gross income"].sum()

#Gross income from the sales of Health and Beauty products in the city of Naypyitaw
df_healthAndBeauty_Naypyitaw = df_sales.query("`City` == 'Naypyitaw' and `Product line` == 'Health and beauty'")
healthAndBeauty_Naypyitaw = df_healthAndBeauty_Naypyitaw["gross income"].sum()

#Gross income from the sales of Health and Beauty products in the city of Mandalay
df_healthAndBeauty_Mandalay = df_sales.query("`City` == 'Mandalay' and `Product line` == 'Health and beauty'")
healthAndBeauty_Mandalay = df_healthAndBeauty_Mandalay["gross income"].sum()

#Gross income from the sale of Health and Beauty products accross cities:
healthAndBeauty = healthAndBeauty_Yangon + healthAndBeauty_Naypyitaw + healthAndBeauty_Mandalay

#-------------------------------

#Gross income from the sales of Home and lifestyle products in the city of Yangon
df_homeAndlifestyle_Yangon = df_sales.query("`City` == 'Yangon' and `Product line` == 'Home and lifestyle'")
homeAndlifestyle_Yangon = df_homeAndlifestyle_Yangon["gross income"].sum()

#Gross income from the sales of Home and lifestyle products in the city of Naypyitaw
df_homeAndlifestyle_Naypyitaw = df_sales.query("`City` == 'Naypyitaw' and `Product line` == 'Home and lifestyle'")
homeAndlifestyle_Naypyitaw = df_homeAndlifestyle_Naypyitaw["gross income"].sum()

#Gross income from the sales of Home and lifestyle products in the city of Mandalay
df_homeAndlifestyle_Mandalay = df_sales.query("`City` == 'Mandalay' and `Product line` == 'Home and lifestyle'")
homeAndlifestyle_Mandalay = df_homeAndlifestyle_Mandalay["gross income"].sum()

#Gross income from the sale of Home and lifestyle products accross cities:
homeAndlifestyle = homeAndlifestyle_Yangon + homeAndlifestyle_Naypyitaw + homeAndlifestyle_Mandalay

#-------------------------------

#Gross income from the sales of Sports and travel products in the city of Yangon
df_sportsAndtravel_Yangon = df_sales.query("`City` == 'Yangon' and `Product line` == 'Sports and travel'")
sportsAndtravel_Yangon = df_sportsAndtravel_Yangon["gross income"].sum()

#Gross income from the sales of Sports and travel products in the city of Naypyitaw
df_sportsAndtravel_Naypyitaw = df_sales.query("`City` == 'Naypyitaw' and `Product line` == 'Sports and travel'")
sportsAndtravel_Naypyitaw = df_sportsAndtravel_Naypyitaw["gross income"].sum()

#Gross income from the sales of Sports and travel products in the city of Mandalay
df_sportsAndtravel_Mandalay = df_sales.query("`City` == 'Mandalay' and `Product line` == 'Sports and travel'")
sportsAndtravel_Mandalay = df_sportsAndtravel_Mandalay["gross income"].sum()

#Gross income from the sale of Sports and travel products accross cities:
sportsAndtravel = sportsAndtravel_Yangon +sportsAndtravel_Naypyitaw + sportsAndtravel_Mandalay

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Creating 4 datasets: one that contains the gross income per category accross all cities and 3 others containing the gross income per product category in in each city

#Creating numpy arrays: one that contain the name if the products categories, and the other contain the contribution of that product category in terms of gross income
arr_productCategory = np.array(['Electronic accessories','Fashion accessories','Food and beverages','Health and beauty','Home and lifestyle','Sports and travel']) 
arr_grossIncomePerCategory = np.array([electronicAccessories,fashionAccessories,foodAndbeverages,healthAndBeauty,homeAndlifestyle, sportsAndtravel])
#Creating a data frame containing the product categories and their respecting gross income data
df_grossIncomePerCategory = df = pd.DataFrame({'Product Category':arr_productCategory, 'Gross Income':arr_grossIncomePerCategory})

#Creating numpy arrays: one that contain the name if the products categories, and the other contain the contribution of that product category in terms of gross income in the ciry of Yangon
arr_grossIncomePerCategory_Yangon = np.array([electronicAccessories_Yangon,fashionAccessories_Yangon,foodAndbeverages_Yangon,healthAndBeauty_Yangon,homeAndlifestyle_Yangon, sportsAndtravel_Yangon])
#Creating a data frame containing the product categories and their respecting gross income data for the city of Yangon
df_grossIncomePerCategory_Yangon = df = pd.DataFrame({'Product Category':arr_productCategory, 'Gross Income':arr_grossIncomePerCategory_Yangon})

#Creating numpy arrays: one that contain the name if the products categories, and the other contain the contribution of that product category in terms of gross income in the ciry of Mandalay
arr_grossIncomePerCategory_Mandalay = np.array([electronicAccessories_Mandalay,fashionAccessories_Mandalay,foodAndbeverages_Mandalay,healthAndBeauty_Mandalay,homeAndlifestyle_Mandalay, sportsAndtravel_Mandalay])
#Creating a data frame containing the product categories and their respecting gross income data for the city of Mandalay
df_grossIncomePerCategory_Mandalay = df = pd.DataFrame({'Product Category':arr_productCategory, 'Gross Income':arr_grossIncomePerCategory_Mandalay})

#Creating numpy arrays: one that contain the name if the products categories, and the other contain the contribution of that product category in terms of gross income in the ciry of Naypyitaw
arr_grossIncomePerCategory_Naypyitaw = np.array([electronicAccessories_Naypyitaw,fashionAccessories_Naypyitaw,foodAndbeverages_Naypyitaw,healthAndBeauty_Naypyitaw,homeAndlifestyle_Naypyitaw, sportsAndtravel_Naypyitaw])
#Creating a data frame containing the product categories and their respecting gross income data for the city of Naypyitaw
df_grossIncomePerCategory_Naypyitaw = df = pd.DataFrame({'Product Category':arr_productCategory, 'Gross Income':arr_grossIncomePerCategory_Naypyitaw})

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Creating a bar chart with filtering capabilities 

#Creating the selection boxes:
data_filter = st.radio("Select Data View", ("Profit per Product Category accross Cities",
                                          "Profit per Product Category in Yangon",
                                          "Profit per Product Category in Naypyitaw",
                                          "Profit per Product Category in Mandalay"))

#Establishing conditions for interactivity:
if data_filter == "Profit per Product Category accross Cities":
    df_filter = df_grossIncomePerCategory
    x_label = 'Product Category'
    y_label = 'Gross Income'
    title_filter = 'Gross Income per Product Category'
elif data_filter == "Profit per Product Category in Yangon":
    df_filter = df_grossIncomePerCategory_Yangon
    x_label = 'Product Category'
    y_label = 'Gross Income'
    title_filter = 'Gross Income per Product Category in Yangon'
elif data_filter == "Profit per Product Category in Naypyitaw":
    df_filter = df_grossIncomePerCategory_Naypyitaw
    x_label = 'Product Category'
    y_label = 'Gross Income'
    title_filter = 'Gross Income per Product Category in Naypyitaw'
elif data_filter == "Profit per Product Category in Mandalay":
    df_filter = df_grossIncomePerCategory_Mandalay
    x_label = 'Product Category'
    y_label = 'Gross Income'
    title_filter = 'Gross Income per Product Category in Mandalay'


#Creating a bar chart that shows the gross income of the store (or store in a certain city) per category:
fig_grossIncomeperCategory = px.bar(df_filter, 
                                x=x_label, 
                                y=y_label,
                                color='Product Category',
                                barmode='group') 

fig_grossIncomeperCategory.update_traces(textposition='outside', width=0.25, hoverinfo='text+x')

fig_grossIncomeperCategory.update_layout(uniformtext_minsize=8, title_x=0.5,
                                     title={'text':title_filter,
                                         'x': 0.5,
                                         'xanchor': 'center'},
                                         bargap=1, bargroupgap=1)

st.plotly_chart(fig_grossIncomeperCategory)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Plot 2:

#Importing the second data set: Worls Economic Forum data

st.title('World Economic Forum Data')

st.subheader('Display of the Dataset:')
#df_economicData = pd.read_csv("C:/Users/Lenovo/OneDrive/01_Education/02_AUB/01_Fall2023/MSBA325-Data Visualization and Communication/Projects/DataSets/PopulationDataWorldBank.csv")
df_economicData = pd.read_csv('data/PopulationDataWorldBank.csv')
st.dataframe(df_economicData)

#Creating a data frame with the countries and their GDPs:
df_GDPofCountries = df_economicData.query("`Indicator Name` == 'GDP (current US$)'").query("`Country Code` != 'WLD' and `Country Code` != 'HIC' and `Country Code` != 'OED' and `Country Code` != 'PST' and `Country Code` != 'IBT' and `Country Code` != 'LMY' and `Country Code` != 'MIC' and `Country Code` != 'IBD' and `Country Code` != 'EAS' and `Country Code` != 'UMC' and `Country Code` != 'ECS' and `Country Code` != 'NAC' and `Country Code` != 'LTE' and `Country Code` != 'EAP' and `Country Code` != 'TEA' and `Country Code` != 'EUU' and `Country Code` != 'EMU' and `Country Code` != 'EAR' and `Country Code` != 'LCN' and `Country Code` != 'LMC' and `Country Code` != 'TLA' and `Country Code` != 'LAC' and `Country Code` != 'TEC' and `Country Code` != 'TSA' and `Country Code` != 'SAS' and `Country Code` != 'MEA' and `Country Code` != 'ECA' and `Country Code` != 'ARB' and `Country Code` != 'IDA' and `Country Code` != 'FCS' and `Country Code` != 'TSS'").query("`Country Code` != 'SSF' and `Country Code` != 'SSA'")

#Removing the years where the GDP of one of the top 10 countries is missing
df_GDPofCountries = df_GDPofCountries.drop(columns=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969'])

#Creating a data frame with the GDP of China and the United Staes from 1970 to 2019: 
df_GDPcomparison = df_GDPofCountries.query("`Country Code` == 'USA' or `Country Code` == 'CHN'")

#Dropping irrelevant columns:
df_GDPcomparison = df_GDPcomparison.drop(columns=["Country Code", 'Indicator Code', 'Indicator Name', 'Country Name','2020']) 

#Transposing the data frame
df_GDPcomparison = df_GDPcomparison.T

#Adding headers to the columns
df_GDPcomparison.columns =['China','USA']
    
#Creating an array that contains the period from 1970 to 2019, and adding it to the data fram under a new column called 'Date':
Date = ['1970', '1971', '1972', '1973','1974','1975','1076','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
df_GDPcomparison['Date']=Date

st.subheader('GDP of USA and China from 1970 to 2019:')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Creating the selection boxes 1:
data_filter2 = st.radio("Select Country", ("USA and China",
                                          "USA",
                                          "China"))

#Establishing conditions for interactivity 1: Filtering by Country
if data_filter2 == "USA and China":
    x_label2 = 'Date'
    y_label2 = ['USA','China']
    title_filter2 = 'GDP of USA and China from 1970 to 2019'
elif data_filter2 == "USA":
    x_label2 = 'Date'
    y_label2 = 'USA'
    title_filter2 = 'GDP of USA from 1970 to 2019'
elif data_filter2 == "China":
    x_label2 = 'Date'
    y_label2 = 'China'
    title_filter2 = 'GDP of China from 1970 to 2019'

#-------------------------------

#Establishing conditions for interactivity 2: Filtering by Date

#Setting the Date column to integers to be able to add the slider
df_GDPcomparison['Date'] = df_GDPcomparison['Date'].astype(int)

#Creating the slider with the minimum value being 1970 and the maximum value being 2019
year_range = st.slider(
    "Select year range",
    min_value=1970,
    max_value=df_GDPcomparison['Date'].max(),
    value=(1970, df_GDPcomparison['Date'].max())
)

#Dynamically filtering the dataframe by creating a new one that contain the GDP of the years set by the sliders
df_filteredByYear = df_GDPcomparison[(df_GDPcomparison['Date'] >= year_range[0]) & (df_GDPcomparison['Date'] <= year_range[1])]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Creating a line plot that would display the GDP of China and the US for the period of 1970 to 2019
fig_GDPcomparison = px.line(df_filteredByYear, x=x_label2, y=y_label2,
              title=title_filter2,
              labels={'x':'Date', 'y':'GDP in Dollar'})

fig_GDPcomparison.update_layout(xaxis=dict(linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=12, color='rgb(82,82,82)',),)
                                ,showlegend=True)

#fig_GDPcomparison.update_traces(textposition='outside')
fig_GDPcomparison.update_layout(uniformtext_minsize=8, title_x=0.5,
                                     title={'text':title_filter,
                                         'x': 0.5,
                                         'xanchor': 'center'},
                                         bargap=1, bargroupgap=1)
fig_GDPcomparison.update_xaxes(tickangle=45)

st.plotly_chart(fig_GDPcomparison)
