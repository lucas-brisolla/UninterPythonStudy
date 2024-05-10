validaInt()

# programa
arquivo = "game.txt"
if arquivoExiste(arquivo):
    print("O arquivo está armazenado no computador.")
else:
    print("O arquivo não existe. ")

while True:
    menu = ("MENU \n 1 - Cadastrar novo item\n 2 - Listar cadastros\n 3 - SAIR\n /:")
    val = validaInt(menu, 1, 3)
    if menu == 1:
        cadastrarArquivo(arquivo, nomeJogo, nomeConsole)
