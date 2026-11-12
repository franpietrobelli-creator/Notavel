aprovado_por_frequencia = freq >= 0.5 or freq >= 0.5 
aprovado_por_nota = nota_prevista >= 7.0 or nota_prevista >= 7.0

if aprovado_por_frequencia and aprovado_por_nota:
    print('O aluno foi aprovado')
else:
    print(f'O aluno reprovará por frequencia {freq * 100}%') or print(f'O aluno reprovará por nota {nota_prevista[0]:.2f}')
    if not aprovado_por_frequencia and not aprovado_por_nota:
        print(f'O aluno reprovará por nota {nota_prevista[0]:.2f} e frequencia {freq * 100}%')