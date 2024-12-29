import streamlit as st

# CSS can be added in multiple ways:
# 1. Using st.markdown with style tags
st.markdown("""
    <style>
        .custom-header {
            color: #4A90E2;
            font-size: 24px;
            text-align: center;
        }
        
        .custom-box {
            padding: 20px;
            border-radius: 5px;
            background-color: #f0f2f6;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Using st.markdown to inject HTML with custom styles
st.markdown('<div class="custom-header">Welcome to my Streamlit App</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-box">This is a styled container</div>', unsafe_allow_html=True)

# 3. JavaScript integration using components.html
# Create an interactive button with JavaScript
js_code = """
<script>
function handleClick() {
    alert('Button clicked!');
    // You can also interact with Streamlit components using window.Streamlit
    window.Streamlit.setComponentValue('Button was clicked!');
}
</script>

<button onclick="handleClick()" style="
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;">
    Click me!
</button>
"""

# 4. Using components.html for complex HTML/JS integration
import streamlit.components.v1 as components

# Embed the HTML/JavaScript code
components.html(js_code, height=100)

# 5. Creating a custom component with HTML iframe
html_content = """
<iframe src="https://example.com" 
        width="100%" 
        height="450px" 
        style="border: none; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
</iframe>
"""
st.markdown(html_content, unsafe_allow_html=True)

# 6. Adding external CSS and JavaScript files
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" rel="stylesheet"/>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
""", unsafe_allow_html=True)

# 7. Creating an interactive chart with JavaScript
interactive_chart = """
<div id="chart" style="width: 100%; height: 300px;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
<script>
var ctx = document.getElementById('chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderWidth: 1
        }]
    }
});
</script>
"""

components.html(interactive_chart, height=350)