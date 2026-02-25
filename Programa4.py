def aumentar_dia(dia, mes, ano):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_mes[1] = 29

    dia += 1
    
    if dia > dias_mes[mes - 1]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1

    return dia, mes, ano

fecha = input("Ingresa la fecha (día/mes/año): ")
dia, mes, ano = map(int, fecha.split('/'))

d, m, a = aumentar_dia(dia, mes, ano)

print(f"El siguiente día es: {d}/{m}/{a}")