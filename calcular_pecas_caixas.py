import os
import pdfkit
from datetime import datetime

now = datetime.now

output_PDF = os.path.abspath("new_file.pdf")
config = pdfkit.configuration(wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

#custos das madeiras
custo_ripa = float(input("Valor da ripa UN: "))
custo_tabua = float(input("Valor da tábua UN: "))

#custos das peças
custo_modulo = custo_ripa/6.125
custo_lixeira_tampa = custo_tabua/10
print("Custo do módulo UN: ", custo_modulo)
print("Custo da lixeira/tampa UN: ", custo_lixeira_tampa)

#markup(%) ou margem de lucro(R$)
print("1 - Markup(%)\n2 - Margem de lucro(R$)")
option = float(input("Opção (1 ou 2): "))

#calculo markup
if (option == 1 ):
    markup_modulo = float(input("Insira o markup em % do módulo: "))
    val_modulo = custo_modulo * (markup_modulo/100) + custo_modulo
    
    markup_lixeira = float(input("Insira o markup em % da lixeira: "))
    val_lixeira = custo_lixeira_tampa * (markup_lixeira/100) + custo_lixeira_tampa
    
    markup_tampa = float(input("Insira o markup em % da tampa: "))
    val_tampa = custo_lixeira_tampa * (markup_tampa/100) + custo_lixeira_tampa
    print("Valor do módulo UN: ", val_modulo)
    print("Valor da lixeira UN: ", val_lixeira)
    print("Valor da tampa UN: ", val_tampa)

#calculo margem de lucro
if (option == 2):
    margem_de_lucro_modulo = float(input("Insira a margem de lucro em R$ do modulo: "))
    val_modulo = custo_modulo + margem_de_lucro_modulo
    
    margem_de_lucro_lixeira = float(input("Insira a margem de lucro em R$ da lixeira: "))
    val_lixeira = custo_lixeira_tampa + margem_de_lucro_lixeira

    margem_de_lucro_tampa = float(input("Insira a margem de lucro em R$ da tampa: "))
    val_tampa = custo_lixeira_tampa + margem_de_lucro_tampa
    
    print("Valor do módulo UN: ", val_modulo)
    print("Valor da lixeira UN: ", val_lixeira)
    print("Valor da tampa UN: ", val_tampa)

#calculo da venda
print("Digite a quantidade quer irá vender de...")
quant_modulo = float(input("Módulos: "))
venda_modulo = quant_modulo*val_modulo

quant_lixeira = float(input("Lixeiras: "))
venda_lixeira = quant_lixeira*val_lixeira

quant_tampa = float(input("Tampas: "))
venda_tampa = quant_tampa*val_tampa

venda_total = venda_modulo + venda_lixeira + venda_tampa

vendedor = input("Vendedor: ")

print("Valor total de módulos: ",venda_modulo)
print("Valor total de lixeiras: ",venda_lixeira)
print("Valor total de tampas: ",venda_tampa)
print("Valor total da venda: ",venda_total)
if(float(input("Gerar nota?\n1 - Sim\n")) == 1):
    os.system('cls' if os.name == 'nt' else 'clear')
    #print("#-- Meliponário Bernhardt --#\n|")
    #print(f"|{quant_modulo:.0f}x Módulos - R${val_modulo:.2f}(UN)")
    #print(f"|{quant_lixeira:.0f}x Lixeiras - R${val_lixeira:.2f}(UN)")
    #print(f"|{quant_tampa:.0f}x Tampas - R${val_tampa:.2f}(UN)\n|")
    #print(f"|TOTAL: R${venda_total:.2f}")
    print("#---------------------------#\n")
    print("GERANDO PDF...")

#cria PDF
s = f"""<h3><strong>Meliponario Bernhardt</strong></h1>
       <p>Taquara - RS - 95600-538</p>
       <p>CPF/CNPJ: 00000000000</p>
       <p>E-mail: contact@bryandbernhardt.com</p>
       <p>Fone: (55)95555-5555</p>
       <hr/>
       <p>Data da venda: {datetime.today().strftime('%d-%m-%Y %H:%M')}</p>
       <p>Vendedor: {vendedor}</p>
       <hr/>
       <p>{quant_modulo:.0f}x Modulos - R${val_modulo:.2f}(UN)</p>
       <p>{quant_lixeira:.0f}x Lixeiras - R${val_lixeira:.2f}(UN)</p>
       <p>{quant_tampa:.0f}x Tampas - R${val_tampa:.2f}(UN)</p>
       <hr/>
       <p>TOTAL: R${venda_total:.2f}</p>"""

pdfkit.from_string(s, output_path = "new_file.pdf", configuration = config)

os.system(f"start chrome {output_PDF}")
