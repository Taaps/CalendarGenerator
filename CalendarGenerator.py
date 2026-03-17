#%%
def gerar_calendario_completo(pais: str, estado: str, cidade: str, ano_inicio: int, ano_fim: int):
    import pandas as pd
    import holidays
    from datetime import date


    dias_pt = {
        'Monday': 'Segunda-feira', 'Tuesday': 'Terça-feira', 
        'Wednesday': 'Quarta-feira', 'Thursday': 'Quinta-feira', 
        'Friday': 'Sexta-feira', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
    }

    try:
        # 1. Pegamos os feriados oficiais do país/estado
        feriados_obj = holidays.BR(subdiv=estado, years=range(ano_inicio, ano_fim + 1))
        
        # 2. Adicionamos o feriado municipal de Curitiba manualmente
        if cidade.lower() == "curitiba":
            for ano in range(ano_inicio, ano_fim + 1):
                feriados_obj.append({date(ano, 9, 8): "Nossa Senhora da Luz dos Pinhais (Padroeira)"})

        # 3. Criamos um intervalo de datas completo (de 01/01/AnoInicio até 31/12/AnoFim)
        data_inicial = f"{ano_inicio}-01-01"
        data_final = f"{ano_fim}-12-31"
        datas = pd.date_range(start=data_inicial, end=data_final)

        lista_dias = []

        # 4. Iteramos sobre TODOS os dias do intervalo
        for data in datas:
            # Convertemos a data do pandas para o objeto date do python para comparar
            data_date = data.to_pydatetime().date()
            
            # Verificamos se esse dia está no objeto de feriados
            nome_feriado = feriados_obj.get(data_date) 
            eh_feriado = "Sim" if nome_feriado else "Não"

            lista_dias.append({
                "dt_data": data.strftime('%Y-%m-%d'),
                "cd_ano": data.year,
                "tx_dia_semana": dias_pt[data.strftime('%A')],
                "tx_feriado": eh_feriado,
                "tx_nome_feriado": nome_feriado if nome_feriado else "-",
                "tx_pais": pais,
                "tx_estado": estado,
                "tx_cidade": cidade,
            })

        df = pd.DataFrame(lista_dias)
        df['cd_util_5'] = np.where((df.tx_dia_semana == 'Domingo') | (df.tx_dia_semana == 'Sábado') | (df.tx_feriado == 'Sim'),0,1)
        df['cd_util_6'] = np.where((df.tx_dia_semana == 'Domingo') |  (df.tx_feriado == 'Sim'),0,1)
        df['dt_data'] = pd.to_datetime(df['dt_data'])
        df['cd_dia_semana'] = df.dt_data.dt.dayofweek + 2
        df['cd_dia_semana'] = np.where(df.cd_dia_semana == 8, 1, df.cd_dia_semana)


        print(f"✨ Sucesso! Calendário gerado com {len(df)} dias no total.")
        return df

    except Exception as e:
        print(f"❌ Erro ao gerar calendário: {e}")
        return None
#%%
# Execução
df_resultado = gerar_calendario_completo(pais='BR', estado='PR', cidade='Curitiba', ano_inicio=2024, ano_fim=2025)

# Visualizando as primeiras linhas
print(df_resultado.head(15))

# Se quiser salvar para Excel:
# df_resultado.to_excel("calendario_completo.xlsx", index=False)