# 🚀 Pipeline ELT: PostgreSQL para PostgreSQL

Esta é uma pipeline simples de **Extract, Load, Transform (ELT)**, projetada para demonstrar a movimentação de dados de um banco de dados **PostgreSQL** de origem para um de destino.

O processo utiliza um script Python para automatizar a extração e carga, tudo orquestrado dentro de um ambiente Docker.

---

### 📦 Componentes da Pipeline

A pipeline é composta por três serviços principais, definidos no arquivo `docker-compose.yml`:

- **`source_postgres`**: O banco de dados de origem. É de onde os dados serão extraídos.
- **`destination_postgres`**: O banco de dados de destino. É para onde os dados serão carregados.
- **`elt_script`**: O container que executa o script Python `elt_script.py`. Ele é responsável por:
    - ✅ Verificar se ambos os bancos de dados estão prontos para conexões.
    - 📤 Exportar (usando `pg_dump`) os dados do banco de origem.
    - 📥 Importar (usando `psql`) os dados para o banco de destino.

---

### ⚙️ Como Funciona

O `docker-compose.yml` garante que os serviços do PostgreSQL subam e que o script da pipeline só comece a rodar depois que eles estiverem prontos.

O script `elt_script.py` usa as ferramentas de linha de comando nativas do PostgreSQL (`pg_dump` e `psql`) para transferir os dados de forma eficiente, criando um dump intermediário em formato `.sql`.

---

### 💡 Próximos Passos e Oportunidades de Melhoria

Esta arquitetura serve como uma base sólida. Para evoluir a pipeline, considere as seguintes melhorias:

- **Transformação de Dados**: Adicione uma etapa de transformação no banco de destino para realizar a limpeza, agregação ou enriquecimento dos dados. Ferramentas como o **dbt** (Data Build Tool) são ideais para isso.
- **Agendamento**: Use orquestradores como o **Apache Airflow** para agendar a execução da pipeline de forma automática e confiável.
- **Incrementalidade**: Em vez de fazer um "dump" completo toda vez, implemente uma lógica para transferir apenas os dados novos ou alterados.
- **Observabilidade**: Adicione logs, alertas e métricas para monitorar o desempenho e detectar possíveis erros.
