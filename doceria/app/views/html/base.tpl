<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ loja }} — doces artesanais sob encomenda</title>
  <meta name="description" content="Brigadeiros, beijinhos, alfajores e outros doces artesanais. Escolha seus doces e envie o pedido pelo WhatsApp.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bagel+Fat+One&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
  <header class="topo">
    <a class="marca" href="#inicio">{{ loja }}</a>
    <nav aria-label="Principal">
      <a href="#vitrine">Vitrine</a>
      <a href="#pedido">Fazer pedido</a>
    </nav>
  </header>

  <main id="inicio">
    {{!base}}
  </main>

  <footer class="rodape">
    <p>{{ loja }} · Pedidos pelo WhatsApp</p>
  </footer>

  <script src="/static/js/app.js"></script>
</body>
</html>
