import streamlit as st
import requests

st.set_page_config(page_title="Product Barcode Finder", layout="centered")
st.title("🔍 Product Barcode Finder")

st.write("Enter the product name and brand to retrieve the barcode (UPC/GTIN).")

# User inputs
product_name = st.text_input("Product Name", placeholder="e.g., Niacinamide Serum")
brand = st.text_input("Brand Name", placeholder="e.g., The Ordinary")

def get_barcode_via_api(product_name, brand):
    url = "https://api.upcitemdb.com/prod/trial/search"
    params = {
        "s": product_name,
        "brand": brand
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("code") == "OK" and data.get("items"):
            item = data["items"][0]
            return item.get("gtin") or item.get("upc")
        else:
            return "No barcode found for this product."
    except requests.RequestException as e:
        return f"Request failed: {e}"

# Trigger search
if st.button("Get Barcode"):
    if product_name and brand:
        with st.spinner("Fetching barcode..."):
            barcode = get_barcode_via_api(product_name, brand)
            st.success(f"Barcode: {barcode}")
    else:
        st.warning("Please enter both product name and brand.")
