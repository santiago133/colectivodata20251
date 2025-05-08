import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")


#ANTES DE FILTRAR COMO ANALISTAS DE DATOS DEBES CONOCER (EXPLORAR LA FUENTE PRIMARIA)
#print(dataFrameAsistencia['estado'].unique())
#print(dataFrameAsistencia['estrato'].unique())
print(dataFrameAsistencia['medio_transporte'].unique())


#FILTROS Y CONDICIONES PARA TRANSOFRMAR DATOS
#1. Reportar todos los estudiantes que asistieron
estudiantesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
print(estudiantesQueAsistieron)
#2. Reportar todos los estudiantes que faltaron
estudiantesQueNoAsistieron=dataFrameAsistencia.query('estado=="no asistio"')
print(estudiantesQueNoAsistieron)
#3. Reportar todos los estudiantes que llegaron tarde(Justificado)
estudiantesQueLlegaronTarde=dataFrameAsistencia.query('estado=="justificado"')
print(estudiantesQueLlegaronTarde)
#4. Reportar todos los estudiantes de estrato 1
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')
print(estudiantesEstratoUno)
#5. Reportar todos los estudiantes de estratos altos
estudiantesEstratoAlto=dataFrameAsistencia.query('estrato>=4')
print(estudiantesEstratoAlto)
#6. Reportar todos los estudaintes que llegan en metro
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
print(estudiantesQueUsanMetro)
#7. Reportar todos los estudaintes que llegan en bicicleta
estudiantesQueUsanBicicleta=dataFrameAsistencia.query('medio_transporte=="bicicleta"')
print(estudiantesQueUsanBicicleta)
#8. Reportar todos los estudiantes que no caminan para llegar a la u
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
print(estudiantesQueNoCaminan)
#9. Reportar todos los registros de asistencia del mes de junio
estudiantesAbril=dataFrameAsistencia.query('fecha=="2025-04-01" or fecha=="2025-04-02" or fecha=="2025-04-03" or fecha=="2025-04-04" or fecha=="2025-04-05" or fecha=="2025-04-06" or fecha=="2025-04-07" or fecha=="2025-04-08" or fecha=="2025-06-09" or fecha=="2025-04-10"')
print(estudiantesAbril)
#10. Reportar los estudaintes que faltaron y usan bus para llegar a la u
estudiantesQueFaltanUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasisten')
print(estudiantesQueFaltanUsanBus.info())
#11. Reportar estudiantes que usan bus y son de estratos altos
estudiantesQuefaltanyUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
print(estudiantesQuefaltanyUsanBus.info())
#12. Reportar estudiantes que usan bus y son de estratos bajos
estudiantesQueUsanBusEstratoBajo=dataFrameAsistencia.query('medio_transporte=="bus" and estrato<=2')
print(estudiantesQueUsanBusEstratoBajo.info())
#13. Reportar estudiantes que llegan tarde y son de estrato 3,4,5 o 6
estudiantesQueLlegaronTardeEstrato2_4_5_6=dataFrameAsistencia.query('estado=="justificado" and (estrato==2 or estrato==4 or estrato==5 or estrato==6)')
print(estudiantesQueLlegaronTardeEstrato2_4_5_6.info())
#14. Reportar estudiantes que usan transportes ecologicos 
estudiantesQueUsanTransporteEcologico=dataFrameAsistencia.query('estrato<=2 and (medio_transporte=="bicicleta" or medio_transporte=="metro" or medio_transporte=="a pie")')
print(estudiantesQueUsanTransporteEcologico.info())
#15. Reportar estudiantes que faltan y usan carro para transportarse
estudiantesQueFaltanYUsanCarro=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="carro"')
print(estudiantesQueFaltanYUsanCarro.info())
#16. Reportar estudiantes que asisten son estratos altos y caminan
estudiantesqueAsistenEstratoAltoYCaminar=dataFrameAsistencia.query('estado=="asistio" and estrato>=4 and medio_transporte=="a pie"')
print(estudiantesqueAsistenEstratoAltoYCaminar.info())
#17. Reportar estudiantes que son estratos bajos y justifican su iniasistencia
estudiantesEstratoBajoJustificanInasistencia=dataFrameAsistencia.query('estado=="justificado" and estrato<=2')
print(estudiantesEstratoBajoJustificanInasistencia.info())
#18. Reportar estudiantes que son estratos altos y justifican su iniasistencia
estudiantesEstratoAltoJustificanInasistencia=dataFrameAsistencia.query('estado=="justificado" and estrato>=4')
print(estudiantesEstratoAltoJustificanInasistencia.info())
#19. Reportar estudiantes que usan carro y justifican su inasistencia
estudiantesQueUsanCarroYJustificanInasistencia=dataFrameAsistencia.query('estado=="justificado" and medio_transporte=="carro"')
print(estudiantesQueUsanCarroYJustificanInasistencia.info())
#20. Reportar estudiantes que faltan y usan metro y son estratos medios
estudiantesQueFaltanUsanMetroEstratoMedio=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="metro" and (estrato==3 or estrato==4)')
print(estudiantesQueFaltanUsanMetroEstratoMedio.info())

#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()
print(conteoRegistrosPorEstado)
#2. Numero de registros por estrato
conteoRegistrosPorEstrato=dataFrameAsistencia.groupby('estrato').size()
print(conteoRegistrosPorEstrato)
#3. Cantidad de estudiantes por medio de transporte
conteoRegistrosPorMedioTransporte=dataFrameAsistencia.groupby('medio_transporte').size()
print(conteoRegistrosPorMedioTransporte)
#4. Cantidad de registros por grupo
conteoRegistrosPorGrupo=dataFrameAsistencia.groupby('id_grupo').size()
print(conteoRegistrosPorGrupo)
#5. Cruce entre estado y medio de transporte
cruceEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()
print(cruceEstadoMedioTransporte)
#6. Promedio de estrato por estado de asistencia
promedioEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoPorEstado)
#7. Estrato promedio por medio de transporte
promedioEstratoPorMedioTransporte=dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()
print(promedioEstratoPorMedioTransporte)
#8. Maximo estrato por estado de asistencia
maximoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].max()
print(maximoEstratoPorEstado)
#9. Minimo estrato por estado de asistencia
minimoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].min()
print(minimoEstratoPorEstado)
#10.Conteo de asistencias por grupo y por estado
conteoAsistenciaPorGrupoYEstado=dataFrameAsistencia.groupby(['id_grupo','estado']).size()
print(conteoAsistenciaPorGrupoYEstado)
#11. Transporte usado por cada grupo
transporteUsadosPorGrupo=dataFrameAsistencia.groupby(['id_grupo','medio_transporte']).size()
print(transporteUsadosPorGrupo)
#12. cuantos grupos distintos registraron asistencia por fecha
conteoGruposPorFecha=dataFrameAsistencia.groupby(['fecha','id_grupo']).size()
print(conteoGruposPorFecha)
#13. Promedio de estrato por fecha
promedioEstratoporEstado=dataFrameAsistencia.groupby('fecha')['estrato'].mean()
print(promedioEstratoporEstado)
#14. Numero de tipos de estado por transporte
numeroTipoEstadoPorTransporte=dataFrameAsistencia.groupby(['medio_transporte','estado']).size()
print(numeroTipoEstadoPorTransporte)
#15. Primer Registro de cada grupo
primerRegistroPorGrupo=dataFrameAsistencia.groupby('id_grupo').first()
print(primerRegistroPorGrupo)