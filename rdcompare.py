"""
Compartilhamento de dados, procurar pelo email achar em outro base de dados o mesmo cliente e
verificar se o mesmo tem outros atributos caso tenha pegar estes dados e colocar no cliente que fez
a requisiçao.
"""


def list_compare(d1, d2):
    if d1 == {} or d2 == {}:
        return 'Email vazio'
    return organize(d1, d2)


def organize(d1, d2):
    """
    Retorna a diferença entre os dois dicionario.
    Acdiciona no dicionario que nao tem esse paramentro, retorna em uma lista de tuplas
    [('chave', 'valor'), ('chave', 'valor'), ...]
    """
    # print('d1: %s d2: %s' % (len(d1), len(d2)))
    differ = set(d1.items()) ^ set(d2.items())
    dic = dict(differ)
    # print(dic)
    for v in dic:
        d1[v] = dic[v]
    orderby = list(d1.items())
    orderby.sort()
    # print(orderby)
    return orderby


assert list_compare({},
                    dict(name='Danilo Rodrigues', email='danilo.roddrigues@gmail.com', )) == 'Email vazio'

assert list_compare(dict(name='Danilo Rodrigues', email='danilo.roddrigues@gmail.com', ),
                    dict(name='Danilo Rodrigues', email='danilo.roddrigues@gmail.com', phone='6292720466', )) == [
           ('email', 'danilo.roddrigues@gmail.com'),
           ('name', 'Danilo Rodrigues'), ('phone', '6292720466')]

assert list_compare(dict(name='Danilo Rodrigues', email='danilo.roddrigues@gmail.com', ),
                    dict(name='Danilo Rodrigues', email='danilo.roddrigues@gmail.com', empresa='Jovem Pan', )) == [
           ('email', 'danilo.roddrigues@gmail.com'),
           ('empresa', 'Jovem Pan'), ('name', 'Danilo Rodrigues')]

assert list_compare(dict(name='Danilo Rodrigues', email='danilo.roddrigues@gmail.com', phone='6292720466', ),
                    dict(name='Danilo Rodrigues', email='danilo.roddrigues@gmail.com', empresa='Jovem Pan', )) == [
           ('email', 'danilo.roddrigues@gmail.com'),
           ('empresa', 'Jovem Pan'), ('name', 'Danilo Rodrigues'),
           ('phone', '6292720466')]
