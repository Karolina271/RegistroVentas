import sales_analysis as sa

def main():
    # Ruta del archivo CSV con los datos de ventas
    file_path = 'C:/Users/labinf1.pasto/Documents/GitHub/RegistroVentas/sales_data.csv'

    
    # Cargar datos de ventas
    sales_data = sa.load_sales_data(file_path)
    
    # Calcular ventas mensuales
    monthly_sales = sa.calculate_monthly_sales(sales_data)
    
    # Mostrar gráfico de ventas mensuales
    sa.plot_monthly_sales(monthly_sales)

if __name__ == '__main__':
    main()
    
