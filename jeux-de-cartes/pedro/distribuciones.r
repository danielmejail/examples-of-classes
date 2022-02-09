## Algunas distribuciones y probabilidades relacionadas con Pedro
##

distribucion_empirica_del_valor_de_pedro_al_inicio <- function(num_trials)
{
  j <- 0
  dist_vector <- vector()
  while ( j < num_trials )
  {
    palos = 4
    rangos = 13
    jugadores = 1
    cartas = 4
    mazo <- mezclarMazo(crearMazo(palos, rangos))
    mano <- repartirCartas(mazo = mazo, cartas = cartas, jugadores = jugadores)
    suma <- sumarCartas(mano[1,])
    dist_vector <- c(dist_vector, suma)
    j <- j + 1
  }
  return(dist_vector)
}

distribucion_acumulada_del_valor_de_pedro_al_inicio <- function(num_trials, x)
  # determina la probabilidad de que el valor total de las cuatro cartas al inicio sea
  # menor que x
{
  palos = 4
  rangos = 13
  jugadores = 1
  cartas = 4
  
  casos_favorables <- 0
  j <- 0
  dist_vector <- vector()
  while ( j < num_trials )
  {
    mazo <- mezclarMazo(crearMazo(palos, rangos))
    mano <- repartirCartas(mazo = mazo, cartas = cartas, jugadores = jugadores)
    suma <- sumarCartas(mano[1,])
    if ( suma < x ){
      casos_favorables <- casos_favorables + 1
    }
    j <- j + 1
  }
  return(casos_favorables / num_trials)
}

probabilidad_de_diferencia_de_pedro_al_inicio <- function(num_trials, x0, x1)
  # determina la probabilidad de que el valor total de las cuatro cartas del primer jugador
  # al inicio sea menor que x0 y que el de las cuatro cartas del segundo jugador al inicio
  # sea mayor o igual a x1
{
  palos = 4
  rangos = 13
  jugadores = 2
  cartas = 4
  
  casos_favorables <- 0
  j <- 0
  dist_vector <- vector()
  while ( j < num_trials )
  {
    mazo <- mezclarMazo(crearMazo(palos, rangos))
    mano <- repartirCartas(mazo = mazo, cartas = cartas, jugadores = jugadores)
    suma1 <- sumarCartas(mano[1,])
    suma2 <- sumarCartas(mano[2,])
    if ( (suma1 < x0) & (suma2 >= x1) ){
      casos_favorables <- casos_favorables + 1
    }
    j <- j + 1
  }
  return(casos_favorables / num_trials)
}

distribucion_empirica_del_valor_de_pedro_luego_de_una <- function(num_trials)
{
  j <- 0
  dist_vector <- vector()
  while ( j < num_trials )
  {
    palos = 4
    rangos = 13
    jugadores = 1
    cartas = 4
    mazo <- mezclarMazo(crearMazo(palos, rangos))
    mano <- repartirCartas(mazo = mazo, cartas = cartas, jugadores = jugadores)
    robada <- mazo[jugadores * cartas + 1]
    mano <- cambiarUna(mano, robada)
    suma <- sumarCartas(mano[1,])
    dist_vector <- c(dist_vector, suma)
    j <- j + 1
  }
  return(dist_vector)
}

distribucion_acumulada_del_valor_de_pedro_luego_de_una <- function(num_trials, x)
  # determina la probabilidad de que el valor total de las cuatro cartas al inicio sea
  # menor que x
{
  palos = 4
  rangos = 13
  jugadores = 1
  cartas = 4
  
  casos_favorables <- 0
  j <- 0
  dist_vector <- vector()
  while ( j < num_trials )
  {
    mazo <- mezclarMazo(crearMazo(palos, rangos))
    mano <- repartirCartas(mazo = mazo, cartas = cartas, jugadores = jugadores)
    robada <- mazo[jugadores * cartas + 1]
    mano <- cambiarUna(mano, robada)
    suma <- sumarCartas(mano[1,])
    if ( suma < x ){
      casos_favorables <- casos_favorables + 1
    }
    j <- j + 1
  }
  return(casos_favorables / num_trials)
}