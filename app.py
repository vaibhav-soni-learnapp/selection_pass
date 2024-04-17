import streamlit as st
import pandas as pd
import requests
from io import StringIO

def send_file(file):
    url = 'https://crates.dev.zero1byzerodha.com/users/file'
    headers = {
        'Authorization': 'Bearer d011a53f5413423fceaf0bf8e9db78dde18dff63'
    }
    files = {
        'file': file.getvalue()
    }
    response = requests.post(url, headers=headers, files=files)
    return response

def categorize_data(df):
    # Categorize data based on the 'status' column
    categories = {
        "ACCEPTED": [],
        "REJECTED": [],
        "WAITLISTED": [],
        "CLAIMED": [],
        "SELECTED": []
    }
    for _, row in df.iterrows():
        status = row['status']
        if status in categories:
            categories[status].append(row.to_dict())
    return categories

def main():
    st.title("CSV File Upload and Categorization")
    uploaded_file = st.file_uploader("Choose a file", type='csv')
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if 'status' not in df.columns:
            st.error("Uploaded CSV must contain a 'status' column.")
            return

        categorized_data = categorize_data(df)
        for status, records in categorized_data.items():
            if records:
                st.subheader(f"Records with status {status}:")
                st.write(pd.DataFrame(records))

        # Sending the file to the server
        if st.button("Send File"):
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            response = send_file(stringio)
            if response.status_code == 200:
                st.success("Success! File has been sent.")
            else:
                st.error(f"Failed to send file: {response.status_code}")

if __name__ == "__main__":
    main()
