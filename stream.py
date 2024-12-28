import streamlit as st
import streamlit.components.v1 as components

# Custom HTML and JavaScript for Login and Register
html_code = """
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
<script>
function login() {
    document.getElementById("login").style.display = "block";
    document.getElementById("register").style.display = "none";
}
function register() {
    document.getElementById("login").style.display = "none";
    document.getElementById("register").style.display = "block";
}
</script>
<style>
    .form-box { max-width: 400px; margin: auto; font-family: Arial, sans-serif; }
    .input-box { margin: 15px 0; }
    .input-field { width: 100%; padding: 10px; margin: 5px 0; }
    .submit { background: #4CAF50; color: white; border: none; padding: 10px; cursor: pointer; width: 100%; }
    .submit:hover { background: #45a049; }
</style>
"""

# Render the HTML
components.html(html_code, height=600)
