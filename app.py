import streamlit as st
from renderer import generate_contract

st.set_page_config(page_title="Gerador de Contratos", page_icon="📄", layout="wide")

st.sidebar.title("Menu")
choice = st.sidebar.radio("Navegação", ["Gerar Contrato"])

if choice == "Gerar Contrato":
    st.title("Gerar Contrato de Permuta")
    project = st.text_input("Nome do Projeto")
    contratante = st.text_input("Contratante (nome/razão social)")
    contratado = st.text_input("Contratado (nome/razão social)")
    quantidade_debentures = st.text_input("Quantidade de debêntures")
    quantidade_cotas = st.text_input("Quantidade de cotas")
    valor = st.text_input("Valor (R$)")
    cidade = st.text_input("Cidade")
    data = st.date_input("Data do Contrato")

    st.subheader("Cláusulas adicionais")
    clauses = []
    if st.checkbox("Adicionar Confidencialidade"):
        clauses.append({
            "titulo": "Confidencialidade",
            "texto": "As partes obrigam-se a manter sigilo sobre todas as informações relativas a este contrato."
        })

    st.subheader("Formatação das cláusulas")
    font = st.selectbox("Fonte cláusulas adicionais", ["Arial", "Times New Roman", "Calibri"])
    bold = st.checkbox("Negrito")
    italic = st.checkbox("Itálico")
    caps = st.checkbox("Caixa Alta")

    if st.button("Gerar Word"):
        styles = {"clausulas_extra": {"font": font, "bold": bold, "italic": italic, "caps": caps}}
        context = {
            "contratante_nome": contratante,
            "contratado_nome": contratado,
            "quantidade_debentures": quantidade_debentures,
            "quantidade_cotas": quantidade_cotas,
            "valor": valor,
            "cidade": cidade,
            "data_contrato": data.isoformat()
        }
        output = "contratos_gerados/ContratoPermuta.docx"
        generate_contract("templates/exemplo_template.docx", context, clauses, styles, output)
        with open(output, "rb") as f:
            st.download_button("⬇️ Baixar Contrato", f, file_name="ContratoPermuta.docx")

