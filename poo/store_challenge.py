#!/usr/bin/bash
from datetime import datetime
from store import Cliente, Vendedor, Compra


def main():
    cliente = Cliente('Romário Arruda', 26)
    vendedor = Vendedor('João da Silva', 30, 4000)
    
    compra1 = Compra(vendedor, datetime.now(), 512)
    compra2 = Compra(vendedor, datetime(2022, 2, 15), 256)
    
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    
    print(f'Cliente: {cliente}', '(Adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')
    
    valor_total = cliente.total_compras()
    qtd_compras = cliente.qtd_compras()
    
    print(f'Total: {valor_total} em {qtd_compras} compras')
    print(f'Ultima compra: {cliente.get_data_ultima_compra()}')



if __name__ == '__main__':
    main()