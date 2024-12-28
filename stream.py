import streamlit as st

# CSS Styling
st.markdown("""
    <style>
        /* Import Poppins Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

/* Global Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

/* Body Styling */
body {
    background: url("images/1.jpg") no-repeat center center fixed;
    background-size: cover;
    overflow: hidden;
}

/* Wrapper */
.wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 110vh;
    background: rgba(39, 39, 39, 0.4);
}

/* Navigation Bar */
.nav {
    position: fixed;
    top: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    height: 100px;
    line-height: 100px;
    background: linear-gradient(rgba(39,39,39,0.6), transparent);
    z-index: 100;
}

.nav-logo p {
    color: white;
    font-size: 25px;
    font-weight: 600;
}

.nav-menu ul {
    display: flex;
}

.nav-menu ul li {
    list-style: none;
}

.nav-menu ul li .link {
    text-decoration: none;
    font-weight: 500;
    color: #fff;
    padding-bottom: 15px;
    margin: 0 25px;
    transition: border-bottom 0.3s ease;
}

.link:hover, .active {
    border-bottom: 2px solid #fff;
}

/* Buttons */
.nav-button .btn {
    width: 130px;
    height: 40px;
    font-weight: 500;
    background: rgba(255, 255, 255, 0.4);
    border: none;
    border-radius: 30px;
    cursor: pointer;
    transition: background 0.3s ease;
}

.btn:hover {
    background: rgba(255, 255, 255, 0.3);
}

#registerBtn {
    margin-left: 15px;
}

.btn.white-btn {
    background: rgba(255, 255, 255, 0.7);
}

.btn.white-btn:hover {
    background: rgba(255, 255, 255, 0.5);
}

/* Hamburger Menu Button */
.nav-menu-btn {
    display: none;
}

/* Form Box */
.form-box {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 512px;
    height: 420px;
    overflow: hidden;
    z-index: 2;
}

/* Login & Registration Containers */
.login-container,
.register-container {
    position: absolute;
    width: 500px;
    display: flex;
    flex-direction: column;
    transition: 0.5s ease-in-out;
}

.login-container {
    left: 4px;
}

.register-container {
    right: -520px;
}

/* Form Headers */
.top span {
    color: #fff;
    font-size: small;
    padding: 10px 0;
    display: flex;
    justify-content: center;
}

.top span a {
    font-weight: 500;
    color: #fff;
    margin-left: 5px;
    text-decoration: none;
}

header {
    color: #fff;
    font-size: 30px;
    text-align: center;
    padding: 10px 0 30px;
}

/* Input Fields */
.input-field {
    font-size: 15px;
    background: rgba(255, 255, 255, 0.2);
    color: #fff;
    height: 50px;
    width: 100%;
    padding: 0 10px 0 45px;
    border: none;
    border-radius: 30px;
    outline: none;
    transition: background 0.2s ease;
}

.input-field:hover,
.input-field:focus {
    background: rgba(255, 255, 255, 0.25);
}

::placeholder {
    color: #fff;
}

.input-box i {
    position: relative;
    top: -35px;
    left: 17px;
    color: #fff;
}

/* Submit Button */
.submit {
    font-size: 15px;
    font-weight: 500;
    color: black;
    height: 45px;
    width: 100%;
    border: none;
    border-radius: 30px;
    outline: none;
    background: rgba(255, 255, 255, 0.7);
    cursor: pointer;
    transition: background 0.3s ease, box-shadow 0.3s ease;
}

.submit:hover {
    background: rgba(255, 255, 255, 0.5);
    box-shadow: 1px 5px 7px 1px rgba(0, 0, 0, 0.2);
}

/* Two-Column Layout */
.two-col {
    display: flex;
    justify-content: space-between;
    color: #fff;
    font-size: small;
    margin-top: 10px;
}

.two-col .one {
    display: flex;
    gap: 5px;
}

.two label a {
    text-decoration: none;
    color: #fff;
}

.two label a:hover {
    text-decoration: underline;
}

/* Responsive Design */
@media only screen and (max-width: 786px) {
    .nav-button {
        display: none;
    }

    .nav-menu.responsive {
        top: 100px;
    }

    .nav-menu {
        position: absolute;
        top: -800px;
        display: flex;
        justify-content: center;
        background: rgba(255, 255, 255, 0.2);
        width: 100%;
        height: 90vh;
        backdrop-filter: blur(20px);
        transition: 0.3s;
    }

    .nav-menu ul {
        flex-direction: column;
        text-align: center;
    }

    .nav-menu-btn {
        display: block;
    }

    .nav-menu-btn i {
        font-size: 25px;
        color: #fff;
        padding: 10px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        cursor: pointer;
        transition: background 0.3s ease;
    }

    .nav-menu-btn i:hover {
        background: rgba(255, 255, 255, 0.15);
    }
}

@media only screen and (max-width: 540px) {
    .wrapper {
        min-height: 100vh;
    }

    .form-box {
        width: 100%;
        height: 500px;
    }

    .register-container,
    .login-container {
        width: 100%;
        padding: 0 20px;
    }

    .register-container .two-forms {
        flex-direction: column;
        gap: 0;
    }
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
