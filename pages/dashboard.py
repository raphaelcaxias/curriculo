import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from config import get_colors
from datetime import datetime, timedelta

def render_dashboard():
    st.markdown("""
    <div class="section-glass" style="min-height:80vh;padding-top:6rem;">
        <div class="container">
            <div class="section-header">
                <span class="label">Business Intelligence</span>
                <h2>Dashboard Interativo</h2>
            </div>
    """, unsafe_allow_html=True)
    c = get_colors()
    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    projetos = ["Análise de Churn","Dashboard de Vendas","Otimização de Preços","Segmentação de Clientes","Previsão de Demanda","Análise de Sentimento","Modelo de Propensão","Automação de Relatórios","Análise de ROI","Monitoramento de KPIs"]
    regioes = ["Sudeste","Sul","Nordeste","Centro-Oeste","Norte"]
    status = ["Concluído","Em Andamento","Planejado"]
    data=[]
    for i in range(150):
        data.append({
            "Projeto": np.random.choice(projetos),
            "Data": np.random.choice(dates),
            "Região": np.random.choice(regioes, p=[0.45,0.20,0.18,0.10,0.07]),
            "Status": np.random.choice(status, p=[0.55,0.30,0.15]),
            "Valor": round(np.random.lognormal(9,0.8),2),
            "Horas": np.random.randint(20,400),
            "Satisfacao": np.random.randint(60,100),
            "Complexidade": np.random.choice(["Baixa","Média","Alta"], p=[0.2,0.5,0.3])
        })
    df = pd.DataFrame(data)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Mes"] = df["Data"].dt.strftime("%Y-%m")

    col1, col2, col3 = st.columns(3)
    with col1:
        periodo = st.selectbox("Período", ["Últimos 6 meses","Últimos 12 meses","Últimos 24 meses"], index=1)
    with col2:
        regiao = st.selectbox("Região", ["Todas"] + sorted(df["Região"].unique().tolist()), index=0)
    with col3:
        status_filtro = st.selectbox("Status", ["Todos"] + sorted(df["Status"].unique().tolist()), index=0)

    df_filtrado = df.copy()
    ultima_data = df["Data"].max()
    if periodo == "Últimos 6 meses":
        data_corte = ultima_data - timedelta(days=180)
    elif periodo == "Últimos 12 meses":
        data_corte = ultima_data - timedelta(days=365)
    else:
        data_corte = ultima_data - timedelta(days=730)
    df_filtrado = df_filtrado[df_filtrado["Data"] >= data_corte]
    if regiao != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Região"] == regiao]
    if status_filtro != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Status"] == status_filtro]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Projetos", f"{len(df_filtrado):,}")
    col2.metric("Receita Total", f"R$ {df_filtrado['Valor'].sum()/1e6:.1f}M")
    col3.metric("Ticket Médio", f"R$ {df_filtrado['Valor'].mean():,.0f}".replace(",","."))
    col4.metric("Satisfação Média", f"{df_filtrado['Satisfacao'].mean():.1f}%")

    fig1 = px.bar(df_filtrado.groupby("Mes").size().reset_index(name="Quantidade").sort_values("Mes"), x="Mes", y="Quantidade", title="Projetos por Mês", color_discrete_sequence=[c["chart_colors"][0]], template=c["plotly_template"])
    fig1.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))
    fig2 = px.pie(df_filtrado.groupby("Região")["Valor"].sum().reset_index(), names="Região", values="Valor", title="Receita por Região", hole=0.4, color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
    fig2.update_layout(height=350, margin=dict(l=10,r=10,t=50,b=20), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))
    fig3 = px.line(df_filtrado.groupby("Mes")["Valor"].sum().reset_index().sort_values("Mes"), x="Mes", y="Valor", title="Evolução da Receita", markers=True, color_discrete_sequence=[c["chart_colors"][1]], template=c["plotly_template"])
    fig3.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))
    fig4 = px.scatter(df_filtrado, x="Horas", y="Valor", color="Complexidade", size="Satisfacao", title="Esforço vs. Retorno", color_discrete_sequence=c["chart_colors"], template=c["plotly_template"])
    fig4.update_layout(height=350, margin=dict(l=20,r=20,t=50,b=40), paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))
    fig5 = px.bar(df_filtrado["Status"].value_counts().reset_index(), x="count", y="Status", orientation="h", title="Status dos Projetos", color="Status", color_discrete_sequence=c["chart_colors"][3:], template=c["plotly_template"])
    fig5.update_layout(height=300, margin=dict(l=20,r=20,t=50,b=20), showlegend=False, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=c["text"]))

    col1, col2 = st.columns(2)
    col1.plotly_chart(fig1, use_container_width=True)
    col2.plotly_chart(fig2, use_container_width=True)
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig3, use_container_width=True)
    col2.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)

    with st.expander("📋 Dados detalhados"):
        st.dataframe(df_filtrado.sort_values("Data", ascending=False), use_container_width=True)

    st.markdown("</div></div>", unsafe_allow_html=True)
