import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from config import get_colors
from datetime import datetime, timedelta

# ============================================================================
# GERADOR DE DADOS SIMULADOS (realistas)
# ============================================================================
def generate_business_data():
    """Gera dados simulados de uma empresa de análise de dados"""
    np.random.seed(42)
    
    # Datas
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Projetos
    projetos = [
        "Análise de Churn", "Dashboard de Vendas", "Otimização de Preços",
        "Segmentação de Clientes", "Previsão de Demanda", "Análise de Sentimento",
        "Modelo de Propensão", "Automação de Relatórios", "Análise de ROI",
        "Monitoramento de KPIs", "Estudo de Mercado", "Recomendação de Produtos"
    ]
    
    regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
    status = ["Concluído", "Em Andamento", "Planejado"]
    
    data = []
    for i in range(150):
        data.append({
            "Projeto": np.random.choice(projetos),
            "Data": np.random.choice(dates),
            "Região": np.random.choice(regioes, p=[0.45, 0.20, 0.18, 0.10, 0.07]),
            "Status": np.random.choice(status, p=[0.55, 0.30, 0.15]),
            "Valor": round(np.random.lognormal(9, 0.8), 2),
            "Horas": np.random.randint(20, 400),
            "Satisfacao": np.random.randint(60, 100),
            "Complexidade": np.random.choice(["Baixa", "Média", "Alta"], p=[0.2, 0.5, 0.3])
        })
    
    df = pd.DataFrame(data)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Mes"] = df["Data"].dt.strftime("%Y-%m")
    df["AnoMes"] = df["Data"].dt.to_period("M")
    return df

# ============================================================================
# DASHBOARD PRINCIPAL
# ============================================================================
def render_dashboard():
    colors = get_colors()
    
    # Carregar dados
    df = generate_business_data()
    
    # ======================== FILTROS ========================
    st.markdown("### Filtros")
    col1, col2, col3 = st.columns(3)
    with col1:
        # Últimos meses
        opcoes_periodo = ["Últimos 6 meses", "Últimos 12 meses", "Últimos 24 meses"]
        periodo = st.selectbox("Período", opcoes_periodo, index=1)
    
    with col2:
        regioes = ["Todas"] + sorted(df["Região"].unique().tolist())
        regiao = st.selectbox("Região", regioes, index=0)
    
    with col3:
        status_opts = ["Todos"] + sorted(df["Status"].unique().tolist())
        status_filtro = st.selectbox("Status", status_opts, index=0)
    
    # Aplicar filtros
    df_filtrado = df.copy()
    
    # Período
    ultima_data = df["Data"].max()
    if periodo == "Últimos 6 meses":
        data_corte = ultima_data - timedelta(days=180)
    elif periodo == "Últimos 12 meses":
        data_corte = ultima_data - timedelta(days=365)
    else:  # 24 meses
        data_corte = ultima_data - timedelta(days=730)
    df_filtrado = df_filtrado[df_filtrado["Data"] >= data_corte]
    
    # Região
    if regiao != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Região"] == regiao]
    
    # Status
    if status_filtro != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Status"] == status_filtro]
    
    # ======================== KPIs ========================
    st.markdown("### Indicadores Gerenciais")
    total_projetos = len(df_filtrado)
    receita_total = df_filtrado["Valor"].sum()
    receita_media = df_filtrado["Valor"].mean()
    satisfacao_media = df_filtrado["Satisfacao"].mean()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Projetos", f"{total_projetos:,}")
    col2.metric("Receita Total", f"R$ {receita_total/1e6:.1f}M")
    col3.metric("Ticket Médio", f"R$ {receita_media:,.0f}".replace(",", "."))
    col4.metric("Satisfação Média", f"{satisfacao_media:.1f}%")
    
    # ======================== GRÁFICOS ========================
    st.markdown("### Análises Visuais")
    
    # GRÁFICO 1: Projetos por Mês (barras)
    df_mes = df_filtrado.groupby("Mes").size().reset_index(name="Quantidade")
    df_mes = df_mes.sort_values("Mes")
    fig1 = px.bar(
        df_mes,
        x="Mes",
        y="Quantidade",
        title="Projetos por Mês",
        color_discrete_sequence=[colors["chart_colors"][0]],
        template=colors["plotly_template"]
    )
    fig1.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=40),
        xaxis_title="Mês",
        yaxis_title="Quantidade de Projetos",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=colors["text"])
    )
    
    # GRÁFICO 2: Distribuição por Região (pizza)
    df_regiao = df_filtrado.groupby("Região")["Valor"].sum().reset_index()
    fig2 = px.pie(
        df_regiao,
        names="Região",
        values="Valor",
        title="Receita por Região",
        hole=0.4,
        color_discrete_sequence=colors["chart_colors"],
        template=colors["plotly_template"]
    )
    fig2.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=50, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=colors["text"])
    )
    
    # GRÁFICO 3: Evolução da Receita (linha)
    df_receita = df_filtrado.groupby("Mes")["Valor"].sum().reset_index()
    df_receita = df_receita.sort_values("Mes")
    fig3 = px.line(
        df_receita,
        x="Mes",
        y="Valor",
        title="Evolução da Receita",
        markers=True,
        color_discrete_sequence=[colors["chart_colors"][1]],
        template=colors["plotly_template"]
    )
    fig3.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=40),
        xaxis_title="Mês",
        yaxis_title="Receita (R$)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=colors["text"])
    )
    
    # GRÁFICO 4: Relação Horas vs. Valor (scatter)
    fig4 = px.scatter(
        df_filtrado,
        x="Horas",
        y="Valor",
        color="Complexidade",
        size="Satisfacao",
        title="Esforço vs. Retorno",
        color_discrete_sequence=colors["chart_colors"],
        template=colors["plotly_template"]
    )
    fig4.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=40),
        xaxis_title="Horas Trabalhadas",
        yaxis_title="Valor do Projeto (R$)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=colors["text"])
    )
    
    # GRÁFICO 5: Status dos Projetos (barra horizontal)
    df_status = df_filtrado["Status"].value_counts().reset_index()
    df_status.columns = ["Status", "Quantidade"]
    fig5 = px.bar(
        df_status,
        x="Quantidade",
        y="Status",
        orientation="h",
        title="Status dos Projetos",
        color="Status",
        color_discrete_sequence=colors["chart_colors"][3:],
        template=colors["plotly_template"]
    )
    fig5.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis_title="Quantidade",
        yaxis_title="",
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color=colors["text"])
    )
    
    # Organizar em grid 2x2
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig1, use_container_width=True)
    col2.plotly_chart(fig2, use_container_width=True)
    
    col1, col2 = st.columns(2)
    col1.plotly_chart(fig3, use_container_width=True)
    col2.plotly_chart(fig4, use_container_width=True)
    
    # Gráfico de status ocupa largura total
    st.plotly_chart(fig5, use_container_width=True)
    
    # ======================== TABELA RESUMO ========================
    with st.expander("📋 Dados detalhados"):
        st.dataframe(df_filtrado.sort_values("Data", ascending=False), use_container_width=True)
