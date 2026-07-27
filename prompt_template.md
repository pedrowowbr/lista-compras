# Tarefa

Analise a imagem da nota fiscal e extraia todos os produtos.

## Regras

Para cada produto extraia:

- **dt_compra**: data da compra no formato YYYY-MM-DD.
- **produto**: apenas o nome do produto, removendo marca, tamanho, peso, volume, quantidade e outras descrições.
- **valor_produto**:
  - se o item foi comprado em unidade, informe o valor unitário;
  - se o item foi vendido por peso (kg ou g), informe o valor total pago pelo item.

## Produtos conhecidos

{produtos}

Caso encontre um produto equivalente a um da lista acima, utilize exatamente o mesmo nome.

## Formato da resposta

Retorne **apenas** um JSON válido.

Utilize **exatamente** estas chaves:

- dt_compra
- produto
- valor_produto

O formato deve ser exatamente:

{resposta}