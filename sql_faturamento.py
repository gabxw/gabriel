import pyodbc
 
# =========================
# Credenciais SQL
# =========================
SQL_SERVER = "10.16.33.38"
SQL_DB     = "GrupoRoma_DealernetWF"
SQL_USER   = "POWERBI3"
SQL_PASS   = "GFDCBer#erDfyHji"
 
DRIVERS = [
    "ODBC Driver 17 for SQL Server",
    "ODBC Driver 18 for SQL Server",
    "SQL Server Native Client 11.0",
    "SQL Server",
]
 
def _montar_conn_str(driver: str) -> str:
    return (
        f"DRIVER={{{driver}}};"
        f"SERVER={SQL_SERVER};DATABASE={SQL_DB};"
        f"UID={SQL_USER};PWD={SQL_PASS};"
        "TrustServerCertificate=yes;"
    )
 
def _conectar() -> pyodbc.Connection:
    for driver in DRIVERS:
        try:
            conn = pyodbc.connect(_montar_conn_str(driver), timeout=10)
            return conn
        except pyodbc.Error:
            pass
    raise ConnectionError(f"Nenhum driver ODBC funcionou. Instalados: {pyodbc.drivers()}")
 
def buscar_proposta(chassi: str = None, pedido: int = None) -> list[dict]:
    """
    Busca propostas pelo chassi primeiro. Se não encontrar, busca pelo pedido.
    """
    conn = _conectar()
    try:
        cur = conn.cursor()
 
        # 1. Tenta pelo chassi
        if chassi:
            SQL_CHASSI = """
                SELECT proposta_status, p.*, v.*
                FROM gruporoma_dealernetwf..veiculo v
                JOIN gruporoma_dealernetwf..proposta p ON p.proposta_veiculocod = v.veiculo_codigo
                WHERE v.veiculo_chassi LIKE ?
                and proposta_status != 'NEG'
                and proposta_status != 'CAN'
            """
            cur.execute(SQL_CHASSI, [f'%{chassi}%'])
            cols = [c[0] for c in cur.description]
            rows = cur.fetchall()
            if rows:
                return [dict(zip(cols, row)) for row in rows]
 
        # 2. Fallback: tenta pelo pedido
        if pedido:
            SQL_PEDIDO = """
                SELECT proposta_status, *
                FROM gruporoma_dealernetwf..proposta
                WHERE proposta_pedido = ?
                and proposta_status != 'NEG'
                and proposta_status != 'CAN'
            """
            cur.execute(SQL_PEDIDO, [pedido])
            cols = [c[0] for c in cur.description]
            rows = cur.fetchall()
            if rows:
                return [dict(zip(cols, row)) for row in rows]
 
        return []
 
    finally:
        cur.close()
        conn.close()
 
 
if __name__ == "__main__":
    chassi_teste = "9BD363APUTYT47340"
    pedido_teste = 537076
 
    resultado = buscar_proposta(chassi=chassi_teste, pedido=pedido_teste)
    if resultado:
        print(f"Sucesso! Foram retornados {len(resultado)} registros.")
        for linha in resultado:
            print(linha)
    else:
        print(f"Nenhum registro encontrado para o chassi {chassi_teste} ou pedido {pedido_teste}.")