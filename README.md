<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Pipeline ELT</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: auto;
            padding: 20px;
            background-color: #f6f8fa;
        }
        .container {
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        h1, h2 {
            color: #24292e;
            border-bottom: 2px solid #eaecef;
            padding-bottom: 0.3em;
            margin-top: 24px;
        }
        code {
            background-color: #f3f4f6;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
        }
        pre {
            background-color: #f3f4f6;
            padding: 1em;
            border-radius: 8px;
            overflow-x: auto;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            padding-left: 1.5em;
            text-indent: -1.5em;
        }
        ul li::before {
            content: "•";
            color: #0366d6;
            font-weight: bold;
            display: inline-block;
            width: 1.5em;
            margin-left: -1.5em;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Pipeline ELT de PostgreSQL para PostgreSQL</h1>
    <p>Esta é uma pipeline simples de <strong>Extract, Load, Transform (ELT)</strong> projetada para demonstrar a movimentação de dados de um banco de dados <strong>PostgreSQL</strong> de origem para um de destino. Ela utiliza um script Python para automatizar o processo, executando dentro de um container Docker.</p>

    <h2>Componentes</h2>
    <ul>
        <li><strong><code>source_postgres</code></strong>: Container Docker que hospeda o banco de dados de origem.</li>
        <li><strong><code>destination_postgres</code></strong>: Container Docker que serve como o banco de dados de destino.</li>
        <li><strong><code>elt_script</code></strong>: Container Docker que executa o script Python <code>elt_script.py</code>, responsável por:
            <ul>
                <li>Verificar a disponibilidade dos bancos de dados.</li>
                <li>Exportar (<code>pg_dump</code>) os dados do banco de origem.</li>
                <li>Importar (<code>psql</code>) os dados para o banco de destino.</li>
            </ul>
        </li>
    </ul>

    <h2>Como Funciona</h2>
    <p>O <code>docker-compose.yml</code> orquestra os três serviços. O <code>elt_script</code> aguarda que os bancos de dados de origem e destino estejam prontos antes de começar o processo. O script, por sua vez, utiliza as ferramentas de linha de comando nativas do PostgreSQL (<code>pg_dump</code> e <code>psql</code>) para transferir os dados.</p>

    <h2>Próximos Passos</h2>
    <p>A arquitetura atual serve como uma base sólida. As futuras melhorias podem incluir:</p>
    <ul>
        <li><strong>Transformação de Dados:</strong> Atualmente, a pipeline é um processo EL. Para fazer uma verdadeira pipeline ELT, a etapa de transformação deve ser adicionada no banco de destino, após a carga dos dados.</li>
        <li><strong>Agendamento:</strong> Integrar com ferramentas como <strong>Apache Airflow</strong> ou <strong>dbt</strong> para agendar a execução da pipeline.</li>
        <li><strong>Incremento de Dados:</strong> Implementar a lógica para transferir apenas novos ou alterados em vez de fazer um "dump" completo.</li>
        <li><strong>Monitoramento e Logs:</strong> Adicionar logs e métricas para monitorar o desempenho e detectar erros.</li>
    </ul>
</div>

</body>
</html> 
