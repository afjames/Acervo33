
# Política de Segurança e Hardening - Acervo33

Este documento detalha as decisões de segurança da informação implementadas no **Acervo33**, alinhadas ao conceito de **Defesa em Profundidade (Defense in Depth)**.

## 🛡️ Controles de Defesa (Blue Team)

### 1. Gestão de Segredos e Credenciais
* **Variáveis de Ambiente:** Nenhuma credencial de conexão é inserida diretamente no código-fonte. O gerenciamento é feito via arquivo `.env`.
* **Prevenção de Vazamento:** O arquivo `.env` está explicitamente ignorado no `.gitignore` para evitar vazamentos acidentais (*Credential Leaks*) em sistemas de controle de versão.

### 2. Princípio do Menor Privilégio (PoLP)
* **Acesso Restrito ao Banco:** A aplicação web utiliza um usuário dedicado no MySQL com permissões estritas para manipulação de dados (DML: `SELECT`, `INSERT`, `UPDATE`, `DELETE`), sem privilégios de alteração de estrutura (DDL) ou acesso de `root`.
* **Contenção de Danos (Blast Radius):** Na hipótese de comprometimento da aplicação web, o impacto fica contido ao schema `acervo33_db`, impedindo a execução de comandos destrutivos no servidor MySQL.

### 3. Hardening na Camada de Dados (Database-First)
* **Prevenção de Encoding Bypasses:** O uso de `utf8mb4` previne falhas de sanitização decorrentes de caracteres especiais ou truncamento de strings.
* **Validação por Listas Brancas (Allowlist):** Restrições `CHECK` garantem que apenas formatos pré-aprovados (`Vinil`, `CD`, `FitaK7`) e notas dentro do intervalo legal (0 a 10) entrem na base.
* **Integridade Referencial:** Chaves Estrangeiras configuradas com `ON DELETE RESTRICT` impedem a criação de registros órfãos ou exclusões acidentais em cascata.

## 🔴 Mapeamento de Ameaças (Red Team vs Blue Team)

* **Ameaça:** Extração do arquivo `.env` por leitura indevida de arquivos (LFI).
  * *Defesa:* O atacante obtém apenas um usuário de menor privilégio, incapaz de comprometer a infraestrutura do sistema operacional ou de outros bancos.
* **Ameaça:** Injeção de dados maliciosos contornando validações do Front-End / Flask.
  * *Defesa:* As regras de tipagem estrita e constraints `CHECK` do MySQL funcionam como firewall de última camada, abortando a transação.