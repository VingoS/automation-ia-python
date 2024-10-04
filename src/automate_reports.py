import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Função para carregar e processar os dados financeiros
def load_financial_data(filepath):
    df = pd.read_csv(filepath)
    return df

# Função para gerar gráfico de lucro e despesas
def generate_graph(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Data'], df['Lucro'], label='Lucro', marker='o')
    plt.plot(df['Data'], df['Despesas'], label='Despesas', marker='o')
    plt.title('Relatório Financeiro - Lucro vs Despesas')
    plt.xlabel('Data')
    plt.ylabel('Valor (R$)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('relatorio_grafico.png')  # Salvar gráfico como PNG
    plt.close()

# Função para gerar o relatório em PDF
def generate_pdf_report(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título
    pdf.cell(200, 10, txt="Relatório Financeiro", ln=True, align="C")

    # Inserir gráfico
    pdf.image('relatorio_grafico.png', x=10, y=30, w=180)

    # Adicionar tabela de dados
    pdf.ln(85)  # Espaço após gráfico
    for i in range(len(df)):
        pdf.cell(200, 10, txt=f"{df['Data'][i]} - Lucro: R${df['Lucro'][i]} - Despesas: R${df['Despesas'][i]}", ln=True)
    
    pdf.output("relatorio_financeiro.pdf")
    print("Relatório gerado e salvo como 'relatorio_financeiro.pdf'.")

# Fluxo principal
if __name__ == "__main__":
    # Carregar dados
    df = load_financial_data('data/financial_data.csv')

    # Gerar gráfico
    generate_graph(df)

    # Gerar PDF
    generate_pdf_report(df)