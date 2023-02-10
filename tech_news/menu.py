# Requisitos 11 e 12
import sys


def analyzer_menu():
    sys.stdout.write(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n "
        "4 - Listar top 5 categorias;\n 5 - Sair.\n"
    )
    switcher = {
        "0": "Digite quantas notícias serão buscadas:\n",
        "1": "Digite o título:\n",
        "2": "Digite a data no formato aaaa-mm-dd:\n",
        "3": "Digite a categoria:\n",
    }
    try:
        sys.stdout.write(switcher[input()])
    except KeyError:
        sys.stderr.write("Opção inválida\n")
