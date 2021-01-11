# Ejercicios 1 y 2

## Composición de contenedores usando Sail por Laravel

Me fui guiando con documentación y videos del peladonerd y si bien logré levantar algo, luego por el lado de sail fue todo más fluido.

Como el autor de Laravel indica en los [docs](https://laravel.com/docs/8.x/sail#introduction) de Sail, se trata de una ligera interfaz de línea de comando para interactuar con un entorno de desarrollo por defecto de laravel en Docker. Apenas salido de paquete, almenos hoy 10 de Enero de 2021, permite tener un stack de una app Laravel8, Redis, php8 y Mysql8!

pasos que seguí para tener un CRUD con sail 8:

- `sail mysql -u root -p` probando sail para entrar al contenedor directamente en mysql y crear la db magnus_test. probando persistencia
- `sail artisan migrate` probando sail para un comando php artisan de migración
- `sail artisan make:migration create_products_table --create=products` generando una tabla products con sail
- `sail artisan migrate` migrar products a Miliwonder
- `sail artisan make:controller ProductController --resource --model=Product` controller para product
- `sail artisan serve`

urls:

- `http://localhost/create`
- `http://localhost/show`
- `http://localhost/edit`
- `http://localhost/index`


# Ejercicio 3

Se encuentra alojado en el repo como

- `cat ./python/ejercicio3.py`

para verlo desde la raíz y usando 

- `$ sudo apt-get update`
- `$ sudo apt-get install python3.6`

En ubuntu 16 o posterior, se puede correr como 

- `python3 ./python/ejercicio3.py`

# Ejercicio 5

# Ejercicio 6

# Ejercicio 7

Disponible en la base magnus_test

![antes](https://i.imgur.com/LGeEX15.png)

```text
SET SQL_SAFE_UPDATES = 0;
UPDATE 
	magnus_test.employees mtem
INNER JOIN magnus_test.countries mtpais on mtem.country_id = mtpais.id
INNER JOIN magnus_test.continents mtco on mtpais.continent_id = mtco.id
SET 
	mtem.salary =
		REPLACE((mtem.salary*((mtco.anual_adjustment+100)/100)),'.0000','')
WHERE mtem.salary <= 5000;
SET SQL_SAFE_UPDATES = 1;
```

![despues](https://i.imgur.com/wwMRpWx.png)


# Ejercicio 4

