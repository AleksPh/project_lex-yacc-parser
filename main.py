from Parser.yacc_grammar import parser
from Parser.lex import tokens
from AST.ast_drawer import draw_ast


def main():
    index = 0
    while True:
        try:
            s = input('Enter a statement or expression: ')
        except EOFError:
            break
        if not s:
            continue
        s = s.replace(" ", "")
        index += 1
        result = parser.parse(s)
        print(result)

        graph = draw_ast(s)
        graph.render(f'Output/output_{index}', view=True)


if __name__ == '__main__':
    main()