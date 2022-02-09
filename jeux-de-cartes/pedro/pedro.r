## Algunas funciones b\'asicas para Pedro
##

crearMazo <- function(palos = 0, rangos = 0) {
  mazo <- vector()

  for (i in seq(1,palos)){
    mazo <- append(mazo, seq(1,rangos))
  }
  return(mazo)
}

mezclarMazo <- function(mazo = vector())
{
  # return(repartirCartas(mazo, length(mazo)))
  return(sample(mazo, length(mazo), replace = FALSE))
}

repartirCartas <- function(mazo = vector(), cartas = 0, jugadores = 0)
{
  # copia <- mazo[]
  # mano <- sample(mazo, cartas, replace = FALSE)
  # asume que el mazo est\'a mezclado; reparte cartas a jugadores
  # crea una matriz de jugadores por cartas en que cada fila representa la mano de un jugador
  if ( jugadores == 0 )
  {
    return(vector())
  }
  mano <- matrix(data = 0, nrow = jugadores, ncol = cartas)
  if ( cartas > 0 )
  {
    jugador <- 1
    while ( jugador <= jugadores )
    {
      # print(c("jugador: ",jugador), quote = FALSE)
      # print(mano[jugador,])
      mano[jugador,] <- mazo[seq((jugador-1) * cartas + 1, (jugador * cartas))]
      # print(mano[jugador,])
      jugador <- jugador + 1
    }
  }
  return(mano)
}

sumarCartas <- function(cartas)
{
  return(sum(cartas))
}

masAlta <- function(mano)
  # devuelve el \'indice de la carta m\'as alta
{
  i <- 1
  for ( j in seq(1,length(mano)) )
  {
    if ( mano[j] > mano[i] )
    {
      i <- j
    }
  }
  return(i)
}

cambiarUna <- function(mano, robada)
  # devuelve una nueva mano intercambiando la carta m\'as alta por la robada
  # (si \'esta es menor)
{
  ind_de_alta <- masAlta(mano)
  if ( mano[ind_de_alta] > robada )
  {
    mano[ind_de_alta] <- robada
  }
  return(mano)
}