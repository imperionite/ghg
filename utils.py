import streamlit as st

def add_footer():
    footer_style = """
        <style>
        .footer-text {
            font-size: 0.9rem;
            color: #6c757d;  /* muted gray */
            text-align: left;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }
        .footer-text a {
            color: #6c757d;
            text-decoration: none;
        }
        .footer-text a:hover {
            text-decoration: underline;
            color: #0056b3;
        }
        </style>
    """
    footer_html = """
    <div class="footer-text">
        © 2025
        <a href="https://github.com/imperionite/ilmanala" target="_blank" rel="noopener noreferrer"> GHG Data Explorer PH </a>
        by
        <a href="https://github.com/imperionite" target="_blank" rel="noopener noreferrer"> Arnel Imperial</a>.
        Built with ❤️ using
        <a href="https://www.r-project.org/about.html" target="_blank" rel="noopener noreferrer">R</a>,
        <a href="https://docs.python.org/3/faq/general.html#what-is-python" target="_blank" rel="noopener noreferrer">Python</a>,
        <a href="https://docs.astro.build/en/concepts/why-astro/" target="_blank" rel="noopener noreferrer">AstroJS</a>,
        <a href="https://firebase.google.com/" target="_blank" rel="noopener noreferrer">Firebase</a> and
        <a href="https://streamlit.io/" target="_blank" rel="noopener noreferrer">Streamlit</a>
    </div>
"""

    st.markdown(footer_style + footer_html, unsafe_allow_html=True)