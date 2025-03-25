import streamlit as st

def pizzahut():
    # Display welcome message
    st.title("Welcome to PYTHON Pizza!")
    
    # Pizza prices
    small_pizza = 15
    medium_pizza = 20
    large_pizza = 25

    # Topping prices
    small_pepperoni = 2
    medium_large_pepperoni = 3
    extra_cheese_price = 1

    # Create UI elements
    size = st.selectbox("What size pizza would you like?", ["S", "M", "L"])
    add_pepperoni = st.checkbox("Would you like pepperoni?")
    extra_cheese = st.checkbox("Would you like extra cheese?")

    # Calculate total bill
    total = 0

    # Add base pizza price
    if size == "S":
        total += small_pizza
    elif size == "M":
        total += medium_pizza
    else:  # "L"
        total += large_pizza

    # Add pepperoni cost if selected
    if add_pepperoni:
        if size == "S":
            total += small_pepperoni
        else:  # medium or large
            total += medium_large_pepperoni

    # Add extra cheese cost if selected
    if extra_cheese:
        total += extra_cheese_price

    # Display the total bill
    if st.button("Calculate Total"):
        st.write(f"Your total bill is: ${total}")

# Run the app
if __name__ == "__main__":
    pizzahut()
