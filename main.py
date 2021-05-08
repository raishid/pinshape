from modulos import firefox_class
from modulos.read_excel import Read_excel

fila_inicial = 2

while True:
    datos = Read_excel.Get_data_excel(fila_inicial)
    if datos == False:
        print('No hay datos en la hoja excel')
        input("presiona Enter para continuar.")
        break
    firefox = firefox_class.Firefox_driver()
    #link = firefox.Iniciar_registro(datos['email'], datos['user'], datos['web'], datos['bio'])
    #Read_excel.Guardar_link(fila_inicial, link)
    break

print('Registrado todo exitosamente!!')

