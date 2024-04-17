import streamlit as st
import requests
import pandas as pd

def upload_file(file):
    url = "https://crates.zero1byzerodha.com/users/file"
    files = {'file': (file.name, file, 'text/csv')}
    headers = {'Authorization': 'Bearer d011a53f5413423fceaf0bf8e9db78dde18dff63'}
    response = requests.post(url, headers=headers, files=files)
    return response.text

def main():
    st.title("📧 Email & 💬 WhatsApp Messages")
    st.header("⚡Zero1 Fest 💥")
    st.subheader("👤Upload Users")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        # Show file content
        st.write("Uploaded File Content:")
        dataframe = pd.read_csv(uploaded_file)
        st.dataframe(dataframe)
        # Perform the file upload
        result = upload_file(uploaded_file)
        # Display the result
        st.write("Server Response:")
        st.text(result)

if __name__ == "__main__":
    main()
