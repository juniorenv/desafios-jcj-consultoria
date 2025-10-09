function processarPedido(textoPedido) {
  const pedido = {
    cliente: null,
    itens: [],
    endereco: null,
    formaPagamento: null,
  };

  // Extrair informações simples usando Regex com captura de grupo

  // Extrai nome do cliente
  const clienteMatch = textoPedido.match(/Cliente:\s*(.*)/i);
  if (clienteMatch && clienteMatch[1]) {
    pedido.cliente = clienteMatch[1].trim();
  }

  // Extrai endereço do cliente
  const enderecoMatch = textoPedido.match(/Endereço:\s*(.*)/i);
  if (enderecoMatch && enderecoMatch[1]) {
    pedido.endereco = enderecoMatch[1].trim();
  }

  // Extrai metodo de pagamento escolhido
  const pagamentoMatch = textoPedido.match(/Pagamento:\s*(.*)/i);
  if (pagamentoMatch && pagamentoMatch[1]) {
    pedido.formaPagamento = pagamentoMatch[1].trim();
  }

  const linhas = textoPedido.split('\n');
  
  for (const linha of linhas) {
    // Unicode para capturar os textos corretos
    const itemMatch = linha.trim().match(/^(\d+)\s*[xX]?\s*([\p{L}\p{N}\s-]+)\s*(?:\((.*)\))?$/u);

    if (itemMatch) {
      // itemMatch[0] é o match completo, os outros são os grupos de captura
      // itemMatch[1] match da quantidade
      // itemMatch[2] match do produto
      // itemMatch[3] match da observação

      const quantidade = parseInt(itemMatch[1], 10);
      const produto = itemMatch[2].trim();
      const observacao = itemMatch[3] ? itemMatch[3].trim() : null;

      pedido.itens.push({
        quantidade,
        produto,
        observacao,
      });
    }
  }

  return pedido;
}

// Exemplos de Uso


// Exemplo 1 - Pedido de Hamburguer
const pedido01 = `
Olá, gostaria de fazer um pedido!

Cliente: Junior Almeida

Itens:
2x Hambúrguer (sem cebola)
1x Batata Frita Media
1x Refrigerante Lata (Coca-Cola)
3 X Esfiha de frango

Endereço: Rua das Flores, 312, Bairro Centro

Pagamento: Cartão de Crédito
`;

console.log(JSON.stringify(processarPedido(pedido01), null, 2));

// Exemplo 2 - Pedido de Pizza
const pedido02 = `
Boa noite! Quero fazer um pedido para entrega
Cliente: Maria Santos
Itens:
1x Pizza Grande Calabresa (borda recheada)
2x Pizza Média Quatro Queijos
1x Refrigerante 2L (Guaraná)
3x Coca-Cola Lata
Endereço: Avenida Brasil, 1520, Apartamento 304, Jardim Primavera
Pagamento: Pix
`;

console.log(JSON.stringify(processarPedido(pedido02), null, 2));

// Exemplo 3 - Pedido de Lanchonete
const pedido03 = `
Olá! Gostaria de encomendar para retirada
Cliente: Carlos Eduardo Lima
Itens:
3x Pastel de Carne (bem passado)
2x Coxinha de Frango
1x Suco Natural de Laranja (sem açúcar)
4 X Pão de Queijo
2x Café Expresso
Endereço: Rua São Pedro, 89, Sala 12, Centro
Pagamento: Dinheiro
`;

console.log(JSON.stringify(processarPedido(pedido03), null, 2));