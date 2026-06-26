import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from config import get_colors

def generate_desenrola_data():
    """Gera dados para análise do Desenrola Brasil"""
    np.random.seed(42)
    regioes = ["Sudeste", "Nordeste", "Sul", "Centro-Oeste", "Norte"]
    faixas = ["Até R$ 5k", "R$ 5k-15k", "R$ 15k-50k", "Acima R$ 50k"]
    
    return pd.DataFrame({
        "Região": np.random.choice(regioes, 400, p=[0.45, 0.28, 0.15, 0.07, 0.05]),
        "Faixa": np.random.choice(faixas, 400, p=[0.55, 0.28, 0.12, 0.05]),
        "Valor": np.random.lognormal(mean=8.5, sigma=1.2, size=400),
        "Status": np.random.choice(["Renegociado", "Em Negociação", "Inadimplente"], 400, p=[0.65, 0.25, 0.10])
    })

def generate_anp_data():
    """Gera dados para análise da ANP"""
    np.random.seed(123)
    estados = ["SP", "RJ", "MG", "RS", "PR", "BA"]
    combustiveis = ["Gasolina", "Etanol", "Diesel"]
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
    
    dados = []
    for estado in estados:
        for comb in combustiveis:
            base = {"Gasolina": 5.8, "Etanol": 3.5, "Diesel": 5.2}[comb]
            for mes in meses:
                dados.append({
                    "Estado": estado,
                    "Combustível": comb,
                    "Mês": mes,
                    "Preço": base + np.random.normal(0, 0.15)
                })
    return pd.DataFrame(dados)

def generate_operational_data():
    """Gera dados de impacto operacional"""
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
    return pd.DataFrame({
        "Mês": meses * 2,
        "Tipo": ["Antes"] * 12 + ["Após"] * 12,
        "Horas": [120, 125, 118, 130, 122, 128, 126, 124, 129, 127, 125, 130] +
                [95, 70, 55, 45, 38, 35, 33, 32, 30, 29, 28, 27]
    })

def render_desenrola():
    """Renderiza análise do Desenrola Brasil"""
    st.markdown("### Análise de Renegociações")
    
    df = generate_desenrola_data()
    colors = get_colors()
    
    col1, col2 = st.columns(2)
    with col1:
        regioes = st.multiselect("Região", df["Região"].unique(), default=df["Região"].unique())
    with col2:
        status = st.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())
    
    df_filtered = df[(df["Região"].isin(regioes)) & (df["Status"].isin(status))]
    
    if len(df_filtered) == 0:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")
        return
    
    # Métricas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Contratos", f"{len(df_filtered):,}".replace(",", "."))
    with col2:
        st.metric("Valor Total", f"R$ {df_filtered['Valor'].sum()/1e6:.1f}M")
    with col3:
        st.metric("Taxa Sucesso", f"{(df_filtered['Status']=='Renegociado').mean()*100:.1f}%")
    
    # Gráficos
    col1, col2 = st.columns(2)
    with col1:
        fig_pie = px.pie(
            df_filtered,
            names="Região",
            values="Valor",
            hole=0.55,
            color_discrete_sequence=colors["chart_colors"],
            template=colors["plotly_template"]
        )
        fig_pie.update_layout(
            margin=dict(l=10, r=10, t=10, b=10),
            height=320,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter", color=colors["text"])
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        fig_bar = px.bar(
            df_filtered.groupby("Faixa", observed=False)["Valor"].sum().reset_index(),
            x="Faixa",
            y="Valor",
            color_discrete_sequence=[colors["chart_colors"][0]],
            template=colors["plotly_template"]
        )
        fig_bar.update_layout(
            margin=dict(l=10, r=10, t=10, b=10),
            height=320,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Inter", color=colors["text"]),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)")
        )
        st.plotly_chart(fig_bar, use_container_width=True)

def render_anp():
    """Renderiza análise de combustíveis ANP"""
    st.markdown("### Preços de Combustíveis")
    
    df = generate_anp_data()
    colors = get_colors()
    
    col1, col2 = st.columns(2)
    with col1:
        estado = st.selectbox("Estado", df["Estado"].unique())
    with col2:
        combustivel = st.selectbox("Combustível", df["Combustível"].unique())
    
    df_filtered = df[(df["Estado"] == estado) & (df["Combustível"] == combustivel)]
    
    col1, col2 = st.columns(2)
    with col1:
        preco_atual = df_filtered[df_filtered["Mês"] == "Jun"]["Preço"].values[0]
        st.metric("Preço Atual", f"R$ {preco_atual:.2f}")
    with col2:
        variacao = ((df_filtered["Preço"].max() - df_filtered["Preço"].min()) / df_filtered["Preço"].min()) * 100
        st.metric("Variação Semestral", f"{variacao:.1f}%")
    
    fig = px.line(
        df_filtered,
        x="Mês",
        y="Preço",
        markers=True,
        color_discrete_sequence=[colors["chart_colors"][0]],
        template=colors["plotly_template"]
    )
    fig.update_layout(
        title=f"{combustivel} - {estado}",
        margin=dict(l=20, r=20, t=50, b=20),
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=colors["text"]),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)")
    )
    st.plotly_chart(fig, use_container_width=True)

def render_operational():
    """Renderiza análise de impacto operacional"""
    st.markdown("### Impacto da Automação")
    
    df = generate_operational_data()
    colors = get_colors()
    
    fig = px.line(
        df,
        x="Mês",
        y="Horas",
        color="Tipo",
        markers=True,
        color_discrete_sequence=[colors["chart_colors"][3], colors["chart_colors"][0]],
        template=colors["plotly_template"]
    )
    fig.update_layout(
        title="Evolução de Horas - Antes vs Após Automação",
        margin=dict(l=20, r=20, t=60, b=20),
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color=colors["text"]),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="rgba(148,163,184,0.1)")
    )
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Horas Economizadas", "1.108 h", "+93% eficiência")
    with col2:
        st.metric("Custo Evitado", "R$ 185k", "vs. contratação")
    with col3:
        st.metric("Projetos Entregues", "24", "+60% vs. ano anterior")

def main():
    st.markdown("""
    <div class="section-header">
        <span class="section-label">Análise ao Vivo</span>
        <h2 class="section-title">Demonstração analítica</h2>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs(["🇧🇷 Desenrola Brasil", "⛽ Combustíveis ANP", "📊 Impacto Operacional"])
    
    with tabs[0]:
        render_desenrola()
    
    with tabs[1]:
        render_anp()
    
    with tabs[2]:
        render_operational()

if __name__ == "__main__":
    main()
