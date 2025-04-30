import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")


#ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
#print(dataFrameAsistencia['estado'].unique())
#print(dataFrameAsistencia['estrato'].unique())
print(dataFrameAsistencia['medio_transporte'].unique())


#FILTROS Y CONDICIONES PARA TRANSOFRMAR DATOS
#1. Reportar todos los estudiantes que asistieron
estudiantesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
#2. Reportar todos los estudiantes que faltaron
#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
#4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')
#5. Reportar todos los estudiantes de estratos altos
#6. Reportar todos los estudaintes que llegan en metro
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
#7. Reportar todos los estudaintes que llegan en bicicleta
#8. Reportar todos los estudiantes que no caminan para llegar a la u
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
#9. Reportar todos los registros de asistencia del mes de junio
#10. Reportar los estudaintes que faltaron y usan bus para llegar a la u
estudiantesQueFaltanUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
#11. Reportar estudiantes que usan bus y son de estratos altos
#12. Reportar estudiantes que usan bus y son de estratos bajos
#13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6
#14. Reportar estudiantes que usan transportes ecologicos 
#15. Reportar estudiantes que faltan y usan carro para transportarse
#16. Reportar estudiantes que asisten son estratos altos y caminan
#17. Reportar estudiantes que son estratos bajos y justifican su iniasistencia
#18. Reportar estudiantes que son estratos altos y justifican su iniasistencia
#19. Reportar estudiantes que usan carro y justifican su inasistencia
#20. Reportar estudiantes que faltan y usan metro y son estratos medios


#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()

#2. Numero de registros por estrato
conteoRegistrosPorEstrato=dataFrameAsistencia.groupby('estrato').size()

#3. Cantidad de estudiantes por medio de transporte
#4. Cantidad de registros por grupo
#5. Cruce entre estado y medio de transporte
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()


#6. Promedio de estrato por estado de asistencia
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoPorEstado)

#7. Estrato promedio por medio de transporte
#8. Maximo estrato por estado de asistencia
#9. Minimo estrato por estado de asistencia
#10.Conteo de asistencias por grupo y por estado
#11. Transporte usado por cada grupo
#12. cuantos grupos distintos registraron asistencia por fecha
#13. Promedio de estrato por fecha
#14. Numero de tipos de estado por transporte
#15. Primer Registro de cada grupo
