# Evidências dos Testes e Correções — PIT II

**Aluno:** Vagner William Matos Alves Lima  
**RGM:** 33902739  
**Projeto:** Aplicativo mobile/web para loja virtual de cupcakes

## 1. Mensagem de confirmação no carrinho
**Problema identificado:** a mensagem exibida após adicionar um cupcake ao carrinho apresentava pouco destaque.

**Correção aplicada:** foram criados estilos visuais específicos para mensagens de sucesso e de erro. A confirmação passou a informar de forma clara que o produto foi adicionado com sucesso.

**Evidência:** alteração registrada no arquivo `index.html`, nas classes `msg ok` e `msg erro`.

## 2. Validação dos campos obrigatórios
**Problema identificado:** a orientação ao usuário era pouco específica quando faltavam informações necessárias para finalizar o pedido.

**Correção aplicada:** o sistema passou a verificar nome, telefone, endereço, forma de pagamento e modalidade de entrega, informando exatamente quais campos precisam ser preenchidos.

**Evidência:** lógica de validação adicionada ao evento de finalização do formulário.

## 3. Acompanhamento do pedido
**Problema identificado:** a versão inicial apresentava apenas o status “Pedido recebido”.

**Correção aplicada:** foi incluída uma sequência simplificada de etapas: Pedido recebido, Pagamento confirmado, Em preparo, Saiu para entrega e Concluído.

**Evidência:** componente de status ampliado inserido na confirmação do pedido.

## 4. Responsividade em telas menores
**Problema identificado:** alguns campos e botões ficavam muito próximos em dispositivos móveis.

**Correção aplicada:** foram ampliados os espaçamentos do formulário e as áreas de toque dos campos e botões.

**Evidência:** regras adicionais de responsividade inseridas no media query para telas de até 600 pixels.

## 5. Confirmação final do pedido
**Problema identificado:** a confirmação apresentava poucas informações sobre a finalização.

**Correção aplicada:** foi incluído um resumo com número do pedido, cliente, forma de pagamento, modalidade de entrega e sequência de status.

**Evidência:** novo bloco de confirmação adicionado ao `index.html`.

## Resultado da verificação
Após as correções, foram novamente verificados catálogo, carrinho, formulário, validações, pagamento, entrega, confirmação do pedido e responsividade. O fluxo principal apresentou funcionamento satisfatório.

## Funcionalidades previstas para evolução futura
- pagamento real integrado;
- cadastro e autenticação de usuários;
- rastreamento real da entrega;
- testes em ampla variedade de navegadores e dispositivos;
- testes de desempenho com vários usuários simultâneos.
