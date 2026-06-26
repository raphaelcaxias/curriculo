import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from config import get_colors

def generate_desenrola():
    np.random.seed(42)
    regioes = ["Sudeste","Nordeste","Sul","Centro-Oeste","Norte"]
    faixas = ["Até R$5k","R$5k-15k","R$15k-50k","Acima R$50k"]
    return pd.DataFrame({
        "Região": np.random.choice(regioes, 400, p=[0.45,0.28,0.15,0.07,0.05]),
        "Faixa": np.random.choice(faixas, 400, p=[0.55,0.28,0.12,0.05]),
        "Valor": np.random.lognormal(8.5,1.2,400),
        "Status": np.random.choice(["Renegociado","Em Negociação","Inadimplente"], 400, p=[0.65,0.25,0.10])
    })

def generate_anp():
    np.random.seed(123)
    estados = ["SP","RJ","MG","RS","PR","BA"]
    comb = ["Gasolina","Etanol","Diesel"]
    meses = ["Jan","Fev","Mar","Abr","Mai","Jun"]
    data=[]
    for e in estados:
        for c in comb:
            base = {"Gasolina":5.8,"Etanol":3.5,"Diesel":5.2}[c]
            for m in meses:
                data.append({"Estado":e,"Combustível":c,"Mês":m,"Preço":base+np.random.normal(0,0.15)})
    return pd.DataFrame(data)

def render_analytics_dashboard():
    colors = get_colors()
    st.markdown("### Análise de Dados Interativa")
    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Combustíveis ANP", "📈 Impacto Operacional"])

    with tabs[0]:
        df = generate_desenrola()
        col1, col2 = st.columns(2)
        with col1:
            regioes = st.multiselect("Região", df["Região"].unique(), default=df["Região"].unique())
        with col2:
            status = st.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())
        filtro = df[(df["Região"].isin(regioes)) & (df["Status"].isin(status))]
        if filtro.empty:
            st.warning("Nenhum dado para os filtros selecionados.")
            return
        k1,k2,k3 = st.columns(3)
        k1.metric("Contratos", f"{len(filtro):,}")
        k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f}M")
        k3.metric("Taxa Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
        fig1 = px.pie(filtro, names="Região", values="Valor", hole=0.5, color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
        fig1.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="rgba(0,0,0,0)")
        fig2 = px.bar(filtro.groupby("Faixa", observed=False)["Valor"].sum().reset_index(), x="Faixa", y="Valor", color_discrete_sequence=[colors["chart_colors"][0]], template=colors["plotly_template"])
        fig2.update_layout(height=350, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="rgba(0,0,0,0)")
        col1, col2 = st.columns(2)
        col1.plotly_chart(fig1, use_container_width=True)
        col2.plotly_chart(fig2, use_container_width=True)

    with tabs[1]:
        df = generate_anp()
        col1, col2 = st.columns(2)
        with col1:
            estado = st.selectbox("Estado", df["Estado"].unique())
        with col2:
            combustivel = st.selectbox("Combustível", df["Combustível"].unique())
        filtro = df[(df["Estado"]==estado) & (df["Combustível"]==combustivel)]
        if filtro.empty:
            st.warning("Nenhum dado.")
            return
        k1, k2 = st.columns(2)
        k1.metric("Preço Atual", f"R$ {filtro[filtro['Mês']=='Jun']['Preço'].values[0]:.2f}")
        variacao = (filtro["Preço"].max() - filtro["Preço"].min()) / filtro["Preço"].min() * 100
        k2.metric("Variação Semestral", f"{variacao:.1f}%")
        fig = px.line(filtro, x="Mês", y="Preço", markers=True, color_discrete_sequence=[colors["chart_colors"][0]], template=colors["plotly_template"])
        fig.update_layout(height=400, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
        df = pd.DataFrame({
            "Mês": meses*2,
            "Tipo": ["Antes"]*12 + ["Após"]*12,
            "Horas": [120,125,118,130,122,128,126,124,129,127,125,130] + [95,70,55,45,38,35,33,32,30,29,28,27]
        })
        fig = px.line(df, x="Mês", y="Horas", color="Tipo", markers=True, color_discrete_sequence=[colors["chart_colors"][3], colors["chart_colors"][0]], template=colors["plotly_template"])
        fig.update_layout(height=400, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
        k1,k2,k3 = st.columns(3)
        k1.metric("Horas Economizadas", "1.108 h", "+93% eficiência")
        k2.metric("Custo Evitado", "R$ 185k", "vs. contratação")
        k3.metric("Projetos Entregues", "24", "+60% vs. anterior")
