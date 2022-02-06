def format_despesa_valor(obj):
    valor = '{:.2f}'.format(float(obj.valor))
    return f'R$ {valor}'
