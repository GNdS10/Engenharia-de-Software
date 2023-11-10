#language: pt

Funcionalidade: Teste de busca por produto no Magazine Luiza

  Cenário: O usuário deve ser capaz de buscar por um produto com sucesso
    Dado que o usuário está na página inicial do Magazine Luiza
    Quando o usuário insere "smartphone" na barra de pesquisa
    E o usuário pressiona Enter
    Então o usuário deve ver uma lista de resultados de pesquisa de "smartphone"
