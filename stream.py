import streamlit as st

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
        background: #cce7ff; /* Soft sky blue background */
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
    }
    .toggle-buttons{
        display: flex;
        justify-content: space-around;
        margin-bottom: 30px;
    }
    .toggle-btn{
        padding: 10px 30px;
        cursor: pointer;
        border: none;
        border-radius: 30px;
        background: #66b3ff;
        color: white;
        font-size: 16px;
    }
    .toggle-btn.active{
        background: #4da3e6;
    }
    .hidden{
        display: none;
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
    </style>
    <title>Login | Ludiflex</title>
</head>
<body>
    <div class="login-box">
        <div class="toggle-buttons">
            <button class="toggle-btn active" onclick="showLogin()">Sign In</button>
            <button class="toggle-btn" onclick="showSignUp()">Sign Up</button>
        </div>
        
        <div id="signin" class="">
            <div class="login-header">
                <header>Sign In</header>
            </div>
            <div class="input-box">
                <input type="text" class="input-field" placeholder="Username" required>
            </div>
            <div class="input-box">
                <input type="password" class="input-field" placeholder="Password" required>
            </div>
            <div class="input-submit">
                <button class="submit-btn">Sign In</button>
            </div>
        </div>
        
        <div id="signup" class="hidden">
            <div class="login-header">
                <header>Sign Up</header>
            </div>
            <div class="input-box">
                <input type="text" class="input-field" placeholder="Full Name" required>
            </div>
            <div class="input-box">
                <input type="text" class="input-field" placeholder="Username" required>
            </div>
            <div class="input-box">
                <input type="text" class="input-field" placeholder="GitHub Link" required>
            </div>
            <div class="input-box">
                <input type="text" class="input-field" placeholder="GitHub Token" required>
            </div>
            <div class="input-box">
                <input type="password" class="input-field" placeholder="Password" required>
            </div>
            <div class="input-submit">
                <button class="submit-btn">Sign Up</button>
            </div>
        </div>
    </div>

    <script>
        function showSignUp() {
            document.getElementById('signin').classList.add('hidden');
            document.getElementById('signup').classList.remove('hidden');
        }

        function showLogin() {
            document.getElementById('signup').classList.add('hidden');
            document.getElementById('signin').classList.remove('hidden');
        }
    </script>
</body>
</html>
"""

# Display HTML content in Streamlit app
st.markdown(login_html, unsafe_allow_html=True)
