import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from config import get_colors
from datetime import datetime, timedelta

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

def generate_projetos():
    np.random.seed(456)
    projetos = ["Churn","Vendas","Preços","Segmentação","Demanda","Sentimento","Propensão","Automação","ROI","KPIs","Mercado","Recomendação"]
    regioes = ["Sudeste","Sul","Nordeste","Centro-Oeste","Norte"]
    status = ["Concluído","Em Andamento","Planejado"]
    complexidade = ["Baixa","Média","Alta"]
    data = []
    for _ in range(200):
        data.append({
            "Projeto": np.random.choice(projetos),
            "Região": np.random.choice(regioes, p=[0.45,0.20,0.18,0.10,0.07]),
            "Status": np.random.choice(status, p=[0.55,0.30,0.15]),
            "Complexidade": np.random.choice(complexidade, p=[0.2,0.5,0.3]),
            "Horas": np.random.randint(20, 400),
            "Valor": round(np.random.lognormal(9, 0.8), 2),
            "Satisfacao": np.random.randint(60, 100)
        })
    return pd.DataFrame(data)

def render_analytics_dashboard():
    colors = get_colors()
    st.markdown("### Análise de Dados Interativa")
    
    tabs = st.tabs(["📊 Projetos", "🇧🇷 Desenrola", "⛽ ANP", "📈 Correlações"])
    
    with tabs[0]:
        df = generate_projetos()
        col1, col2 = st.columns(2)
        with col1:
            regioes = st.multiselect("Região", df["Região"].unique(), default=df["Região"].unique())
        with col2:
            status = st.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())
        filtro = df[(df["Região"].isin(regioes)) & (df["Status"].isin(status))]
        if filtro.empty:
            st.warning("Nenhum dado para os filtros selecionados.")
            return
        # KPIs
        k1,k2,k3,k4 = st.columns(4)
        k1.metric("Projetos", len(filtro))
        k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f}M")
        k3.metric("Média Horas", f"{filtro['Horas'].mean():.0f}h")
        k4.metric("Satisfação", f"{filtro['Satisfacao'].mean():.1f}%")
        # Gráficos
        c1, c2 = st.columns(2)
        fig1 = px.bar(filtro.groupby("Complexidade")["Valor"].sum().reset_index(), x="Complexidade", y="Valor", color="Complexidade", title="Valor por Complexidade", color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
        fig1.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
        fig2 = px.pie(filtro, names="Região", values="Valor", hole=0.5, title="Receita por Região", color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
        fig2.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
        c1.plotly_chart(fig1, use_container_width=True)
        c2.plotly_chart(fig2, use_container_width=True)
        # Tabela
        with st.expander("📋 Dados detalhados"):
            st.dataframe(filtro, use_container_width=True)
    
    with tabs[1]:
        df = generate_desenrola()
        col1, col2 = st.columns(2)
        with col1:
            regioes = st.multiselect("Região (Desenrola)", df["Região"].unique(), default=df["Região"].unique(), key="des_reg")
        with col2:
            status = st.multiselect("Status (Desenrola)", df["Status"].unique(), default=df["Status"].unique(), key="des_status")
        filtro = df[(df["Região"].isin(regioes)) & (df["Status"].isin(status))]
        if filtro.empty:
            st.warning("Nenhum dado.")
            return
        k1,k2,k3 = st.columns(3)
        k1.metric("Contratos", f"{len(filtro):,}")
        k2.metric("Valor Total", f"R$ {filtro['Valor'].sum()/1e6:.1f}M")
        k3.metric("Taxa Sucesso", f"{(filtro['Status']=='Renegociado').mean()*100:.1f}%")
        fig1 = px.pie(filtro, names="Região", values="Valor", hole=0.5, color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
        fig1.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
        fig2 = px.bar(filtro.groupby("Faixa", observed=False)["Valor"].sum().reset_index(), x="Faixa", y="Valor", color_discrete_sequence=[colors["chart_colors"][0]], template=colors["plotly_template"])
        fig2.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
        c1,c2 = st.columns(2)
        c1.plotly_chart(fig1, use_container_width=True)
        c2.plotly_chart(fig2, use_container_width=True)
    
    with tabs[2]:
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
        k1,k2 = st.columns(2)
        k1.metric("Preço Atual", f"R$ {filtro[filtro['Mês']=='Jun']['Preço'].values[0]:.2f}")
        variacao = (filtro["Preço"].max() - filtro["Preço"].min()) / filtro["Preço"].min() * 100
        k2.metric("Variação Semestral", f"{variacao:.1f}%")
        fig = px.line(filtro, x="Mês", y="Preço", markers=True, color_discrete_sequence=[colors["chart_colors"][0]], template=colors["plotly_template"])
        fig.update_layout(height=400, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
        st.plotly_chart(fig, use_container_width=True)
    
    with tabs[3]:
        st.markdown("### Análise de Correlações")
        df = generate_projetos()
        # Correlação Horas vs Valor
        fig = px.scatter(df, x="Horas", y="Valor", color="Complexidade", size="Satisfacao", title="Correlação: Horas vs Valor", template=colors["plotly_template"], color_discrete_sequence=colors["chart_colors"])
        fig.update_layout(height=400, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
        st.plotly_chart(fig, use_container_width=True)
        # Boxplot por região
        fig2 = px.box(df, x="Região", y="Valor", color="Região", title="Distribuição de Valor por Região", template=colors["plotly_template"], color_discrete_sequence=colors["chart_colors"])
        fig2.update_layout(height=400, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
        st.plotly_chart(fig2, use_container_width=True)
        # Tabela de correlação
        st.dataframe(df[["Horas","Valor","Satisfacao"]].corr(), use_container_width=True)
