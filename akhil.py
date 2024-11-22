import streamlit as st
import math

def Elec_Power(V, I, PF):
    """
    Calculate the active power (P), reactive power (Q), and apparent power (S).
    """
    # Calculate apparent power
    S = V * I
    # Calculate active power
    P = V* I * PF
    # Calculate reactive power
    Q = V * I * math.sqrt(1 - PF**2)
    return P, Q, S

# Streamlit App
st.title("2205a21063-ps2")
st.header("This application is useful to calculate the active power(P),reactive power(Q) and apparent power(S) based on input parameters such as voltage,current, and powerfactor")

# Input Fields

col1,col2=st.columns(2)
with col1:
 V = st.number_input("Input voltage (v)", min_value=0.0, step=0.1)
 I = st.number_input("current", min_value=0.0, step=0.1)
 PF = st.number_input("Power Factor (pf)", min_value=0.0, max_value=1.0, step=0.01)

# Button to calculate

 if st.button("Calculate"):
    try:
      with col2:
        P, Q, S = Elec_Power(V, I, PF)
        st.success(f"Active Power (P): {P:.2f} Watts")
        st.success(f"Reactive Power (Q): {Q:.2f} VARs")
        st.success(f"Apparent Power (S): {S:.2f} VA")
    except ValueError as e:
        st.error(str(e))
        
        