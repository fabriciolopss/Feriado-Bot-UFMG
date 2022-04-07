Basicamente a proposta dessa automação do twitter é postar todos os dias, pelo menos 2x por dia, qual o feriado mais próximo
a partir do momento que o script calcula o feriado mais próximo, com base em uma lista de feriados que está em um .txt(quero
no futuro automatizar a construção desse arquivo a partir do calendário da própria UFMG), depois de calcular o feriado mais próximos
o script formula uma string com algumas informações, como o tempo que falta, os campus nos quais será, de fato feriado e etc. No futuro
vou transformar esse script em uma API, provavelmente usando Flask, mas por enquanto é isso, lembrando que qualquer contribuição ou ideia
é válida.