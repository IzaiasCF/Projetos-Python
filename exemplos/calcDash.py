import math
import cmath
from datetime import datetime
from typing import Tuple, Union
import streamlit as st

# ---------- Funções utilitárias ---------- #


def basic_calc(n1: float, n2: float, op: str) -> Union[float, str]:
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "×":
        return n1 * n2
    elif op == "÷":
        if n2 == 0:
            return "Erro: divisão por zero"
        return n1 / n2
    elif op == "^":
        return n1**n2
    else:
        return "Operação inválida"


def scientific_calc(x: float, func: str) -> Union[float, str]:
    try:
        if func == "sin":
            return math.sin(math.radians(x))
        elif func == "cos":
            return math.cos(math.radians(x))
        elif func == "tan":
            return math.tan(math.radians(x))
        elif func == "log10":
            if x <= 0:
                return "Erro: log de número não positivo"
            return math.log10(x)
        elif func == "ln":
            if x <= 0:
                return "Erro: log de número não positivo"
            return math.log(x)
        elif func == "exp":
            return math.exp(x)
        elif func == "sqrt":
            if x < 0:
                return "Erro: raiz de número negativo"
            return math.sqrt(x)
        else:
            return "Função inválida"
    except ValueError as e:
        return f"Erro: {str(e)}"


def calc_bmi(weight_kg: float, height_cm: float) -> Tuple[float, str]:
    if height_cm <= 0:
        return 0.0, "Altura inválida"
    bmi_value = weight_kg / ((height_cm / 100) ** 2)
    if bmi_value < 18.5:
        category = "Abaixo do peso"
    elif bmi_value < 25:
        category = "Peso normal"
    elif bmi_value < 30:
        category = "Sobrepeso"
    else:
        category = "Obesidade"
    return round(bmi_value, 2), category


def quadratic_solve(
    a: float, b: float, c: float
) -> Union[str, Tuple[float, complex, complex]]:
    if a == 0:
        return "Não é uma equação quadrática"
    delta = b**2 - 4 * a * c
    root1 = (-b + cmath.sqrt(delta)) / (2 * a)
    root2 = (-b - cmath.sqrt(delta)) / (2 * a)
    return delta, root1, root2


def loan_payment(principal: float, annual_rate: float, years: int) -> float:
    if principal <= 0 or years <= 0:
        return 0.0
    monthly_rate = annual_rate / 12 / 100
    n_payments = years * 12
    if monthly_rate == 0:
        return principal / n_payments
    payment = (
        principal
        * (monthly_rate * (1 + monthly_rate) ** n_payments)
        / ((1 + monthly_rate) ** n_payments - 1)
    )
    return round(payment, 2)


def length_convert(value: float, unit_from: str, unit_to: str) -> float:
    # Conversões básicas usando metros como referência
    factors = {
        "m": 1,
        "cm": 100,
        "mm": 1000,
        "km": 0.001,
        "in": 39.3701,
        "ft": 3.28084,
        "yd": 1.09361,
        "mi": 0.000621371,
    }
    if unit_from not in factors or unit_to not in factors:
        return 0.0
    return round(value / factors[unit_from] * factors[unit_to], 6)


# ---------- Execução principal ---------- #

if __name__ == "__main__":
    st.set_page_config(
        page_title="🧮 Super Calculadora Dashboard",
        page_icon="🧮",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("🧮 Super Calculadora Dashboard")
    st.caption(
        "Crie, calcule e explore diversos tipos de cálculos em um único lugar! ✨"
    )

    # ---------- Sidebar de navegação ---------- #
    module = st.sidebar.selectbox(
        "📂 Escolha o módulo:",
        (
            "Calculadora Básica",
            "Calculadora Científica",
            "IMC (Índice de Massa Corporal)",
            "Equação Quadrática",
            "Pagamento de Empréstimo",
            "Conversor de Comprimento",
        ),
    )

    st.sidebar.markdown("---")
    st.sidebar.write("Data/Hora local:")
    st.sidebar.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    # ---------- Implementação de cada módulo ---------- #
    if module == "Calculadora Básica":
        st.header("🧮 Calculadora Básica")
        col1, col2, col3 = st.columns(3)
        with col1:
            n1 = st.number_input("Número 1", value=0.0)
        with col2:
            operation = st.selectbox("Operação", ["+", "-", "×", "÷", "^"])
        with col3:
            n2 = st.number_input("Número 2", value=0.0)
        if st.button("Calcular", key="basic"):
            result = basic_calc(n1, n2, operation)
            st.success(f"Resultado: {result}")

    elif module == "Calculadora Científica":
        st.header("🔬 Calculadora Científica")
        x = st.number_input("Valor", value=0.0)
        func = st.selectbox(
            "Função", ["sin", "cos", "tan", "log10", "ln", "exp", "sqrt"], index=0
        )
        if st.button("Calcular", key="scientific"):
            result = scientific_calc(x, func)
            st.success(f"{func}({x}) = {result}")

    elif module == "IMC (Índice de Massa Corporal)":
        st.header("⚖️ Calculadora de IMC")
        weight = st.number_input("Peso (kg)", min_value=0.0, value=70.0)
        height = st.number_input("Altura (cm)", min_value=0.0, value=170.0)
        if st.button("Calcular IMC"):
            bmi_value, category = calc_bmi(weight, height)
            st.metric(label="Seu IMC", value=f"{bmi_value:.2f}")
            st.write(f"Classificação: {category}")

    elif module == "Equação Quadrática":
        st.header("📝 Resolvedor de Equação Quadrática")
        a = st.number_input("a", value=1.0)
        b = st.number_input("b", value=0.0)
        c = st.number_input("c", value=0.0)
        if st.button("Resolver"):
            result = quadratic_solve(a, b, c)
            if isinstance(result, str):
                st.error(result)
            else:
                delta, r1, r2 = result
                st.write(f"Δ (delta) = {delta}")
                st.write(f"x₁ = {r1}")
                st.write(f"x₂ = {r2}")

    elif module == "Pagamento de Empréstimo":
        st.header("🏦 Calculadora de Pagamento de Empréstimo")
        principal = st.number_input(
            "Principal (R$)", min_value=0.0, value=10000.0, step=1000.0
        )
        rate = st.number_input("Taxa Anual (%)", min_value=0.0, value=8.0, step=0.1)
        years = st.number_input("Prazo (anos)", min_value=1, value=5)
        if st.button("Calcular Pagamento Mensal"):
            payment = loan_payment(principal, rate, years)
            st.metric(label="Pagamento Mensal", value=f"R$ {payment:,.2f}")

    elif module == "Conversor de Comprimento":
        st.header("📏 Conversor de Comprimento")
        col1, col2, col3 = st.columns(3)
        with col1:
            value = st.number_input("Valor", value=1.0)
        with col2:
            unit_from = st.selectbox(
                "De", ["m", "cm", "mm", "km", "in", "ft", "yd", "mi"], index=0
            )
        with col3:
            unit_to = st.selectbox(
                "Para", ["m", "cm", "mm", "km", "in", "ft", "yd", "mi"], index=1
            )
        if st.button("Converter"):
            result = length_convert(value, unit_from, unit_to)
            st.success(f"{value} {unit_from} = {result:.6f} {unit_to}")

    # ---------- Rodapé ---------- #
    st.markdown("---")
    st.write("© 2025 – Desenvolvido com ❤ em Python + Streamlit")

    # Para rodar o programa:
    # streamlit run c:/Users/IzaiasCF/Documents/Projetos/Projetos-Python/exemplos/calcDash.py
