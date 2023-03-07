import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl as ex


# PAGE TITLE
st.set_page_config(page_title = "Data Visualization App",
                   page_icon=":bar_chart:" , 
                   layout = 'wide')

# TITLE OF THE APP
st.title(":bar_chart: Data Visualization App")

# SIDEBAR OF THE APP
st.sidebar.subheader("Visualization Setting")

# FILE UPLOAD SETUP
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel File." ,
                         type=['csv', 'xlsx'])

global df

if uploaded_file is not None :
    print(uploaded_file)
    print('hello')

    try:
        df = pd.read_csv(uploaded_file)

    except Exception as e:
        print(e)
        df = pd.read_excel(io = uploaded_file,engine='openpyxl')

global numeric_columns
global string_columns

try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    string_columns = df.select_dtypes('object').columns

except Exception as e:
    print(e)
    st.write('Please upload the file to the appliation.')



# SELECT WIDGET IN THE SIDEBAR

if uploaded_file is not None :

    # row_select = st.sidebar.number_input(
    #     label='Number of rows', value=1,
    #     min_value=1, max_value=len(df), 
    # )
    
    # file = st.table(df.head(row_select))

    chart_select = st.sidebar.selectbox(
        label='Select the Chart type' ,
        options=['Linechart', 'Histogram', 'Piechart', 'Scatterplots']
    )

    if chart_select == 'Scatterplots' :
        
        st.sidebar.subheader("Scatterplot Settings")
        
        try :
            x_value = st.sidebar.selectbox('X-axis', options=numeric_columns)
            y_value = st.sidebar.selectbox('Y-axis', options=numeric_columns)
            plot = px.scatter(data_frame=df, x=x_value, y=y_value, title='Scatter-Plots')
            # DISPLAY THE CHART
            st.plotly_chart(plot)

        except Exception as e :
            print(e)

    elif chart_select == 'Linechart' :
        
        st.sidebar.subheader("Linechart Settings")
        
        try :
            x_value = st.sidebar.selectbox('X-axis', options=numeric_columns)
            y_value = st.sidebar.selectbox('Y-axis', options=numeric_columns)
            plot = px.line(data_frame=df, x=x_value, y=y_value, title='Line Chart')
            # DISPLAY THE CHART
            st.plotly_chart(plot)

        except Exception as e :
            print(e)

    elif chart_select == 'Piechart' :
        
        st.sidebar.subheader("Piechart Settings")
        
        try :
            x_value = st.sidebar.selectbox('Values', options=numeric_columns)
            y_value = st.sidebar.selectbox('Names', options=string_columns)
            plot = px.pie(data_frame=df, values=x_value, names=y_value, title='Pie Chart')
            # DISPLAY THE CHART
            st.plotly_chart(plot)

        except Exception as e :
            print(e)

    elif chart_select == 'Histogram' :
        
        st.sidebar.subheader("Histogram Settings")
        
        try :
            x_value = st.sidebar.selectbox('X-axis', options=numeric_columns)
            plot = px.histogram(data_frame=df, x=x_value, title='Histogram')
            # DISPLAY THE CHART
            st.plotly_chart(plot)

        except Exception as e :
            print(e)



hide_st_style = """
                <style>
                #MainMenu{visibility:hidden;}
                footer{visibility:hidden;}
                header{visibility:hidden;}
                .e1fqkh3o4{padding:2rem 1rem}
                .egzxvld4{padding:1rem auto}
                </style>
                """

st.markdown(hide_st_style, unsafe_allow_html=True)