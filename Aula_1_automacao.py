import pyautogui
import pandas
import time

pyautogui.PAUSE= 0.5

# pressionar a tecla windows do computador
pyautogui.press("win")
# digitar a palavra Chrome 
pyautogui.write("Chrome")
# abrir o navegador
pyautogui.press("enter")
time.sleep(5)
# mapeamento do campo URK usando o mapeador
pyautogui.click(x=310, y=91)
# digitar o endereço na URL mapeada
url_base = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(url_base)
# acessar a URL digitada clicando enter
pyautogui.press("enter")
# tempo de espera para carregamento de pagina
time.sleep(1)


# mapear campos do login email e senha 
time.sleep(2)
# mapeamento do campo email
pyautogui.click(x=570, y=616)
pyautogui.write("qualidade@gmail.com")
pyautogui.press("tab")
# mapeamento do campo senha 
pyautogui.click(x=536, y=746)
pyautogui.write("123456")
pyautogui.press("tab")

pyautogui.press("enter")

# retirando modal da tela
time.sleep(5)
pyautogui.click(x=1201, y=546)

# importar arquivo csv
tabela = pandas.read_csv("menos_produtos.csv")
# printar na tela o conteudo da tabela - print(tabela)
# cadastrar produtos
# mapear campos
for linha in  tabela.index:
    pyautogui.click(x=596, y=432)
    # codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

	 # marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
     # tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
	 # categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
     # preco_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

	 # custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
     # obs
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(10000)