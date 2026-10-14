def week_day(dia):
    dias_semana = {1: "Lunes",
               2: "Martes",
               3: "Miércoles",
               4: "Jueves",
               5: "Viernes",
               6: "Sábado",
               7: "Domingo"}
    if dia in dias_semana:
        return dias_semana[dia]
    else:
        return "Día erróneo"