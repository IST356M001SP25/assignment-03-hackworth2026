import streamlit as st
import packaging
from io import StringIO
import json
'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
def process_file(file_content):
    lines = file_content.split('\n')
    for line in lines:
        package = line.strip()
        package_size = len(package)
        st.write(f"Parsed Package: {package}")
        st.write(f"Total Package Size: {package_size}")

def main():
    st.title("Packaging Information")
    file = st.file_uploader("Upload a file", type=["txt"])
    if file is not None:
        file_content = file.read().decode('utf-8')
        process_file(file_content)

if __name__ == "__main__":
    main()
