import streamlit as st
import os
from config import get_colors
from components import render_skills_chart

def render_home():
    c = get_colors()

    # ================= FOTO =================
    candidatos = [
        "rapha.jpeg","rapha.jpg",
        "assets/rapha.jpeg","assets/rapha.jpg",
        "foto.jpeg","foto.jpg"
    ]
    foto = next((p for p in candidatos if os.path.exists(p)), None)
    foto = foto or "https://ui-avatars.com/api/?name=Raphael+Pires&size=300"

    st.markdown(f"""
    <section class="hero-full">
        <div class="hero-content">
            <img src="{foto}" class="hero-photo">
            <div>
                <h1>Raphael <span>Pires</span></h1>
                <h3>Analista de Dados • Business Intelligence</h3>
                <p>Transformando dados em decisões estratégicas com Python, SQL,
                Power BI, AWS e IA.</p>

                <div class="badge-group">
                    <span class="badge">Python</span>
                    <span class="badge">SQL</span>
                    <span class="badge">Power BI</span>
                    <span class="badge">AWS</span>
                    <span class="badge">IA Generativa</span>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

    st.markdown("## 📈 Indicadores")

    c1,c2,c3,c4,c5,c6 = st.columns(6)
    c1.metric("Experiência","17+ anos")
    c2.metric("Redução","70%")
    c3.metric("Registros","213 mil")
    c4.metric("Dashboards","15+")
    c5.metric("Análises","2h → 15min")
    c6.metric("Dados","R$ 50 bi")

    st.divider()

    st.header("💼 Experiência")
    st.info("Utilize uma timeline em componentes separados para facilitar manutenção.")

    st.header("🚀 Projetos")
    st.markdown("""
- Desenrola Brasil
- CNPq Analytics
- ANP Analytics
- Portfólio Premium
""")

    st.header("☁️ Jornada AWS")
    st.progress(40)
    st.write("Meta: AWS Cloud Practitioner")

    st.header("🛠 Competências")
    render_skills_chart()

    st.header("📬 Contato")
    st.write("""
- LinkedIn
- GitHub
- Email
- WhatsApp
""")
