import streamlit as st
import streamlit.components.v1 as components

def login_signup_form():
    # Custom CSS to ensure proper fitting
    st.markdown("""
        <style>
            /* Remove padding and margin from the main container */
            .stApp {
                padding: 0;
                margin: 0;
            }
            
            /* Hide Streamlit header and footer */
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* Adjust iframe container */
            iframe {
                width: 100vw;
                height: 100vh;
                border: none;
                padding: 0;
                margin: 0;
            }
            
            /* Remove default Streamlit padding */
            .block-container {
                padding: 0;
                margin: 0;
                max-width: 100%;
            }
            
            /* Ensure no scrollbars appear */
            body {
                overflow: hidden;
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <script src="https://kit.fontawesome.com/64d58efce2.js" crossorigin="anonymous"></script>
        <style>
            @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700;800&display=swap");
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body, html {
                width: 100%;
                height: 100%;
                overflow: hidden;
            }

            body, input {
                font-family: "Poppins", sans-serif;
            }

            .container {
                position: relative;
                width: 100%;
                height: 100vh;
                background-color: #fff;
                overflow: hidden;
            }

            .forms-container {
                position: absolute;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
            }

            .signin-signup {
                position: absolute;
                top: 50%;
                transform: translate(-50%, -50%);
                left: 75%;
                width: 50%;
                transition: 1s 0.7s ease-in-out;
                display: grid;
                grid-template-columns: 1fr;
                z-index: 5;
            }

            /* Rest of your existing CSS remains the same */
            [Your existing CSS here...]

            /* Modified media queries for better responsiveness */
            @media (max-width: 870px) {
                .container {
                    min-height: 100vh;
                    height: 100%;
                }
                
                .signin-signup {
                    width: 100%;
                    top: 75%;
                    transform: translate(-50%, -50%);
                    transition: 1s 0.8s ease-in-out;
                    padding: 0 1rem;
                }
                
                .panels-container {
                    grid-template-columns: 1fr;
                    grid-template-rows: 1fr 2fr 1fr;
                }
                
                .panel {
                    padding: 1rem;
                }
                
                .container::before {
                    width: 130%;
                    height: 130%;
                    transform: translateX(-50%);
                    left: 30%;
                    bottom: 68%;
                    right: initial;
                    top: initial;
                }
                
                .image {
                    width: 200px;
                    max-width: 100%;
                }
            }

            @media (max-width: 570px) {
                form {
                    padding: 0 1rem;
                }
                
                .image {
                    display: none;
                }
                
                .panel .content {
                    padding: 0.5rem 1rem;
                }
                
                .container {
                    padding: 1rem;
                }
                
                .panel h3 {
                    font-size: 1.2rem;
                }
                
                .panel p {
                    font-size: 0.9rem;
                    padding: 0.5rem 0;
                }
            }
        </style>
    </head>
    <body>
        <!-- Your existing HTML content remains the same -->
        [Your existing HTML here...]
    </body>
    </html>
    """

    # Render the component with adjusted height
    components.html(html_content, height=1000, scrolling=False)

def main():
    st.set_page_config(
        page_title="Sign In & Sign Up Form",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    login_signup_form()

if __name__ == "__main__":
    main()