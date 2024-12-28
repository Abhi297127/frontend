import streamlit as st

# CSS Styling
st.markdown("""
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
        }
        .wrapper {
            width: 100%;
            height: 100vh;
            background-color: #f7f7f7;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            background-color: #333;
            padding: 15px 30px;
        }
        .nav-logo p {
            color: white;
            font-size: 20px;
            font-weight: bold;
        }
        .nav-menu {
            display: flex;
            list-style: none;
        }
        .nav-menu ul {
            display: flex;
            gap: 20px;
        }
        .nav-menu ul li a {
            color: white;
            text-decoration: none;
            font-size: 16px;
        }
        .btn {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
        }
        .btn.white-btn {
            background-color: white;
            color: #007bff;
        }
        .form-box {
            width: 400px;
            margin-top: 20px;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        .input-box {
            margin-bottom: 15px;
            position: relative;
        }
        .input-field {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .submit {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
        }
        .top {
            text-align: center;
            margin-bottom: 20px;
        }
        .top span {
            font-size: 14px;
            color: #777;
        }
        .top span a {
            color: #007bff;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# HTML Structure
st.markdown("""
    <div class="wrapper">
        <nav class="nav">
            <div class="nav-logo">
                <p>LOGO .</p>
            </div>
            <div class="nav-menu" id="navMenu">
                <ul>
                    <li><a href="#" class="link active">Home</a></li>
                    <li><a href="#" class="link">Blog</a></li>
                    <li><a href="#" class="link">Services</a></li>
                    <li><a href="#" class="link">About</a></li>
                </ul>
            </div>
            <div class="nav-button">
                <button class="btn white-btn" id="loginBtn" onclick="login()">Sign In</button>
                <button class="btn" id="registerBtn" onclick="register()">Sign Up</button>
            </div>
        </nav>

        <div class="form-box">
            <div class="login-container" id="login">
                <div class="top">
                    <span>Don't have an account? <a href="#" onclick="register()">Sign Up</a></span>
                    <header>Login</header>
                </div>
                <div class="input-box">
                    <input type="text" class="input-field" placeholder="Username or Email">
                </div>
                <div class="input-box">
                    <input type="password" class="input-field" placeholder="Password">
                </div>
                <div class="input-box">
                    <input type="submit" class="submit" value="Sign In">
                </div>
            </div>
            <div class="register-container" id="register" style="display: none;">
                <div class="top">
                    <span>Have an account? <a href="#" onclick="login()">Login</a></span>
                    <header>Sign Up</header>
                </div>
                <div class="input-box">
                    <input type="text" class="input-field" placeholder="Email">
                </div>
                <div class="input-box">
                    <input type="password" class="input-field" placeholder="Password">
                </div>
                <div class="input-box">
                    <input type="submit" class="submit" value="Register">
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# JavaScript for functionality
st.markdown("""
    <script>
        function login() {
            document.getElementById('login').style.display = 'block';
            document.getElementById('register').style.display = 'none';
        }

        function register() {
            document.getElementById('login').style.display = 'none';
            document.getElementById('register').style.display = 'block';
        }
    </script>
""", unsafe_allow_html=True)
