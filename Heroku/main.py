from pathlib import Path
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=False)

st.header(":coffee: Mazinger Virtual Coffee Shop!:coffee:")

#Greet your customer and ask your customer name
st.session_state['name'] = st.text_input("Hi, my name is Karen. What is your name?")

if st.session_state['name'].lower() == "alison":
    evil_status = st.text_input("Are you evil?")
    good_deeds = st.number_input("How many good deeds have you done today?", min_value=0)
    if evil_status.lower() == "yes" and good_deeds < 4:
        st.markdown("You're not welcome here Alison!! Get out!!", unsafe_allow_html=False)
    else:
        evil_status = st.text_input("Are you sure?")
        if evil_status.lower() == "no":
            st.markdown(f"You're not welcome here {st.session_state['name']}!! Get out!!", unsafe_allow_html=False)
        else:
            st.markdown("Oh, so you must be one of the good not evil Alison, I guess you can come in. But wait...", unsafe_allow_html=False)
else:
    st.markdown(f"Hello, {st.session_state['name']}, thank you so much for coming in today.", unsafe_allow_html=False)

# Initialize beard_length
beard_length = 0

#Ask if the person has a beard
has_beard = st.text_input("Do you have a beard?")
if has_beard.lower() == "no":
  st.markdown("Get out, and come back when you grow one!!", unsafe_allow_html=False)
else:
  beard_length = st.number_input("Nice beard, How Long is it?", min_value=0)

#How long is the beard
if beard_length >= 2:
  st.markdown("You can go in to the front of the line", unsafe_allow_html=False)
else:
  st.markdown("Get out, and come back when you have a beard longer than 2 inch!!", unsafe_allow_html=False)

st.subheader("Below is our menu:")

#Coffee menu
menu = "Black Coffee $5, Americano $6, Espresso $8, Latte $9, Cappuccino $10, Frappuccino $11, Flat White $9
