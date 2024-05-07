import streamlit as st
import base64

# Function to convert image file to base64
def get_base64(png_file):
    with open(png_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Set the background image
def set_background(png_file):
    bin_str = get_base64(png_file)
    background_image = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: 100vw 100vh;  /* This sets the size to cover 100% of the viewport width and height */
        background-position: center;  
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(background_image, unsafe_allow_html=True)

# Main function
def main():
    original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;">Streamlit CSS Styling✨ </h1>'
    st.markdown(original_title, unsafe_allow_html=True)

    # Set the background image
    set_background("Clouds.jpg")

    # Text input with custom styling
    st.text_input("", placeholder="Streamlit CSS ")

    # Custom input styling
    input_style = """
    <style>
    input[type="text"] {
        background-color: transparent;
        color: #a19eae;  /* This changes the text color inside the input box */
    }
    div[data-baseweb="base-input"] {
        background-color: transparent !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }
    </style>
    """
    st.markdown(input_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
