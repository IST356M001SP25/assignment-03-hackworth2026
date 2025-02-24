import streamlit as st
import packaging

def main():
    st.title("Process One Package")

    pkg = st.text_input("Enter package data:")

    if pkg:
        parsed_pkg = packaging.parse_packaging(pkg)
        total = packaging.calc_total_units(parsed_pkg)
        unit = packaging.get_unit(parsed_pkg)

        st.text(parsed_pkg)
        for item in parsed_pkg:
            name = list(item.keys())[0]
            size = list(item.values())[0]
            st.info(f"{name} ➡️ {size}")

        st.success(f"Total 📦 Size: {total} {unit}")

if __name__ == "__main__":
    main()
