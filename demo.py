import streamlit as st
import base64

def get_base64(png_file):
    with open(png_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpeg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    set_background("D:\py_llm\law\magicpattern-mesh-gradient-1715052764545.png")
    st.title("Streamlit App with Background Image")
    st.write("This is a Streamlit app with a background image!")

if __name__ == "__main__":
    main()
