import streamlit as st
import pickle

# Loading the saved model
model = pickle.load(open('C:/Users/SAMSIV/Downloads/cus_conver_XGBC_model.pkl', 'rb'))


# creating a function for prediction
def prediction(input_data):
    # build the prediction model
    model_pred = model.predict([input_data])

    if model_pred == [0]:
        return 'Client Not subscribed the Insurance'
    else:
        return 'Client subscribed to the Insurance'


# create the function for collecting the data from users

def main():
    # giving a title
    st.title('Customer Conversion Prediction Web Application')

    # getting the input from users
    age1 = st.text_input("Enter Person Age")

    # show a dropdown menu for selecting the occupation
    job1 = st.selectbox('Select the ocuupation', ['blue-collar', 'entrepreneur', 'housemaid', 'services', 'technician',
                                                  'self-employed', 'admin.', 'management', 'unemployed', 'retired',
                                                  'student', 'unknown'])

    # show a dropdown menu for selecting the marital status
    marital1 = st.selectbox('Select Marital status', ["divorced", "married", "single"])

    # show a dropdown menu for selecting the Education Qualification
    education1 = st.selectbox('Select Education qualification', ["primary", "secondary", "unknown", "tertiary"])

    # show a dropdown menu for selecting the Call Type
    call_type1 = st.selectbox('Select last contact communication type', ["unknown", "telephone", "cellular"])

    # show a dropdown menu for selecting the Month
    month1 = st.selectbox('Select the month',
                          ['may', 'jul', 'jan', 'nov', 'jun', 'aug', 'feb', 'apr', 'oct', 'sep', 'dec', 'mar'])

    day1 = 0
    # select the date
    if month1 in ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']:
        day1 = st.selectbox('Select the date',
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                             26, 27, 28, 29, 30, 31])
    elif month1 in ['apr', 'jun', 'sep', 'nov']:
        day1 = st.selectbox('Select the date',
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                             26, 27, 28, 29, 30])
    elif month1 == 'feb':
        day1 = st.selectbox('Select the date',
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                             26, 27, 28])

    # adding the text input for duration
    dur1 = st.text_input('Last contact duration (in seconds)')

    # adding the text input for number of calls
    num_calls1 = st.text_input('Enter the Number of Calls')

    # show a dropdown menu for previous outcome
    prev_outcome1 = st.selectbox('Select outcome of the previous marketing campaign',
                                 ["unknown", "failure", "other", "success"])

    # encoding datas
    job = {'blue-collar': 0, 'unknown': 0, 'entrepreneur': 1, 'housemaid': 2, 'services': 3, 'technician': 4,
           'self-employed': 5, 'admin.': 6, 'management': 7, 'unemployed': 8, 'retired': 9, 'student': 10}
    marital = {"divorced": 0, "married": 1, "single": 2}
    education = {"primary": 0, "secondary": 1, "unknown": 2, "tertiary": 3}
    call_type = {"unknown": 0, "telephone": 1, "cellular": 2}
    month = {'may': 0, 'jul': 1, 'jan': 2, 'nov': 3, 'jun': 4, 'aug': 5, 'feb': 6, 'apr': 7, 'oct': 8, 'sep': 9,
             'dec': 10, 'mar': 11}
    prev_outcome = {"unknown": 0, "failure": 1, "other": 2, "success": 3}
    # code for prediction
    results = ''

    # creating button for prediction
    if st.button('Prediction Results'):
        results = prediction(
            [int(age1), job[job1], marital[marital1], education[education1], call_type[call_type1], int(day1),
             month[month1], int(dur1), int(num_calls1), prev_outcome[prev_outcome1]])
    st.success(results)


if __name__ == '__main__':
    main()