import subprocess
import time
import sys

def wait_for_postgres(host, user, password, port="5432", max_retries=20, delay_seconds=5):
    retries = 0
    while retries < max_retries:
        try:
            result = subprocess.run(
                [
                    "pg_isready",
                    "-h", host,
                    "-p", port,
                    "-U", user
                ],
                env={"PGPASSWORD": password},
                capture_output=True,
                text=True
            )
            if "accepting connections" in result.stdout:
                print(f"✅ Conexão bem sucedida com {host}!")
                return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro na conexão com {host}: {e}")
        retries += 1
        print(f"⏳ Tentando novamente em {delay_seconds} segundos... (Tentativa {retries}/{max_retries})")
        time.sleep(delay_seconds)
    print(f"❌ Máximo de tentativas atingido para {host}, abortando.")
    return False


# Configurações
source_config = {
    'dbname': 'source_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'source_postgres',
    'port': '5432'
}

destination_config = {
    'dbname': 'destination_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'destination_postgres',
    'port': '5432'
}

# Espera os bancos ficarem prontos
if not wait_for_postgres(source_config['host'], source_config['user'], source_config['password']):
    sys.exit(1)

if not wait_for_postgres(destination_config['host'], destination_config['user'], destination_config['password']):
    sys.exit(1)

print("🚀 Iniciando processo de ELT...")

# Dump do banco de origem
dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-p', source_config['port'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql'
]

print("📤 Exportando dados do banco de origem...")
subprocess.run(dump_command, env={"PGPASSWORD": source_config['password']}, check=True)
print("✅ Dump concluído e salvo em data_dump.sql")

# Load no banco de destino
load_command = [
    'psql',
    '-h', destination_config['host'],
    '-p', destination_config['port'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-f', 'data_dump.sql'
]

print("📥 Carregando dados no banco de destino...")
subprocess.run(load_command, env={"PGPASSWORD": destination_config['password']}, check=True)
print("✅ Dados importados com sucesso para o banco de destino!")
