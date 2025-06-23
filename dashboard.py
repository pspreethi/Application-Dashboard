import streamlit as st

# Page setup
st.set_page_config(page_title="Cartesia Application — Sai Preethi Poka", layout="centered")

# Sidebar Navigation
st.sidebar.title("📄 Jump to Section")
page = st.sidebar.radio("Navigate", [
    "👋 A Personal Hello",
    "🌱 Why This Role Matters",
    "🧰 What I Can Offer",
    "🔭 What I’d Love to Work On",
    "🗺️ Logistics",
    "✨ Final Note"
])

# Page 1
if page == "👋 A Personal Hello":
    st.title("Hi Karan 👋")
    st.write("""
Thanks for clicking this. I didn’t want to send a resume or templated email. I wanted to build something that shows how I think and why I’m reaching out.

I’m Preethi. I just finished my Master’s in Information Systems, and I learn best by building and solving open-ended problems.

I saw your post and looked through the open roles. I know I don’t meet the exact experience bar, but I still wanted to share this in case there’s room for someone who’s curious, adaptable, and ready to contribute.
""")


# Page 2
elif page == "🌱 Why This Role Matters":
    st.header("Why This Role Matters to Me")
    st.write("""
I’m at a point in my career where every hour needs to teach me something or move something real forward. That’s why this opportunity in **Business Operations** stood out.

I don’t come from consulting or finance, but I’ve done real work - building forecasting models, prototyping tools, supporting ops teams, automating dashboards in retail. I won't pretend to know everything, but I’m curious, take feedback seriously, and I always show up.

I’m looking for the kind of opportunity where learning happens through contribution, not just preparation. Even if that means starting small on a project or part-time basis. I’m comfortable starting wherever there’s a need and confident I’ll grow into more as I go.
""")

# Page 3
elif page == "🧰 What I Can Offer":
    st.header("What I Can Offer Right Now")
    st.write("""
    Here’s what I know how to do and where I’m strongest:

    - Make sense of messy data and connect it to real business decisions  
    - Design quick, useful MVPs (dashboards, analyses, mini-tools)  
    - Research user, product, and market behavior to uncover insights 
    - Communicate clearly with non-technical stakeholders  
    - Collaborate well. I thrive around smart, intense people  

    I’ve done all of this in different contexts, but what I want now is to do it **alongside people who are building something I care about**.
    """)

# Page 4
elif page == "🔭 What I’d Love to Work On":
    st.header("What I’d Love to Work On at Cartesia")
    st.write("""
    If I got the chance to join you, I’d love to:

    - Build internal tooling to help GTM or ops teams move faster  
    - Design dashboards that bring structure to strategic decisions  
    - Work on activation/onboarding or help build your customer success playbook  
    - Run analysis on early-stage usage, product behavior, or team workflows  

    I’m also open to things I’ve never done before. I don’t need to lead, I need the chance to learn and contribute in a serious way.
    
    """)

# Page 5
elif page == "🗺️ Logistics":
    st.header("Where I’m At Logistically")
    st.write("""
    - Completed MS in Information Systems
    - OPT eligible (12 + 24-month STEM extension, no sponsorship needed currently)  
    - Available immediately  
    - Open to part-time, internship, project-based, or full-time roles
    - **Relocation possible for paid work**, remote preferred if volunteer  
    - My minimum ask: **$35/hr for 20 hrs/week**, with the hope it can grow into more
    """)

# Page 6
elif page == "✨ Final Note":
    st.header("✨ Final Note")
    st.write("""
    I’m not sending this out to a dozen companies. I made this because **I actually want to work with you** and because I think there’s room for someone like me on your team, even if it’s not a standard path.

    Thanks for taking the time to read this. Even if it doesn’t lead to something right now, I’m rooting for what you’re building.

    — Sai Preethi Poka  
    [pokasaipreethi@gmail.com](mailto:pokasaipreethi@gmail.com)
    [LinkedIn](https://www.linkedin.com/in/saipreethipoka/)
    [Resume](https://drive.google.com/file/d/1yg98VCv6LQKajRHnj2xn-xqynsDn1DSJ/view?usp=sharing)
    [Portfolio](https://pspreethi.github.io/portfolio/)
    """)
