# Código para gerar o README.md automaticamente
readme_content = """
# **ATENA.APP**

**ATENA.APP** é um sistema simples e intuitivo de gestão de informações de alunos, desenvolvido em Python usando a biblioteca Tkinter para a interface gráfica. O aplicativo permite registrar, monitorar e gerar relatórios sobre o desempenho acadêmico e a frequência de alunos, com foco em evitar a evasão escolar.

## **Funcionalidades**

1. **Registro de Dados Pessoais:**
   - Nome do aluno.
   - Série do aluno.

2. **Registro de Frequência:**
   - Permite registrar a frequência do aluno em porcentagem.

3. **Cadastro de Notas:**
   - Permite adicionar notas ao histórico do aluno.

4. **Cálculo de Média:**
   - Calcula a média das notas cadastradas.

5. **Avaliação de Risco de Evasão:**
   - Avalia o risco de evasão com base na média das notas e na frequência registrada. Se a média for inferior a 70 ou a frequência for inferior a 75%, o aluno é considerado em risco de evasão.

6. **Geração de Relatório:**
   - Gera um relatório com informações detalhadas sobre o aluno, incluindo:
     - Nome, Série, Frequência.
     - Histórico de Notas.
     - Média das Notas.
     - Status de Risco de Evasão (Sim/Não).

---

## **Instalação e Requisitos**

### **Pré-requisitos**

- **Python** versão 3.6 ou superior.
- **Tkinter** (normalmente já incluído na instalação padrão do Python).

### **Passos para Instalar**

1. **Instalar Python:**
   - Baixe e instale o Python através do site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   
2. **Verificar Tkinter:**
   - Tkinter já vem instalado com Python na maioria dos sistemas. Se necessário, instale o Tkinter com o seguinte comando (no terminal ou prompt de comando):
   
   ```bash
   pip install tk
