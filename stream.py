import streamlit as st
import streamlit.components.v1 as components

def main():
    # Configure page settings
    st.set_page_config(
        page_title="My Website",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for styling
    st.markdown("""
        <style>
        .css-1d391kg {
            padding: 1rem;
        }
        .stButton>button {
            width: 100%;
            background-color: #f0f2f6;
            border: none;
            padding: 15px;
            border-radius: 5px;
            text-align: left;
        }
        .stButton>button:hover {
            background-color: #e0e2e6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Create sidebar navigation
    st.sidebar.title("Navigation")
    
    # Navigation options
    nav_option = st.sidebar.radio("",
        options=["🏠 Home", "📞 Contact Us", "ℹ️ About Us", "🛠️ Services", "🔐 Login"],
        key="nav"
    )

    # Content based on navigation selection
    if nav_option == "🏠 Home":
        st.title("Welcome to Our Website")
        st.write("This is the home page of our website. Feel free to explore!")
        
    elif nav_option == "📞 Contact Us":
        st.title("Contact Us")
        st.write("Get in touch with us!")
        
        # Contact form
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit = st.form_submit_button("Send Message")
            
            if submit:
                st.success("Thanks for reaching out! We'll get back to you soon.")
        
    elif nav_option == "ℹ️ About Us":
        st.title("About Us")
        st.write("Learn more about our company and mission.")
        st.write("We are dedicated to providing excellent service to our customers.")
        
    elif nav_option == "🛠️ Services":
        st.title("Our Services")
        st.write("Explore our range of services:")
        
        # Service cards using columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Service 1")
            st.write("Description of service 1")
            
        with col2:
            st.subheader("Service 2")
            st.write("Description of service 2")
            
    elif nav_option == "🔐 Login":
        st.title("Login")
        
        # Login form
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")
            
            if login_button:
                if username and password:  # Add your authentication logic here
                    st.success("Successfully logged in!")
                else:
                    st.error("Please enter both username and password")

if __name__ == "__main__":
    main()