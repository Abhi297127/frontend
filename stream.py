import streamlit as st

def main():
    # Configure page settings
    st.set_page_config(
        page_title="My Website",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for top navigation
    st.markdown("""
        <style>
        .stButton button {
            background-color: transparent;
            border: none;
            color: #4F8BF9;
            padding: 10px 15px;
            cursor: pointer;
        }
        .stButton button:hover {
            color: #1f4068;
            text-decoration: underline;
        }
        .nav-container {
            display: flex;
            justify-content: space-evenly;
            align-items: center;
            padding: 1rem 0;
            background-color: #f8f9fa;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Create top navigation using columns
    with st.container():
        st.markdown('<div class="nav-container">', unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            home = st.button("🏠 Home")
        with col2:
            contact = st.button("📞 Contact Us")
        with col3:
            about = st.button("ℹ️ About Us")
        with col4:
            services = st.button("🛠️ Services")
        with col5:
            login = st.button("🔐 Login")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Handle navigation
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    # Update page state based on button clicks
    if home:
        st.session_state.page = 'home'
    elif contact:
        st.session_state.page = 'contact'
    elif about:
        st.session_state.page = 'about'
    elif services:
        st.session_state.page = 'services'
    elif login:
        st.session_state.page = 'login'

    # Display content based on page state
    if st.session_state.page == 'home':
        st.title("Welcome to Our Website")
        st.write("This is the home page of our website. Feel free to explore!")
        
    elif st.session_state.page == 'contact':
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
        
    elif st.session_state.page == 'about':
        st.title("About Us")
        st.write("Learn more about our company and mission.")
        st.write("We are dedicated to providing excellent service to our customers.")
        
    elif st.session_state.page == 'services':
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
            
    elif st.session_state.page == 'login':
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