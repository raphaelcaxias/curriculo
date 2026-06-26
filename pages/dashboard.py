import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from config import get_colors
from datetime import datetime, timedelta

def generate_business_data():
    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    projetos = ["Churn","Vendas","Preços","Segmentação","Demanda","Sentimento","Propensão","Automação","ROI","KPIs","Mercado","Recomendação"]
    regioes = ["Sudeste","Sul","Nordeste","Centro-Oeste","Norte"]
    status = ["Concluído","Em Andamento","Planejado"]
    complexidade = ["Baixa","Média","Alta"]
    
    data = []
    for i in range(200):
        data.append({
            "Projeto": np.random.choice(projetos),
            "Data": np.random.choice(dates),
            "Região": np.random.choice(regioes, p=[0.45,0.20,0.18,0.10,0.07]),
            "Status": np.random.choice(status, p=[0.55,0.30,0.15]),
            "Complexidade": np.random.choice(complexidade, p=[0.2,0.5,0.3]),
            "Valor": round(np.random.lognormal(9, 0.8), 2),
            "Horas": np.random.randint(20, 400),
            "Satisfacao": np.random.randint(60, 100)
        })
    df = pd.DataFrame(data)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Mes"] = df["Data"].dt.strftime("%Y-%m")
    return df

def render_dashboard():
    colors = get_colors()
    df = generate_business_data()
    
    # ======================== FILTROS ========================
    st.markdown("### Filtros")
    col1, col2, col3 = st.columns(3)
    with col1:
        periodo = st.selectbox("Período", ["Últimos 6 meses", "Últimos 12 meses", "Últimos 24 meses"], index=1)
    with col2:
        regiao = st.selectbox("Região", ["Todas"] + sorted(df["Região"].unique().tolist()))
    with col3:
        status_filtro = st.selectbox("Status", ["Todos"] + sorted(df["Status"].unique().tolist()))
    
    # Aplicar filtros
    df_filtrado = df.copy()
    ultima_data = df["Data"].max()
    if periodo == "Últimos 6 meses":
        df_filtrado = df_filtrado[df_filtrado["Data"] >= ultima_data - timedelta(days=180)]
    elif periodo == "Últimos 24 meses":
        df_filtrado = df_filtrado[df_filtrado["Data"] >= ultima_data - timedelta(days=730)]
    else:
        df_filtrado = df_filtrado[df_filtrado["Data"] >= ultima_data - timedelta(days=365)]
    if regiao != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Região"] == regiao]
    if status_filtro != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Status"] == status_filtro]
    
    # ======================== KPIs ========================
    st.markdown("### Indicadores Gerenciais")
    total = len(df_filtrado)
    receita = df_filtrado["Valor"].sum()
    ticket = df_filtrado["Valor"].mean()
    satisfacao = df_filtrado["Satisfacao"].mean()
    eficiencia = (receita / df_filtrado["Horas"].sum()) if df_filtrado["Horas"].sum() > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projetos", f"{total:,}")
    col2.metric("Receita Total", f"R$ {receita/1e6:.1f}M")
    col3.metric("Ticket Médio", f"R$ {ticket:,.0f}".replace(",", "."))
    col4.metric("Satisfação", f"{satisfacao:.1f}%")
    
    col1, col2 = st.columns(2)
    col1.metric("Eficiência (R$/h)", f"R$ {eficiencia:.2f}")
    # Projetos por status
    status_count = df_filtrado["Status"].value_counts().to_dict()
    col2.metric("Concluídos", status_count.get("Concluído", 0))
    
    # ======================== GRÁFICOS ========================
    st.markdown("### Análises Visuais")
    
    # Gráfico 1: Barras - Projetos por mês
    df_mes = df_filtrado.groupby("Mes").size().reset_index(name="Quantidade")
    df_mes = df_mes.sort_values("Mes")
    fig1 = px.bar(df_mes, x="Mes", y="Quantidade", title="Projetos por Mês", color_discrete_sequence=[colors["chart_colors"][0]], template=colors["plotly_template"])
    fig1.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    
    # Gráfico 2: Pizza - Receita por região
    df_reg = df_filtrado.groupby("Região")["Valor"].sum().reset_index()
    fig2 = px.pie(df_reg, names="Região", values="Valor", title="Receita por Região", hole=0.4, color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
    fig2.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig1, use_container_width=True)
    col2.plotly_chart(fig2, use_container_width=True)
    
    # Gráfico 3: Linha - Evolução da receita
    df_rec = df_filtrado.groupby("Mes")["Valor"].sum().reset_index()
    df_rec = df_rec.sort_values("Mes")
    fig3 = px.line(df_rec, x="Mes", y="Valor", title="Evolução da Receita", markers=True, color_discrete_sequence=[colors["chart_colors"][1]], template=colors["plotly_template"])
    fig3.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    
    # Gráfico 4: Scatter - Horas vs Valor com regressão
    fig4 = px.scatter(df_filtrado, x="Horas", y="Valor", color="Complexidade", size="Satisfacao", title="Esforço vs Retorno", color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
    fig4.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig3, use_container_width=True)
    col2.plotly_chart(fig4, use_container_width=True)
    
    # Gráfico 5: Boxplot - Satisfação por região
    fig5 = px.box(df_filtrado, x="Região", y="Satisfacao", color="Região", title="Satisfação por Região", color_discrete_sequence=colors["chart_colors"], template=colors["plotly_template"])
    fig5.update_layout(height=350, paper_bgcolor="rgba(0,0,0,0)", font=dict(color=colors["text"]))
    st.plotly_chart(fig5, use_container_width=True)
    
    # ======================== RANKING DE PROJETOS ========================
    st.markdown("### Ranking de Performance")
    df_rank = df_filtrado.groupby("Projeto").agg({
        "Valor": "sum",
        "Horas": "sum",
        "Satisfacao": "mean"
    }).reset_index()
    df_rank["Eficiencia"] = df_rank["Valor"] / df_rank["Horas"]
    df_rank = df_rank.sort_values("Eficiencia", ascending=False)
    st.dataframe(df_rank, use_container_width=True)
    
    # ======================== EXPORTAR ========================
    st.download_button(
        label="📥 Exportar dados (CSV)",
        data=df_filtrado.to_csv(index=False),
        file_name="dados_dashboard.csv",
        mime="text/csv"
    )
