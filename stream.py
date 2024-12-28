import streamlit as st

# Custom CSS to set Streamlit background to grey
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f0f0;  /* Light grey background */
    }
    </style>
""", unsafe_allow_html=True)

# HTML and CSS for the login page
login_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');
    *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Poppins', sans-serif;
    }
    body{
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: transparent; /* Keep background transparent to show Streamlit grey */
    }
    .login-box{
        display: flex;
        justify-content: center;
        flex-direction: column;
        width: 440px;
        height: auto;
        padding: 30px;
        background: #f0f8ff; /* Light blue box */
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .login-header{
        text-align: center;
        margin: 20px 0 40px 0;
    }
    .login-header header{
        color: #2c3e50; /* Darker blue for contrast */
        font-size: 30px;
        font-weight: 600;
    }
    .input-box .input-field{
        width: 100%;
        height: 60px;
        font-size: 17px;
        padding: 0 25px;
        margin-bottom: 15px;
        border-radius: 30px;
        border: 1px solid #b0d4f1;
        background: #e6f2ff; /* Lighter input background */
        box-shadow: 0px 5px 10px 1px rgba(0,0,0, 0.05);
        outline: none;
        transition: .3s;
    }
    ::placeholder{
        font-weight: 500;
        color: #555;
    }
    .input-field:focus{
        width: 105%;
        border-color: #66b3ff;
    }
    .forgot{
        display: flex;
        justify-content: space-between;
        margin-bottom: 40px;
    }
    section{
        display: flex;
        align-items: center;
        font-size: 14px;
        color: #555;
    }
    #check{
        margin-right: 10px;
    }
    a{
        text-decoration: none;
    }
    a:hover{
        text-decoration: underline;
    }
    section a{
        color: #2c3e50;
    }
    .input-submit{
        position: relative;
    }
    .submit-btn{
        width: 100%;
        height: 60px;
        background: #66b3ff; /* Button in soft blue */
        border: none;
        border-radius: 30px;
        cursor: pointer;
        transition: .3s;
    }
    .input-submit label{
        position: absolute;
        top: 45%;
        left: 50%;
        color: #fff;
        -webkit-transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
        cursor: pointer;
    }
    .submit-btn:hover{
        background: #4da3e6;
        transform: scale(1.05,1);
    }
    .sign-up-link{
        text-align: center;
        font-size: 15px;
        margin-top: 20px;
    }
    .sign-up-link a{
        color: #2c3e50;
        font-weight: 600;
    }
    </style>
    <title>Login | Ludiflex</title>
</head>
<body>
    <div class="login-box">
        <div class="login-header">
            <header>Login</header>
        </div>
        <div class="input-box">
            <input type="text" class="input-field" placeholder="Email" autocomplete="off" required>
        </div>
        <div class="input-box">
            <input type="password" class="input-field" placeholder="Password" autocomplete="off" required>
        </div>
        <div class="forgot">
            <section>
                <input type="checkbox" id="check">
                <label for="check">Remember me</label>
            </section>
            <section>
                <a href="#">Forgot password</a>
            </section>
        </div>
        <div class="input-submit">
            <button class="submit-btn" id="submit"></button>
            <label for="submit">Sign In</label>
        </div>
        <div class="sign-up-link">
            <p>Don't have an account? <a href="#">Sign Up</a></p>
        </div>
    </div>
</body>
</html>
"""

# Display HTML content in Streamlit app
st.markdown(login_html, unsafe_allow_html=True)
