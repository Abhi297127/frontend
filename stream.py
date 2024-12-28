import streamlit as st

# CSS styling
st.markdown(
    """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .full-page {
            height: 100%;
            width: 100%;
            background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url(images/bg-2.jpg);
            background-position: center;
            background-size: cover;
            position: absolute;
        }
        .navbar {
            display: flex;
            align-items: center;
            padding: 20px 30px 0 50px;
        }
        nav {
            flex: 1;
            text-align: right;
        }
        nav ul {
            display: inline-block;
            list-style: none;
        }
        nav ul li {
            display: inline-block;
            margin-right: 70px;
        }
        nav ul li a,
        nav ul li button {
            text-decoration: none;
            font-size: 20px;
            color: white;
            font-family: sans-serif;
            background: transparent;
            border: none;
            outline: none;
            cursor: pointer;
        }
        nav ul li button:hover,
        nav ul li a:hover {
            color: aqua;
        }
        a {
            text-decoration: none;
            color: palevioletred;
            font-size: 28px;
        }
        #login-form {
            display: none;
        }
        .form-box {
            width: 380px;
            height: 480px;
            position: relative;
            margin: 2% auto;
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            overflow: hidden;
        }
        .button-box {
            width: 220px;
            margin: 35px auto;
            position: relative;
            box-shadow: 0 0 20px 9px #ff61241f;
            border-radius: 30px;
        }
        .toggle-btn {
            padding: 10px 30px;
            cursor: pointer;
            background: transparent;
            border: 0;
            outline: none;
            position: relative;
        }
        #btn {
            top: 0;
            left: 0;
            position: absolute;
            width: 110px;
            height: 100%;
            background: #F3C693;
            border-radius: 30px;
            transition: 0.5s;
        }
        .input-group-login,
        .input-group-register {
            top: 150px;
            position: absolute;
            width: 280px;
            transition: 0.5s;
        }
        .input-group-register {
            top: 120px;
        }
        .input-field {
            width: 100%;
            padding: 10px 0;
            margin: 5px 0;
            border: none;
            border-bottom: 1px solid #999;
            outline: none;
            background: transparent;
            color: white;
            font-size: 15px;
        }
        .submit-btn {
            width: 85%;
            padding: 10px 30px;
            cursor: pointer;
            display: block;
            margin: auto;
            background: #F3C693;
            border: 0;
            outline: none;
            border-radius: 30px;
        }
        .check-box {
            margin: 30px 10px 34px 0;
        }
        span {
            color: #777;
            font-size: 12px;
            position: absolute;
            bottom: 68px;
        }
        #login {
            left: 50px;
        }
        #register {
            left: 450px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML form
st.markdown(
    """
    <div class="full-page">
        <div class="navbar">
            <div>
                <a href="website.html">Seek Coding</a>
            </div>
            <nav>
                <ul id="MenuItems">
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Services</a></li>
                    <li><a href="#">Contact</a></li>
                    <li>
                        <button class="loginbtn" onclick="document.getElementById('login-form').style.display='block'" style="width:auto;">Login</button>
                    </li>
                </ul>
            </nav>
        </div>
        <div id="login-form" class="login-page">
            <div class="form-box">
                <div class="button-box">
                    <div id="btn"></div>
                    <button type="button" onclick="login()" class="toggle-btn">Log In</button>
                    <button type="button" onclick="register()" class="toggle-btn">Register</button>
                </div>
                <form id="login" class="input-group-login">
                    <input type="text" class="input-field" placeholder="Email Id" required>
                    <input type="password" class="input-field" placeholder="Enter Password" required>
                    <input type="checkbox" class="check-box"><span>Remember Password</span>
                    <button type="submit" class="submit-btn">Log in</button>
                </form>
                <form id="register" class="input-group-register">
                    <input type="text" class="input-field" placeholder="First Name" required>
                    <input type="text" class="input-field" placeholder="Last Name" required>
                    <input type="email" class="input-field" placeholder="Email Id" required>
                    <input type="password" class="input-field" placeholder="Enter Password" required>
                    <input type="password" class="input-field" placeholder="Confirm Password" required>
                    <input type="checkbox" class="check-box"><span>I agree to the terms and conditions</span>
                    <button type="submit" class="submit-btn">Register</button>
                </form>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# JavaScript
st.markdown(
    """
    <script>
        var x = document.getElementById('login');
        var y = document.getElementById('register');
        var z = document.getElementById('btn');
        function register() {
            x.style.left = '-400px';
            y.style.left = '50px';
            z.style.left = '110px';
        }
        function login() {
            x.style.left = '50px';
            y.style.left = '450px';
            z.style.left = '0px';
        }
        var modal = document.getElementById('login-form');
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    </script>
    """,
    unsafe_allow_html=True,
)
