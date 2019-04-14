from io import open
from conllu import parse_incr
from graphviz import Digraph


def gen_dep_graph(token_list):
    dot = Digraph()
    dot.attr('node', shape='none')
    dot.node('0', '-HEAD-')
    for token in token_list:
        dot.node(str(token['id']), token['form'])
    for token in token_list:
        dot.edge(str(token['head']), str(token['id']), label=token['deprel'])
    print(dot)


data_file = open('UD_English-ParTut/en_partut-ud-dev.conllu',
                 'r', encoding='utf-8')
for token_list in parse_incr(data_file):
    gen_dep_graph(token_list)
