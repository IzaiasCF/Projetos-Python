@echo off
:: Caminho at� sua pasta local do reposit�rio
cd /d "C:\Users\IzaiasCF\Documents\Projetos\Projetos-Python"

:: Mensagem de commit padr�o (voc� pode editar)
set /p msg="Digite a mensagem do commit: "

:: Executa os comandos Git
git add .
git commit -m "%msg%"
git push origin main

pause