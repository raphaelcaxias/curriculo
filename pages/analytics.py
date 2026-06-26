import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from config import get_colors

# -----------------------------
# Analytics Premium Refatorado
# -----------------------------

def _card_metric(cols, title, value, delta=None):
    for c, t, v, d in zip(cols, title, value, delta or [None]*len(cols)):
        c.metric(t, v, d)


def render_analytics():
    c = get_colors()

    st.title("📊 Analytics Interativo")
    st.caption("Demonstrações construídas em Streamlit + Plotly")

    tabs = st.tabs([
        "🇧🇷 Desenrola Brasil",
        "⛽ ANP",
        "📈 Impacto Operacional"
    ])

    # ---------------- DESENROLA ----------------
    with tabs[0]:
        np.random.seed(42)

        regioes=["Sudeste","Nordeste","Sul","Centro-Oeste","Norte"]
        status=["Renegociado","Em Negociação","Inadimplente"]

        df=pd.DataFrame({
            "Região":np.random.choice(regioes,400,p=[.45,.28,.15,.07,.05]),
            "Valor":np.random.lognormal(8.5,1.2,400),
            "Status":np.random.choice(status,400,p=[.65,.25,.10])
        })

        f1,f2=st.columns(2)
        reg=f1.multiselect("Região",regioes,default=regioes)
        stat=f2.multiselect("Status",status,default=status)

        filtro=df[df.Região.isin(reg)&df.Status.isin(stat)]

        if filtro.empty:
            st.info("Nenhum registro encontrado.")
        else:
            _card_metric(
                st.columns(3),
                ["Contratos","Valor","Sucesso"],
                [
                    f"{len(filtro):,}",
                    f"R$ {filtro.Valor.sum()/1e6:.1f} M",
                    f"{(filtro.Status=='Renegociado').mean()*100:.1f}%"
                ]
            )

            a,b=st.columns(2)

            fig1=px.pie(
                filtro,
                names="Região",
                values="Valor",
                hole=.6,
                template=c["plotly_template"]
            )

            fig2=px.histogram(
                filtro,
                x="Status",
                color="Status",
                template=c["plotly_template"]
            )

            a.plotly_chart(fig1,use_container_width=True)
            b.plotly_chart(fig2,use_container_width=True)

    # ---------------- ANP ----------------
    with tabs[1]:
        estados=["SP","RJ","MG","PR"]
        meses=["Jan","Fev","Mar","Abr","Mai","Jun"]

        dados=[]
        np.random.seed(1)

        for e in estados:
            preco=5.4
            for m in meses:
                preco+=np.random.normal(0,.10)
                dados.append([e,m,preco])

        df=pd.DataFrame(dados,columns=["Estado","Mês","Preço"])

        estado=st.selectbox("Estado",estados)

        f=df[df.Estado==estado]

        st.metric("Preço Médio",f"R$ {f.Preço.mean():.2f}")

        fig=px.line(
            f,
            x="Mês",
            y="Preço",
            markers=True,
            template=c["plotly_template"]
        )

        st.plotly_chart(fig,use_container_width=True)

    # ---------------- IMPACTO ----------------
    with tabs[2]:

        antes=[120,125,118,130,122,128,126,124,129,127,125,130]
        depois=[95,70,55,45,38,35,33,32,30,29,28,27]

        meses=["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]

        df=pd.DataFrame({
            "Mês":meses*2,
            "Horas":antes+depois,
            "Período":["Antes"]*12+["Depois"]*12
        })

        fig=px.area(
            df,
            x="Mês",
            y="Horas",
            color="Período",
            template=c["plotly_template"]
        )

        st.plotly_chart(fig,use_container_width=True)

        _card_metric(
            st.columns(3),
            ["Horas Economizadas","Custo Evitado","Projetos"],
            ["1.108 h","R$ 185 mil","24"],
            ["+93%","+185 mil","+60%"]
        )
