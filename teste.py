from sql_faturamento import buscar_proposta
 
chassi = "0055403"
pedido = 513135
 
resultados_SQL = buscar_proposta(chassi=chassi, pedido=pedido)
 
if not resultados_SQL:
    print(f"Nenhum registro encontrado para o chassi {chassi} ou pedido {pedido}.")
else:
    status = resultados_SQL[0]['proposta_status']
   
    if status == 'PED':
        print(f"Proposta com status PED — pedido realizado.")
    elif status == 'FAT':
        print(f"Proposta com status FAT — já faturado.")
    else:
        print(f"Status encontrado: {status}")