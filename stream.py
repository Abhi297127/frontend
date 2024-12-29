import streamlit as st
import streamlit.components.v1 as components

def login_signup_form():
    # HTML content with embedded CSS and JavaScript
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

            body, input {
                font-family: "Poppins", sans-serif;
            }

            .container {
                position: relative;
                width: 100%;
                background-color: #fff;
                min-height: 100vh;
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

            form {
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
                padding: 0rem 5rem;
                transition: all 0.2s 0.7s;
                overflow: hidden;
                grid-column: 1 / 2;
                grid-row: 1 / 2;
            }

            form.sign-up-form {
                opacity: 0;
                z-index: 1;
            }

            form.sign-in-form {
                z-index: 2;
            }

            .title {
                font-size: 2.2rem;
                color: #444;
                margin-bottom: 10px;
            }

            .input-field {
                max-width: 380px;
                width: 100%;
                background-color: #f0f0f0;
                margin: 10px 0;
                height: 55px;
                border-radius: 55px;
                display: grid;
                grid-template-columns: 15% 85%;
                padding: 0 0.4rem;
                position: relative;
            }

            .input-field i {
                text-align: center;
                line-height: 55px;
                color: #acacac;
                transition: 0.5s;
                font-size: 1.1rem;
            }

            .input-field input {
                background: none;
                outline: none;
                border: none;
                line-height: 1;
                font-weight: 600;
                font-size: 1.1rem;
                color: #333;
            }

            .input-field input::placeholder {
                color: #aaa;
                font-weight: 500;
            }

            .social-text {
                padding: 0.7rem 0;
                font-size: 1rem;
            }

            .social-media {
                display: flex;
                justify-content: center;
            }

            .social-icon {
                height: 46px;
                width: 46px;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0 0.45rem;
                color: #333;
                border-radius: 50%;
                border: 1px solid #333;
                text-decoration: none;
                font-size: 1.1rem;
                transition: 0.3s;
            }

            .social-icon:hover {
                color: #4481eb;
                border-color: #4481eb;
            }

            .btn {
                width: 150px;
                background-color: #5995fd;
                border: none;
                outline: none;
                height: 49px;
                border-radius: 49px;
                color: #fff;
                text-transform: uppercase;
                font-weight: 600;
                margin: 10px 0;
                cursor: pointer;
                transition: 0.5s;
            }

            .btn:hover {
                background-color: #4d84e2;
            }

            .panels-container {
                position: absolute;
                height: 100%;
                width: 100%;
                top: 0;
                left: 0;
                display: grid;
                grid-template-columns: repeat(2, 1fr);
            }

            .container:before {
                content: "";
                position: absolute;
                height: 2000px;
                width: 2000px;
                top: -10%;
                right: 48%;
                transform: translateY(-50%);
                background-image: linear-gradient(-45deg, #4481eb 0%, #04befe 100%);
                transition: 1.8s ease-in-out;
                border-radius: 50%;
                z-index: 6;
            }

            .image {
                width: 100%;
                transition: transform 1.1s ease-in-out;
                transition-delay: 0.4s;
            }

            .panel {
                display: flex;
                flex-direction: column;
                align-items: flex-end;
                justify-content: space-around;
                text-align: center;
                z-index: 6;
            }

            .left-panel {
                pointer-events: all;
                padding: 3rem 17% 2rem 12%;
            }

            .right-panel {
                pointer-events: none;
                padding: 3rem 12% 2rem 17%;
            }

            .panel .content {
                color: #fff;
                transition: transform 0.9s ease-in-out;
                transition-delay: 0.6s;
            }

            .panel h3 {
                font-weight: 600;
                line-height: 1;
                font-size: 1.5rem;
            }

            .panel p {
                font-size: 0.95rem;
                padding: 0.7rem 0;
            }

            .btn.transparent {
                margin: 0;
                background: none;
                border: 2px solid #fff;
                width: 130px;
                height: 41px;
                font-weight: 600;
                font-size: 0.8rem;
            }

            .right-panel .image,
            .right-panel .content {
                transform: translateX(800px);
            }

            /* ANIMATION */
            .container.sign-up-mode:before {
                transform: translate(100%, -50%);
                right: 52%;
            }

            .container.sign-up-mode .left-panel .image,
            .container.sign-up-mode .left-panel .content {
                transform: translateX(-800px);
            }

            .container.sign-up-mode .signin-signup {
                left: 25%;
            }

            .container.sign-up-mode form.sign-up-form {
                opacity: 1;
                z-index: 2;
            }

            .container.sign-up-mode form.sign-in-form {
                opacity: 0;
                z-index: 1;
            }

            .container.sign-up-mode .right-panel .image,
            .container.sign-up-mode .right-panel .content {
                transform: translateX(0%);
            }

            .container.sign-up-mode .left-panel {
                pointer-events: none;
            }

            .container.sign-up-mode .right-panel {
                pointer-events: all;
            }

            @media (max-width: 870px) {
                /* Your existing media query styles */
            }

            @media (max-width: 570px) {
                /* Your existing media query styles */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="forms-container">
                <div class="signin-signup">
                    <form action="#" class="sign-in-form">
                        <h2 class="title">Sign in</h2>
                        <div class="input-field">
                            <i class="fas fa-user"></i>
                            <input type="text" placeholder="Username" />
                        </div>
                        <div class="input-field">
                            <i class="fas fa-lock"></i>
                            <input type="password" placeholder="Password" />
                        </div>
                        <input type="submit" value="Login" class="btn solid" />
                        <p class="social-text">Or Sign in with social platforms</p>
                        <div class="social-media">
                            <a href="#" class="social-icon">
                                <i class="fab fa-facebook-f"></i>
                            </a>
                            <a href="#" class="social-icon">
                                <i class="fab fa-twitter"></i>
                            </a>
                            <a href="#" class="social-icon">
                                <i class="fab fa-google"></i>
                            </a>
                            <a href="#" class="social-icon">
                                <i class="fab fa-linkedin-in"></i>
                            </a>
                        </div>
                    </form>
                    <form action="#" class="sign-up-form">
                        <h2 class="title">Sign up</h2>
                        <div class="input-field">
                            <i class="fas fa-user"></i>
                            <input type="text" placeholder="Username" />
                        </div>
                        <div class="input-field">
                            <i class="fas fa-envelope"></i>
                            <input type="email" placeholder="Email" />
                        </div>
                        <div class="input-field">
                            <i class="fas fa-lock"></i>
                            <input type="password" placeholder="Password" />
                        </div>
                        <input type="submit" class="btn" value="Sign up" />
                        <p class="social-text">Or Sign up with social platforms</p>
                        <div class="social-media">
                            <a href="#" class="social-icon">
                                <i class="fab fa-facebook-f"></i>
                            </a>
                            <a href="#" class="social-icon">
                                <i class="fab fa-twitter"></i>
                            </a>
                            <a href="#" class="social-icon">
                                <i class="fab fa-google"></i>
                            </a>
                            <a href="#" class="social-icon">
                                <i class="fab fa-linkedin-in"></i>
                            </a>
                        </div>
                    </form>
                </div>
            </div>

            <div class="panels-container">
                <div class="panel left-panel">
                    <div class="content">
                        <h3>New here ?</h3>
                        <p>
                            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Debitis,
                            ex ratione. Aliquid!
                        </p>
                        <button class="btn transparent" id="sign-up-btn">
                            Sign up
                        </button>
                    </div>
                    <img src="/api/placeholder/400/320" class="image" alt="" />
                </div>
                <div class="panel right-panel">
                    <div class="content">
                        <h3>One of us ?</h3>
                        <p>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nostrum
                            laboriosam ad deleniti.
                        </p>
                        <button class="btn transparent" id="sign-in-btn">
                            Sign in
                        </button>
                    </div>
                    <img src="/api/placeholder/400/320" class="image" alt="" />
                </div>
            </div>
        </div>

        <script>
            const sign_in_btn = document.querySelector("#sign-in-btn");
            const sign_up_btn = document.querySelector("#sign-up-btn");
            const container = document.querySelector(".container");

            sign_up_btn.addEventListener("click", () => {
                container.classList.add("sign-up-mode");
            });

            sign_in_btn.addEventListener("click", () => {
                container.classList.remove("sign-up-mode");
            });
        </script>
    </body>
    </html>
    """
    
    # Use streamlit components to render the HTML
    components.html(html_content, height=800, scrolling=True)

# Main Streamlit app
def main():
    st.set_page_config(page_title="Sign In & Sign Up Form", layout="wide")
    
    # Remove default margins
    st.markdown("""
        <style>
            .reportview-container .main .block-container{
                padding-top: 0rem;
                padding-right: 0rem;
                padding-left: 0rem;
                padding-bottom: 0rem;
            }
            .reportview-container .main {
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)
    
    login_signup_form()

if __name__ == "__main__":
    main()