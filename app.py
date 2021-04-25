import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import  pickle
import datetime

st.title("Flight Fare Prediction")
nav = st.sidebar.radio("Navigation", ["Home", "Prediction"])

data = pd.read_excel("plot_data.xlsx")
Airline = data.groupby("Airline")["Price"].mean()
Duration = data.groupby("Duration")["Price"].mean()

Airline = pd.DataFrame({"Airline":Airline.index, "Average Fare":Airline.values})
Duration = pd.DataFrame({"Duration":Duration.index, "Average Fare":Duration.values})

if nav == "Home":
    st.image("Flight.jpg", width=700)
    st.header("Get Some Insights of Fare price")
    graph = st.selectbox("Select a option to get Insights", ["Average FlightFare by Airline",
                                                     "Average FlightFare by Duration"])
    if graph == "Average FlightFare by Airline":
        fig = px.bar(Airline, x= "Airline", y = "Average Fare", title= "Average FlightFare by different Airlines")
        st.plotly_chart(fig)

    if graph == "Average FlightFare by Duration":
        fig_1 = px.scatter(Duration, x="Duration", y="Average Fare", title="Average FlightFare by Duration of Flight")
        st.plotly_chart(fig_1)



if nav == "Prediction":
    st.header("Fill the fields to get Fare")
    journey_date = st.date_input("Enter Journey date")
    Dep_time = st.time_input("Enter Departure time", value = datetime.time(10,00) )
    Arr_time = st.time_input("Enter Arrival time", value = datetime.time(12,00) )
    Duration = st.number_input("Enter Duration of Flight(In hours)", min_value= 0.50, value= 1.00)
    Airline_service = st.selectbox("Enter your Airline Service", list(Airline["Airline"]))
    Boarding_city = st.selectbox("Enter your Boarding city", ['Banglore', 'Kolkata',
                                                              'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Enter your Destination", ['New Delhi', 'Banglore',
                                                          'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])
    Total_Stops = st.selectbox("Enter number of stops", ['non-stop', '1 stop',
                                                         '2 stops', '3 stops', 'More than 3 stops'])
    Add_info = st.selectbox("Enter Additional info", ["No Info", "Business Class", "In-flight meal not included"])



    journey_day = pd.to_datetime(journey_date).day
    journey_month = pd.to_datetime(journey_date).month
    Dep_hour = Dep_time.hour
    Dep_min = Dep_time.minute
    Arr_hour = Arr_time.hour
    Arr_min = Arr_time.minute
    #For Airline Service
    if Airline_service == 'Air India':
        Airline_AirIndia  = 1
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0

    elif Airline_service == 'Jet Airways':
        Airline_AirIndia  = 0
        Airline_JetAirways = 1
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0

    elif Airline_service == 'Jet Airways Business':
        Airline_AirIndia  = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 1
        Airline_MultipleCarriers = 0

    elif Airline_service == 'Jet Airways Business':
        Airline_AirIndia  = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 1
        Airline_MultipleCarriers = 0

    elif Airline_service == 'Multiple carriers':
        Airline_AirIndia  = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 1

    else :
        Airline_AirIndia = 0
        Airline_JetAirways = 0
        Airline_JetAirwaysBusiness = 0
        Airline_MultipleCarriers = 0

    #For Source
    if Boarding_city == 'Delhi':
        Delhi_b = 1
        Kolkata_b = 0
        Mumbai_b = 0

    elif Boarding_city == 'Kolkata':
        Delhi_b = 0
        Kolkata_b = 1
        Mumbai_b = 0

    elif Boarding_city == 'Mumbai':
        Delhi_b = 0
        Kolkata_b = 0
        Mumbai_b = 1

    else:
        Delhi_b = 0
        Kolkata_b = 0
        Mumbai_b = 0

    #For Destination

    if Destination == 'Cochin':
        Cochin_d    =  1
        Delhi_d     =  0
        Hyderabad_d =  0
        Kolkata_d   =  0
        NewDelhi_d  =  0

    elif Destination == 'Delhi':
        Cochin_d    =  0
        Delhi_d     =  1
        Hyderabad_d =  0
        Kolkata_d   =  0
        NewDelhi_d  =  0

    elif Destination == 'Hyderabad':
        Cochin_d    =  0
        Delhi_d     =  0
        Hyderabad_d =  1
        Kolkata_d   =  0
        NewDelhi_d  =  0

    elif Destination == 'Kolkata':
        Cochin_d    =  0
        Delhi_d     =  0
        Hyderabad_d =  0
        Kolkata_d   =  1
        NewDelhi_d  =  0

    elif Destination == 'New Delhi':
        Cochin_d    =  0
        Delhi_d     =  0
        Hyderabad_d =  0
        Kolkata_d   =  0
        NewDelhi_d  =  1

    else:
        Cochin_d    =  0
        Delhi_d     =  0
        Hyderabad_d =  0
        Kolkata_d   =  0
        NewDelhi_d  =  0

    #For Total Stops

    if Total_Stops == '1 stop':
        one_stop   = 1
        two_stop   = 0
        three_stop = 0

    elif Total_Stops == '2 stops':
        one_stop   = 0
        two_stop   = 1
        three_stop = 0

    elif Total_Stops == '3 stops':
        one_stop   = 0
        two_stop   = 0
        three_stop = 1

    else:
        one_stop   = 0
        two_stop   = 0
        three_stop = 0

    #For Additional Info
    if Add_info == "Business Class":
        Business_Class = 1
        No_meal        = 0

    elif Add_info == "In-flight meal not included":
        Business_Class = 0
        No_meal        = 1

    else:
        Business_Class = 0
        No_meal        = 0

    # For Month

    if journey_month == 3:
        March = 1
        April = 0
        May   = 0
        June  = 0

    elif journey_month == 4:
        March = 0
        April = 1
        May   = 0
        June  = 0

    elif journey_month == 5:
        March = 0
        April = 0
        May   = 1
        June  = 0

    elif journey_month == 6:
        March = 0
        April = 0
        May   = 0
        June  = 1

    else:
        March = 0
        April = 0
        May   = 0
        June  = 0

    model = pickle.load(open('finalized_model.sav', 'rb'))

    input_grid = [journey_day, Dep_hour, Dep_min, Arr_hour, Arr_min, Airline_AirIndia, Airline_JetAirways,
                  Airline_JetAirwaysBusiness, Airline_MultipleCarriers, Delhi_b, Kolkata_b, Mumbai_b,
                  Cochin_d, Delhi_d, Hyderabad_d, Kolkata_d, NewDelhi_d, Business_Class, No_meal,
                  one_stop, two_stop, three_stop, Duration, March, April, May, June]



    final_input = np.array(input_grid).reshape(1,-1)


    sub = st.button("Submit")

    if sub:
        predict = round(float(model.predict(final_input)),2)
        st.subheader("The final Flight Fare is:")
        st.header(predict)







