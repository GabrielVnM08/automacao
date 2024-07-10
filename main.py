import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5


#Passo 1 - Entrar no sistema da empresa.  -  Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#Passo 2 - Fazer o login.
pyautogui.click(x=571, y=405)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("Gabriel")

pyautogui.press("tab")
pyautogui.write("gabriel")

pyautogui.click(x=676, y=570)
time.sleep(3)

#Passo 3 - Pegar base de dados.
table = pandas.read_csv("produtos.csv")

#Passo 4 - Cadastrar um produto.
for line in table.index:
    pyautogui.click(x=639, y=291)
    codigo = str(table.loc[line, "codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = str(table.loc[line, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str(table.loc[line, "tipo"])
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(table.loc[line, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco = str(table.loc[line, "preco_unitario"])
    pyautogui.write(preco)

    pyautogui.press("tab")
    custo = str(table.loc[line, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(table.loc[line, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

#Rodar automação em python diariamente/semanalmente - https://www.youtube.com/watch?v=SxEjHAlCqmo&pp=ygUlcHl0aG9uIGF1dG9tYcOnw6NvIHJvZGFyIHNlbWFuYWxtZW50ZQ%3D%3D

#Rodar automação em python com Selenium(segundo plano) - https://www.youtube.com/watch?v=8AMNaVt0z_M&pp=ygUbcHl0aG9uIGF1dG9tYcOnw6NvIHNlbGVuaXVt

#Rodar automação python em arquivo executavel - https://www.youtube.com/watch?v=cGSerUmK0CE&pp=ygURcHl0aG9uIGV4ZWN1dGF2ZWw%3D