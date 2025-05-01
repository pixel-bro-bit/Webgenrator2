import streamlit as st

def generate_personal_website():
    """
    Generates a simple personal website using Streamlit.
    """

    # --- Basic Information ---
    st.title("My Personal Website")
    name = st.text_input("Your Name", "Koshin Nassib")
    tagline = st.text_input("Your Tagline", "Software Engineer | Scientist | muslim ")
    about_me = st.text_area("About Me", "I am a passionate developer with experience in building web applications, analyzing data, and developing AI solutions.  I love learning new things and tackling challenging problems.")
    image_url = st.text_input("Image URL", "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FAli-Nassib&psig=AOvVaw2CL4j0eIIvchzsvpGeZfnW&ust=1745881872194000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLDfh_iq-YwDFQAAAAAdAAAAABAE") # Add a default image URL

    # --- Contact Information ---
    st.header("Contact Information")
    email = st.text_input("Email", "knasib1033@gmail.com")
    linkedin = st.text_input("LinkedIn", "https://www.linkedin.com/in/koshin-nassib-660113232/")
    github = st.text_input("GitHub", "https://github.com/knasib1033")
    twitter = st.text_input("Twitter", "#")

    # --- Projects ---
    st.header("Projects")
    projects = []
    num_projects = st.number_input("Number of Projects", 1, 5, 3)  # Limit to a reasonable number of projects
    for i in range(num_projects):
        st.subheader(f"Project {i+1}")
        project_name = st.text_input(f"Project {i+1} Name", f"Project {i+1}")
        project_description = st.text_area(f"Project {i+1} Description", f"Description of Project {i+1}")
        project_link = st.text_input(f"Project {i+1} Link", "#")  # Default to '#' if no link
        projects.append({
            "name": project_name,
            "description": project_description,
            "link": project_link,
        })

    # --- Skills ---
    st.header("Skills")
    skills = st.text_area("Skills (comma-separated)", "Python, JavaScript, SQL, Machine Learning, Web Development").split(",")
    skills = [skill.strip() for skill in skills]  # Remove leading/trailing spaces

    # --- Education ---
    st.header("Education")
    educations = []
    num_education = st.number_input("Number of Education entries", 1, 3, 1)
    for i in range(num_education):
        st.subheader(f"Education {i + 1}")
        institution_name = st.text_input(f"Institution Name {i + 1}", "University Name")
        degree = st.text_input(f"Degree {i + 1}", "Degree")
        major = st.text_input(f"Major {i + 1}", "Major")
        start_date = st.text_input(f"Start Date {i + 1}", "YYYY-MM")
        end_date = st.text_input(f"End Date {i + 1}", "YYYY-MM")
        educations.append({
            "institution": institution_name,
            "degree": degree,
            "major": major,
            "start_date": start_date,
            "end_date": end_date,
        })

    # --- Generate Website ---
    if st.button("Generate Website"):
        _display_website(name, tagline, about_me, image_url, email, linkedin, github, twitter, projects, skills, educations)

def _display_website(name, tagline, about_me, image_url, email, linkedin, github, twitter, projects, skills, educations):
    """
    Displays the generated personal website. This function is called by generate_personal_website().
    """
    st.markdown(f"""
    # {name}
    ## {tagline}

    ![Profile Image]({image_url})

    ## About Me
    {about_me}

    ## Contact
    - Email: [{email}](mailto:{email})
    - LinkedIn: [{linkedin}]({linkedin})
    - GitHub: [{github}]({github})
    - Twitter: [{twitter}]({twitter})

    ## Projects
    """)
    for project in projects:
        st.markdown(f"""
        ### [{project['name']}]({project['link']})
        {project['description']}
        """)

    st.markdown("## Skills")
    st.markdown(", ".join(skills))

    st.markdown("## Education")
    for education in educations:
        st.markdown(f"""
        ### {education['institution']}
        {education['degree']} in {education['major']}
        {education['start_date']} - {education['end_date']}
        """)
    st.success("Website Generated! You can see the output below.")

if __name__ == "__main__":
    generate_personal_website()
