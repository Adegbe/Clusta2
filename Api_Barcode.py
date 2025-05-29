import streamlit as st
import requests

st.title("Get Product Barcode via UPC Item DB API")

product_name = st.text_input("Enter product name (e.g., Niacinamide Serum)")
brand_name = st.text_input("Enter brand name (e.g., The Ordinary)")

def get_barcode_via_api(product_name, brand):
    url = "https://api.upcitemdb.com/prod/trial/search"
    params = {
        "name": product_name,
        "brand": brand,
        "category": "skincare"
    }
    response = requests.get(url, params=params).json()
    if response.get("code") == "OK" and response.get("items"):
        return response["items"][0].get("barcode")
    return None

if product_name and brand_name:
    barcode = get_barcode_via_api(product_name, brand_name)
    if barcode:
        st.success(f"UPC Barcode: {barcode}")
    else:
        st.error("No barcode found. Try a different name or brand.")
