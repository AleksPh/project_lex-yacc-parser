from graphviz import Digraph
from AST.ast_nodes import *
from AST.new_parser import new_parser

def draw_ast(node, graph=None):
    if graph is None:
        node = new_parser.parse(node)
        graph = Digraph()

    if isinstance(node, BinOpNode):
        graph.node(str(id(node)), label=node.operator)
        graph.edge(str(id(node)), str(id(node.left)))
        draw_ast(node.left, graph)
        graph.edge(str(id(node)), str(id(node.right)))
        draw_ast(node.right, graph)
    elif isinstance(node, NumNode):
        graph.node(str(id(node)), label=str(node.value))
    elif isinstance(node, VarNode):
        graph.node(str(id(node)), label=node.name)

    return graph