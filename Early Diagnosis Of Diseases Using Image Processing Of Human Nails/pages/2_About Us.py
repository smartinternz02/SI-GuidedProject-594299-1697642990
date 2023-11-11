import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="About Us",
    page_icon="people"
)

# Custom CSS to change the background color of the title
st.markdown(
    """
    <style>
        .title-wrapper {
            background-color: red;
        }
        img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(":red[About Us]:male-technologist:")

st.markdown("<br><br>", unsafe_allow_html=True)

# Define the layout for each team member
def team_member_layout(image_path, name, roll_number, description, linkedin_link, github_link):
    # Image column
    st.image(image_path)
    # Text column
    st.header(f":blue[**{name} ({roll_number})**] ")
    st.write(description)

    # Social media links

    st.subheader(f":red[Connect] with {name}:")
    col1, col2 = st.columns(2)
    col1.subheader(f":link:[LinkedIn]({linkedin_link})")
    col2.subheader(f":computer:[GitHub]({github_link})")

# Siddhanth Garg
team_member_layout(
    image_path="images/siddhanth.jpg",
    name="Siddhanth Garg",
    roll_number="21BCE2174",
    description="I'm a dedicated and motivated learner with a burning curiosity for all things data-driven. "
                "Currently pursuing my studies in Computer Science, I'm on a mission to unravel the mysteries hidden within vast data sets, "
                "harnessing their power to drive innovation and solve real-world problems. Through hands-on projects and rigorous coursework, "
                "I have gained a solid foundation in various ML algorithms, predictive modeling, and data visualization techniques. "
                "My experience spans from developing supervised learning models to exploring the exciting realm of deep learning and neural networks.",
    linkedin_link="https://www.linkedin.com/in/siddhanth-garg-7b13b0232/",
    github_link="https://github.com/siddhanth19"

)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# Manas Pandit
team_member_layout(
    image_path="images/manas.png",
    name="Manas Pandit",
    roll_number="21BIT0234",
    description="Currently in third-year pursuing B.Tech in IT at Vellore Institute of Technology, Vellore, "
                "I am driven by my passion for data analysis and problem-solving. I am actively seeking opportunities to apply my analytical skills "
                "in a professional setting, aiming to contribute meaningfully as a Data Analyst. "
                "Feel free to connect with me on LinkedIn and GitHub.",
    linkedin_link="https://www.linkedin.com/in/manas-pandit-b6669422a/",
    github_link="https://github.com/Devmanas23"
)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# Pratyush Kaushal
team_member_layout(
    image_path="images/pratyush.png",
    name="Pratyush Kaushal",
    roll_number="21BCE2198",
    description="A third-year Computer Science Engineering (CSE) student at VIT Vellore, actively engaged in exploring the realms of machine learning and cybersecurity. "
                "Passionate about leveraging technology to address complex challenges, this individual combines theoretical knowledge with practical skills to contribute meaningfully to "
                "the ever-evolving fields of AI and cybersecurity. "
                "You can reach out to me on LinkedIn or check my projects on GitHub.",
    linkedin_link="https://www.linkedin.com/in/pratyush-kaushal-4724a224b/",
    github_link="https://github.com/PratyushKaushal08"
)

# Add some spacing for the closing statement
st.markdown("<br><br>", unsafe_allow_html=True)

# Closing statement
st.write("We hope you liked our effort for this model and show us some love ❤️.")
