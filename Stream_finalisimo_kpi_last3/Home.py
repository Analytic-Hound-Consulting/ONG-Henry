import streamlit as st
import pandas as pd
from PIL import Image


st.markdown ('...**_Analytic Hound data load complete_**')


#COSTADO


st.sidebar.caption("GITHUB REPOSITORY | [LINK](https://github.com/Analytic-Hound-Consulting)")
st.sidebar.caption("MAILING | analytichound@gmail.com")


st.sidebar.header(":violet[ **Developed by Analytic Hound Group®**]")

#LOGO
image = Image.open('./Stream_finalisimo_kpi_last3/images/bannerIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.markdown("-----------")


#1st paragraph
st.header(":violet[ A MIGRATION PROJECT ]")
st.markdown("""Throughout history, migratory flows have undergone multiple changes. These changes are the translation of the different sociopolitical, demographic, environmental and economic aspects among others. "
_**The Analytic Hound ®**_ consulting team, with the contribution of data provided by **Data hub, World bank group and United nations**, has developed an interactive platform for the dynamic analysis of human movement around the world starting from the year 2000.""")
st.markdown ("""On the left side of your screen, you will find a side toolbar which allows you to navigate through this website.""")
    


st.markdown("---")

#2nd paragraph

st.header(":violet[ABOUT US:]")
st.markdown("""_**Analytic Hound ®**_ is a highly specialized consulting firm based in Buenos Aires, Argentina. 
Our mission is to improve the society in which we live through consultancy and, to achieve this, we study, design, execute and evaluate projects and actions that can improve society as we know it. 
""")
st.markdown("We are a multidisciplinary team with different backgrounds and talents, but above all, made up of people of good values. This translates into a synergy that, in addition to being a highly effective work team, makes project development a nutritious, joyful, and stress-free experience.")
st.markdown("---")


#3rd paragraph


st.header(":violet[DATA SOURCES:]")

image = Image.open('./Stream_finalisimo_kpi_last3/images/fuentesIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


col1, col2, col3= st.columns(3)

with col1:      
    with st.expander("UNITED NATIONS"):
        st.markdown("[LINK](https://www.un.org/development/desa/pd/data-landing-page)")
       

        
with col2: 
    with st.expander("DATAHUB"):
        st.markdown("[LINK](https://datahub.io/)")
        
with col3: 
    with st.expander("WORLD BANK GLOBAL"):
        st.markdown("[LINK](https://data.worldbank.org/)")
       
       


st.markdown("---")

#4th paragraph:

st.header(":violet[DISCLAIMER:]")

st.markdown("""**_Analytic Hound_ ®** Analytic Hound ® is a consulting firm based in Buenos Aires (Argentina) without any sociopolitical or economic conflicts of interest related to its different objects of study. The following documentation has been published in good faith for educational purposes only. We make no guarantees about the completeness, reliability and accuracy of this information. Likewise, it is expressly stated that any action that could be taken based on the information provided herein is strictly the responsibility of the reader and Analytic Hound ® 
                    is not responsible for any action by third parties related to the use, interpretation or disclosure thereof.""")

st.write("_**The Analytic Hound team ®**_")

st.markdown("---")



#TEAM

st.header( " :violet[MEMBERS OF THE HOUNDS PACK:]"  )



image1 = Image.open('./Stream_finalisimo_kpi_last3/images/team.png')
st.image(image1, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.markdown("---")


col1, col2, col3, col4, col5 = st.columns(5)

    
        
with col1:          
    if st.button('ALAN MYSLER'):
       st.write("[DATA SCIENTIST](https://www.linkedin.com/in/amysler/)")
    else:
        st.write("[DATA SCIENTIST](https://www.linkedin.com/in/amysler/)")
  
        
with col2:
    if st.button("BELEN ZAPATA"):
       st.write("[DATA ANALYST](https://www.linkedin.com/in/bel%C3%A9n-zapata/)")
    else:
        st.write("[DATA ANALYST](https://www.linkedin.com/in/bel%C3%A9n-zapata/)")        
   
   
with col3:      
    if st.button("LUCAS RODRIGUEZ "):
       st.write("[DATA ENGINEER ](https://www.linkedin.com/in/lucasrdrz/)")
    else:
        st.write("[DATA ENGINEER ](https://www.linkedin.com/in/lucasrdrz/)")    
   


with col4:       
    if st.button("EUGENIA BALL"):
       st.write("[DATA ENGINEER](https://www.linkedin.com/in/eugenia-ball/)")
    else:
        st.write("[DATA ENGINEER](https://www.linkedin.com/in/eugenia-ball/)")

              
        
with col5:
    if st.button("MAURO G. PINI"):
       st.write("[FUNCTIONAL ANALYST](https://www.linkedin.com/in/maurogpini/)")
    else:
        st.write("[FUNCTIONAL ANALYST](https://www.linkedin.com/in/maurogpini/)")
  

st.markdown("---")



st.header(":mailbox: GET IN TOUCH WITH US!")



contact_form = """
<form action="https://formsubmit.co/analytichound@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("./Stream_finalisimo_kpi_last3/style/style.css")




st.markdown("---")


st.markdown(":violet[JOB OPPORTUNITIES:]"  )
st.markdown(" If you want to become a Memeber of the Pack, and work with us in our projects, feel free to send us you resume to : analytichound@gmail.com"  )
