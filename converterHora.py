def convertorDeHoras(h, m):
  if 0 < h <= 12 and 0 < m < 60:
    print(f'{h:02}:{m:02} AM')
    print('Se preferir, digite 999 para SAIR.')
  elif 12 < h < 24 and 0 < m < 60:
    print(f'{h - 12}:{m:02} PM')
    print("Hora convertida!")
    print('Se preferir, digite 999 para SAIR.')
  else:
    print('Valor inválido, digite novamente.')
    print('Se preferir, digite 999 para SAIR.')


while True:
  h = eval(input('Hora: '))
  if h == 999:
    print('Fim')
    break
  m = int(input('Minuto: '))
  convertorDeHoras(h, m)
  print('=' * 12)
