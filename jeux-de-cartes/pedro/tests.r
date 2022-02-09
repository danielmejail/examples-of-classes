## Algunos ejemplos y casos de prueba para Pedro
##

set.seed(1)
# mazo <- crearMazo(4, 13)
# # print(mazo)
# mazo <- mezclarMazo(mazo)
# # print(mazo)
# mano <- repartirCartas(mazo = mazo, cartas = 4, jugadores = 1)
# # print(mano)
# mano <- mano[1,]
# print(mano)
# robada <- 8
# mano <- cambiarUna(mano, robada)
# # print(mano)


par(mfrow = c(1,2))
num_trials <- 5000
dist_vector <- distribucion_empirica_del_valor_de_pedro_al_inicio(num_trials)
# print(dist_vector)
hist(dist_vector, breaks = seq(3,53), xlim = c(3,53))
# hist(dist_vector, breaks = seq(0,14,0.25), xlim = c(0,14))
print(distribucion_acumulada_del_valor_de_pedro_al_inicio(num_trials, x = 21))
# print(probabilidad_de_diferencia_de_pedro_al_inicio(num_trials, x0 = 21, x1 = 21))

dist_vector <- distribucion_empirica_del_valor_de_pedro_luego_de_una(num_trials)
hist(dist_vector, breaks = seq(3,53), xlim = c(3,53))
print(distribucion_acumulada_del_valor_de_pedro_luego_de_una(num_trials, x = 21))