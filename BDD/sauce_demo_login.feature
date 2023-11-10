#language: pt

Funcionalidade: Teste de login no SauceDemo

  Cenário: O usuário deve ser capaz de fazer login com sucesso
    Dado que o usuário está na página de login do SauceDemo
    Quando o usuário insere seu nome de usuário e senha válidos
    E o usuário clica no botão "Login"
    Então o usuário deve ser redirecionado para a página principal do SauceDemo
