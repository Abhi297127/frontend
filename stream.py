import streamlit as st
import streamlit.components.v1 as components

def main():
    # Set page config
    st.set_page_config(page_title="Login System", layout="centered")
    
    # Custom CSS
    st.markdown("""
        <style>
        .stButton > button {
            width: 100%;
            background-color: #5995fd;
            color: white;
            border-radius: 25px;
            height: 45px;
            border: none;
            font-weight: 600;
        }
        .stButton > button:hover {
            background-color: #4d84e2;
        }
        .css-1d391kg {
            padding: 2rem 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Create tabs for login and signup
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])
    
    with tab1:
        st.header("Sign In")
        
        # Login form
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            login_button = st.button("Login")
        
        # Social login options
        st.markdown("<p style='text-align: center; color: #666;'>Or Sign in with</p>", unsafe_allow_html=True)
        social_col1, social_col2, social_col3, social_col4 = st.columns(4)
        
        with social_col1:
            st.button("📘 FB")
        with social_col2:
            st.button("🐦 Twitter")
        with social_col3:
            st.button("🔍 Google")
        with social_col4:
            st.button("💼 LinkedIn")
    
    with tab2:
        st.header("Sign Up")
        
        # Sign up form
        new_username = st.text_input("Choose Username", placeholder="Enter a username")
        email = st.text_input("Email", placeholder="Enter your email")
        new_password = st.text_input("Choose Password", type="password", placeholder="Enter a password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            signup_button = st.button("Sign Up")

        # Social signup options
        st.markdown("<p style='text-align: center; color: #666;'>Or Sign up with</p>", unsafe_allow_html=True)
        social_col1, social_col2, social_col3, social_col4 = st.columns(4)
        
        with social_col1:
            st.button("📘 FB ", key="fb_signup")
        with social_col2:
            st.button("🐦 Twitter ", key="twitter_signup")
        with social_col3:
            st.button("🔍 Google ", key="google_signup")
        with social_col4:
            st.button("💼 LinkedIn ", key="linkedin_signup")

    # Add login/signup logic here
    if login_button:
        if username and password:  # Add your authentication logic here
            st.success("Logged in successfully!")
        else:
            st.error("Please enter both username and password")
            
    if signup_button:
        if new_username and email and new_password and confirm_password:
            if new_password == confirm_password:
                st.success("Account created successfully!")
            else:
                st.error("Passwords don't match")
        else:
            st.error("Please fill in all fields")

if __name__ == "__main__":
    main()