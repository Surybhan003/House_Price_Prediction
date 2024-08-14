import streamlit as st
import pickle

# Title of the app
st.title('House Price Prediction')
pipe = pickle.load(open('LinearRegressionModel.pkl','rb'))

# Input fields

area = st.number_input("Area in square feet", min_value=0)
number_of_rooms = st.number_input("Number of Rooms", min_value=0)
has_yard = st.checkbox("Has Yard?")
has_pool = st.checkbox("Has Pool?")
floors = st.number_input("Number of Floors", min_value=1)
city_code = st.text_input("City Code")
city_part_range = st.number_input("City Part Range", min_value=0)
num_prev_owners = st.number_input("Number of Previous Owners", min_value=0)
is_new_built = st.checkbox("Is New Built?")
has_storm_protector = st.checkbox("Has Storm Protector?")
has_storage_room = st.checkbox("Has Storage Room?")
has_guest_room = st.number_input("Has Guest Room?", min_value=0)



# Submit button
if st.button('Predict'):
    print(has_yard)
    print(int(has_pool))
    price = pipe.predict([[area, number_of_rooms, int(has_yard), int(has_pool), floors, int(city_code), city_part_range, num_prev_owners, int(is_new_built), int(has_storm_protector), int(has_storage_room), has_guest_room]])
    st.write(price)
    # st.success('Form submitted successfully!')