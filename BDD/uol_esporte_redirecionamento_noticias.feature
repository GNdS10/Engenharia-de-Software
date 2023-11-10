#language: pt

Funcionalidade: Verificar redirecionamento de notícias no UOL Esporte

  Cenário: Ao clicar em uma notícia, o usuário deve ser redirecionado para outra página com a mesma manchete
    Dado que o usuário está na página inicial do UOL Esporte
    Quando o usuário clica em uma notícia
    Então o usuário deve ser redirecionado para uma página com a mesma manchete