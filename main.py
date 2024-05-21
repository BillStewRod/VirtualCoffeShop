from pathlib import Path
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

st.header(":coffee: Mazinger Virtual Coffee Shop!:coffee:")

#Greet your customer and ask your customer name
st.session_state['name'] = st.text_input("Hi, my name is Karen. What is your name?")

if st.session_state['name'].lower() == "alison":
    evil_status = st.text_input("Are you evil?")
    good_deeds = st.number_input("How many good deeds have you done today?", min_value=0)
    if evil_status.lower() == "yes" and good_deeds < 4:
        st.markdown("You're not welcome here Alison!! Get out!!")
    else:
        evil_status = st.text_input("Are you sure?")
        if evil_status.lower() == "no":
            st.markdown(f"You're not welcome here {st.session_state['name']}!! Get out!!")
        else:
            st.markdown("Oh, so you must be one of the good not evil Alison, I guess you can come in. But wait...")
else:
    st.markdown(f"Hello, {st.session_state['name']}, thank you so much for coming in today.")

# Initialize beard_length
beard_length = 0

#Ask if the person has a beard
has_beard = st.text_input("Do you have a beard?")
if has_beard.lower() == "no":
  st.markdown("Get out, and come back when you grow one!!")
else:
  beard_length = st.number_input("Nice beard, How Long is it?", min_value=0)

#How long is the beard
if beard_length >= 2:
  st.markdown("You can go in to the front of the line")
else:
  st.markdown("Get out, and come back when you have a beard longer than 2 inch!!")

st.subheader("Below is our menu:")

#Coffee menu
menu = "Black Coffee $5, Americano $6, Espresso $8, Latte $9, Cappuccino $10, Frappuccino $11, Flat White $9, Cafecito $200, Cafe con Leche $300"
menu_list = menu.split(", ")

# Display the menu as a list
for item in menu_list:
    st.markdown(item)

#Ask the customer what they would like from the menu and store it in the variable order.
order = st.selectbox(f"{st.session_state['name']}, what can i make you today?", menu_list)

#Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity =  st.number_input("How many coffees would you like?", min_value=1)

prices = {
"Black Coffee $5": 5,
"Americano $6": 6,
"Espresso $8": 8,
"Latte $9": 9,
"Cappuccino $10": 10,
"Frappuccino $13": 13,
"Flat White $9": 9,
"Cafecito $200": 200,
"Cafe con Leche $300": 300
}

# Check if the order is in the menu
if order not in prices:
    st.markdown("Sorry, that item is not on the menu. Please choose from above menu:")
else:
    #Calculate the customer's total
    total = prices[order] * quantity

    #Give the customer their total
    st.markdown(f"Sounds good {st.session_state['name']}! Thank You for your order. Your total is: ${total}")

    #Final statement
    st.markdown(f"We'll have your {quantity} :coffee: {order} ready for you in a moment.")
