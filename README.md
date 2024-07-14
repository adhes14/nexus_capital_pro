# Iniciar el proyecto

Para setear el ambiente de desarrollo primera vez (linux):
```sh
git clone https://github.com/adhes14/nexus_capital_pro.git
cd nexus_capital_pro
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Despues de instalar una nueva dependencia correr el siguiente comando:
```sh
pip3 freeze > requirements.txt
```

Para correr el proyecto:
```sh
python manage.py runserver
```

# Antecedentes

La empresa Nexus Capital Pro se dedica a la gestión de fondos de inversión y busca modernizar y automatizar sus operaciones mediante el desarrollo de un sistema web basado en Django. Este sistema permitirá una gestión eficiente de los activos, la valoración de fondos, y brindará a los clientes acceso a información actualizada sobre sus inversiones. Se espera que el sistema mejore la transparencia y la precisión en la gestión de los fondos, así como la experiencia del usuario tanto para administradores como para clientes.

El sistema deberá gestionar múltiples tipos de activos como acciones, ETFs y criptomonedas, tomando en cuenta las particularidades de cada mercado. Además, permitirá registrar los ingresos y retiros de fondos de los clientes, y calcular automáticamente el valor de las cuotas de los fondos en función de la variación de los precios de los activos.

# Requisitos

## Requisitos Generales

1. Utilizar Django como framework principal para el desarrollo del sistema.
2. Utilizar PostgreSQL como base de datos.
3. Gestionar múltiples fondos de inversión simultáneamente.

## Requisitos Funcionales

### [Must Have]
1. El sistema debe soportar dos tipos de usuarios: administradores y clientes.
2. Los administradores deben poder registrar compras y ventas de activos (acciones, ETFs, criptomonedas).
3. Los clientes deben poder consultar el estado de su inversión.
4. Los activos deben poder clasificarse según su tipo y características de mercado.
5. El sistema debe calcular automáticamente el valor de la cuota de un fondo al cierre de cada día.
6. Los clientes solo pueden comprar cuotas de los fondos disponibles.
7. Integración con servicios REST para obtener precios de activos en tiempo real.
8. Registrar comisiones por operación y administración de fondos.
9. Registrar ingresos y retiros de fondos por parte de los clientes.
10. Permitir a los clientes comprar cuotas de los fondos y registrar la evolución del valor de sus inversiones.
11. Los fondos deben manejar la liquidez en función de las inversiones de los clientes y las transacciones de compra y venta de activos.
12. Mantener un historial de precios de los activos.
13. Registrar las posiciones de los fondos en diferentes activos.
14. Mantener un historial del valor de las cuotas, la liquidez y la cartera de cada fondo.
15. Registrar los movimientos de efectivo de los clientes en una entidad Billetera.

### [Should Have]
1. Interfaz de usuario intuitiva y fácil de usar.
2. Notificaciones automáticas para los usuarios sobre cambios importantes.

### [Could Have]
1. Análisis gráfico del rendimiento de los fondos.
2. Reportes detallados descargables para administradores y clientes.

### [Won't Have]
1. Funcionalidades de trading en tiempo real directamente en el sistema.
