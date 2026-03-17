    """
    Gera uma tabela (pandas.DataFrame) com os feriados municipais, estaduais e nacionais
    para uma determinada localidade em um intervalo de anos.

    Parâmetros
    ----------
    pais : str
        Código do país conforme biblioteca holidays (ex: 'BR' para Brasil).
    estado : str
        Sigla da unidade federativa (ex: 'PR' para Paraná).
    cidade : str
        Nome da cidade (ex: 'Curitiba'). O valor é insensitive a maiúsculas.
    ano_inicio : int
        Primeiro ano do intervalo desejado.
    ano_fim : int
        Último ano do intervalo desejado (inclusive).

    Retorna
    -------
    pandas.DataFrame
        DataFrame contendo as colunas:
        - dt_data: data no formato YYYY-MM-DD
        - cd_ano: ano
        - tx_dia_semana: dia da semana em português
        - tx_feriado: "Sim" ou "Não"
        - tx_nome_feriado: nome do feriado ou "-"
        - tx_pais: código do país
        - tx_estado: sigla do estado
        - tx_cidade: nome da cidade
        - cd_util_5: 0 se fim de semana ou feriado, 1 caso contrário (semana 5 dias úteis)
        - cd_util_6: 0 se domingo ou feriado, 1 caso contrário (semana 6 dias úteis)
        - cd_dia_semana: número do dia da semana (2 a 7 para seg a sáb, 1 para dom)

    Exemplo
    -------
    >>> df = gerar_tabela_feriados('BR', 'PR', 'Curitiba', 2024, 2025)
    """