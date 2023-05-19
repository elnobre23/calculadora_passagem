ida_volta = int(input('Digite 1 para calcular somente os custos da ida ou 2 para calcular o trajeto de ida e volta: '))
passagem = float(input('Insira o valor das passagens: '))
dias = int(input('Deseja calcular quantos dias de passagem? '))
custo = 0

if ida_volta == 1:
    custo = dias * passagem
else:
    custo = (dias * 2) * passagem
print(f'O custo para {dias} dias é de: R$ {custo:2}')
