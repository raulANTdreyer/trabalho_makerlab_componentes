# Trabalho Prático — Testes de Componente em um Sistema de Maker Lab

## Objetivo

Neste trabalho, vocês receberão um pequeno sistema de maker lab já implementado, contendo:

- código-fonte do subsistema;
- testes de unidade prontos;
- estrutura básica do projeto.

O trabalho de vocês será criar os **testes de componente** do sistema, utilizando `pytest`.

Os testes de componente devem verificar a colaboração real entre as classes do subsistema, cobrindo fluxos de negócio relevantes. Não é permitido transformar o trabalho em testes unitários disfarçados, nem substituir as classes internas do subsistema por mocks.

## Sistema

O sistema representa um pequeno subsistema de empréstimo de equipamentos de um maker lab.

As classes principais do projeto são:

- `ToolRepository`
- `MemberRepository`
- `CheckoutRepository`
- `QueueRepository`
- `MakerLabService`

## Regras de negócio

### Retirada de equipamento
Um membro pode retirar um equipamento somente se:

- o membro existir;
- o equipamento existir;
- o membro não estiver bloqueado;
- o membro tiver treinamento obrigatório concluído;
- o equipamento estiver disponível;
- o membro tiver menos de 2 retiradas ativas;
- o equipamento não estiver reservado para outro membro na fila.

Quando a retirada é feita com sucesso:

- o equipamento deixa de estar disponível;
- a retirada ativa é registrada;
- se o membro tinha fila para esse equipamento, sua entrada na fila deve ser removida.

### Devolução de equipamento
Ao devolver um equipamento:

- a retirada ativa correspondente deve existir;
- a retirada é encerrada;
- se não houver fila pendente para o equipamento, ele volta a ficar disponível;
- se houver fila pendente, ele continua indisponível.

### Fila de espera
Um membro pode entrar na fila de espera de um equipamento somente se:

- o membro existir;
- o equipamento existir;
- o membro não estiver bloqueado;
- o membro tiver treinamento obrigatório concluído;
- o equipamento estiver indisponível;
- o membro não tiver uma entrada duplicada na fila para o mesmo equipamento;
- o membro não for quem já está com o equipamento retirado.

A fila deve respeitar a ordem de chegada.

## Tarefa

Criem os testes de componente em:

```text
tests/components/
```

Sugestão de arquivo:

```text
tests/components/test_makerlab_component.py
```

## Quantidade esperada
Espera-se entre **10 e 12 testes de componente**.

## Cenários mínimos obrigatórios

1. retirada com sucesso;
2. retirada de equipamento inexistente;
3. retirada por membro inexistente;
4. retirada bloqueada por falta de treinamento;
5. retirada bloqueada por membro bloqueado;
6. retirada bloqueada por limite de 2 retiradas ativas;
7. entrada na fila com sucesso para equipamento indisponível;
8. tentativa de fila duplicada;
9. devolução simples sem fila pendente;
10. devolução com fila pendente, mantendo o equipamento indisponível;
11. retirada bem-sucedida por membro que tinha fila para o mesmo equipamento, removendo a fila;
12. sequência completa: retirada → fila por outro membro → devolução → tentativa de nova retirada.

## Requisitos de qualidade

Os testes devem:

- usar as classes reais do subsistema;
- refletir fluxos de negócio;
- ser legíveis e bem nomeados;
- evitar duplicação excessiva;
- ser determinísticos.

## Execução

Para executar os testes de unidade:

```bash
pytest tests/unit
```

Para executar todos os testes:

```bash
pytest
```
