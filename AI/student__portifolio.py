import streamlit as st
import os

# Set page config
st.set_page_config(page_title="My Digital Footprint", page_icon="🚀", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Testimonials", "Timeline","Contact","Settings"])

# Home Page
if page == "Home":
    st.title("🚀 My Digital Footprint – Showcasing My Journey")

    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150, caption="Profile Picture")
    else:
        st.image("queen.jpg", width=150, caption="Profile Picture")

    # Dynamic Profile Editing
    name = st.text_input("Your Name", "UWABATONI Laurene")
    location = st.text_input("Location", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study", "Software Engineering, Year 3")
    university = st.text_input("University", "INES Ruhengeri")

    st.write(f"📍 {location}")
    st.write(f"📚 {field_of_study}")
    st.write(f"🎓 {university}")

    # Resume Download
    try:
        with open("My Resume.pdf", "rb") as file:
            resume_bytes = file.read()
        st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume1.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.warning("⚠ Resume file not found. Please upload your resume.")

    # About Me section
    st.subheader("About Me")
    about_me = st.text_area("Write a short description about yourself", "I am Laurene, an enthusiastic software engineering student set to graduate this year, driven by technology's potential to solve real-world challenges and enhance efficiency. Currently, I am working on my final dissertation and developing a personal portfolio using Python Streamlit.")
    st.write(about_me)

# Projects Page with Filtering System
elif page == "Projects":
    st.title("💻 My Projects")

    project_filter = st.selectbox("Filter by Category", ["All", "Year 1", "Year 2", "Year 3", "Dissertation"])

    projects = {
        "Year 1": "Library Management System - Python & SQLite",
        "Year 2": "Hotel Management System - Java & MySQL",
        "Year 3": "Car Rental System - Python & SQLite",
        "Dissertation": "AI-Powered School-Parent Smart Communication System with Machine Learning - Python & MySQL"
    }

    for year, description in projects.items():
        if project_filter == "All" or project_filter == year:
            with st.expander(f"📌 {year} - {description}"):
                st.write(f"*Project Type:* Individual")
                st.write(f"*Description:* A system designed for {description}.")
                st.write("🔗 [GitHub Repo](#)")

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")
    
    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)
    
    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)
    
    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)

    skill_MachineLearning = st.slider("Machine Learning", 0, 100, 75)
    st.progress(skill_MachineLearning)

    skill_React = st.slider("React Js", 0, 100, 75)
    st.progress(skill_React)

    st.subheader("🏆 Certifications & Achievements")
    st.write("✔ AI in Research & Education")
    st.write("✔ Certified by NOVA SERVICES (Web application development, social media management, webpages creation, website administration and security).")
    st.write("✔ Certificate in TME EDUCATION AMBASSADOR IN RWANDA (Arduino, Python, and introduction to Robotics).")

# Testimonials Page
elif page == "Testimonials":
    st.title("🗣 Testimonials")
    st.write("🌟 A Motivator🤝, Hardworking😘, Teamwork and motivator Friend💖 Such an Innovative Software Engineer! – UKNuswayiba")

    # Display existing testimonials
    st.subheader("💬 Share Your Testimonial")
    
    # User input for new testimonials
    new_testimonial = st.text_area("Write your testimonial here...")
    user_name = st.text_input("Your Name")

    if st.button("Submit"):
        if new_testimonial and user_name:
            st.success("Thank you for your testimonial!")
            st.write(f"🌟 {new_testimonial} – {user_name}")
        else:
            st.warning("Please enter both your testimonial and your name.")

# Timeline Page
elif page == "Timeline":
    st.title("⏳ My Academic & Project Milestones")

    timeline_data = [
        ("Year 1", "📚 First major project completed: Library Management System"),
        ("Year 2", "💻 Deep researches on different programming languages"),
        ("Year 3", "📖 Final Year Dissertation: AI-Powered School-Parent Communication System"),
    ]

    for year, event in timeline_data:
        st.write(f"**{year}:** {event}")

# Contact Page with Validation
elif page == "Contact":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and message:
                st.success("✅ Message sent successfully!")
            else:
                st.warning("⚠ Please fill in all fields before submitting.")

    st.write("📧 Email: uwalaurene250@gmail.com")
    st.write("[🔗 LinkedIn](https://linkedin.com/in/uwabatoni-laurene-2b5a06333)")
    st.write("[📂 GitHub](https://github.com/lolololo001/My-Digital-Footprint.git)")
# Settings Page
elif page == "Settings":
    st.title("⚙️ Settings")
    # Profile Picture Upload
    st.write("🖼 Change Profile Picture")
    new_profile_picture = st.file_uploader("Upload a new profile picture", type=["jpg", "png"])
    
    if new_profile_picture:
        st.image(new_profile_picture, width=150, caption="New Profile Picture")
        st.success("✅ Profile picture updated successfully!")
     
    st.subheader("Edit Profile Details")
    name = st.text_input("Your Name", "UWABATONI Laurene")
    location = st.text_input("Location", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study", "Software Engineering, Year 3")
    university = st.text_input("University", "INES Ruhengeri")
    about_me = st.text_area("About Me", "I am Laurene, an enthusiastic software engineering student...")
    
    if st.button("Save Changes"):
        st.success("✅ Profile updated successfully!")
    