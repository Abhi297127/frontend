import streamlit as st

# CSS styling
st.markdown(
    """
    <style>
        .login-container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            background-color: #f4f4f9;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .login-header {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .login-input {
            margin-bottom: 15px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 5px;
            width: 100%;
        }
        .login-button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px;
            width: 100%;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .login-button:hover {
            background-color: #45a049;
        }
        .login-role {
            margin-bottom: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML form
st.markdown(
    """
    <div class="login-container">
        <div class="login-header">Login</div>
        <form action="" method="post">
            <input class="login-input" type="text" placeholder="Username" id="username" />
            <input class="login-input" type="password" placeholder="Password" id="password" />
            <select class="login-input login-role" id="role">
                <option value="user">User</option>
                <option value="admin">Admin</option>
            </select>
            <button type="button" class="login-button" onclick="handleLogin()">Login</button>
        </form>
    </div>
    """,
    unsafe_allow_html=True,
)

# JavaScript (via st.markdown for now)
st.markdown(
    """
    <script>
        function handleLogin() {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const role = document.getElementById('role').value;
            if (username === '' || password === '') {
                alert('Please fill in all fields');
            } else {
                alert('Logged in as ' + role + ': ' + username);
                // Streamlit doesn't handle JS responses. This is just for display.
            }
        }
    </script>
    """,
    unsafe_allow_html=True,
)

# Backend logic
st.write("Backend handling can be implemented in Python to process login credentials.")
