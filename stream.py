import streamlit as st

# CSS Styling and HTML Structure
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
            background: url("images/1.jpg") no-repeat center center fixed;
            background-size: cover;
        }

        .wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: rgba(39, 39, 39, 0.4);
        }

        .nav {
            position: fixed;
            top: 0;
            width: 100%;
            height: 60px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
            background: rgba(39, 39, 39, 0.8);
            z-index: 100;
        }

        .nav-logo p {
            color: white;
            font-size: 20px;
            font-weight: 600;
        }

        .nav-menu ul {
            display: flex;
            list-style: none;
            margin: 0;
            padding: 0;
        }

        .nav-menu ul li a {
            text-decoration: none;
            color: white;
            margin: 0 10px;
            padding-bottom: 5px;
        }

        .nav-menu ul li a:hover {
            border-bottom: 2px solid white;
        }

        .form-box {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .form-box input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .form-box button {
            width: 100%;
            padding: 10px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .form-box button:hover {
            background: #0056b3;
        }
    </style>

    <div class="wrapper">
        <div class="form-box">
            <h2>Login</h2>
            <input type="text" placeholder="Username">
            <input type="password" placeholder="Password">
            <button>Login</button>
        </div>
    </div>
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
        function myMenuFunction() {
    var i = document.getElementById("navMenu");
    if(i.className === "nav-menu") {
        i.className += " responsive";
    } else {
        i.className = "nav-menu";
    }
   }
     var a = document.getElementById("loginBtn");
    var b = document.getElementById("registerBtn");
    var x = document.getElementById("login");
    var y = document.getElementById("register");
    function login() {
        x.style.left = "4px";
        y.style.right = "-520px";
        a.className += " white-btn";
        b.className = "btn";
        x.style.opacity = 1;
        y.style.opacity = 0;
    }
    function register() {
        x.style.left = "-510px";
        y.style.right = "5px";
        a.className = "btn";
        b.className += " white-btn";
        x.style.opacity = 0;
        y.style.opacity = 1;
    }
    </script>
""", unsafe_allow_html=True)
