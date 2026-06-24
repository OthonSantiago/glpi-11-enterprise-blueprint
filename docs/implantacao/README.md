# Guia de implantação do GLPI 11

## Opção 1 — Docker Compose

Use a imagem oficial do GLPI 11, um serviço de banco compatível, volumes persistentes e um proxy HTTPS. Fixe a versão da imagem, mantenha os dados fora do contêiner e valide a restauração antes da entrada em produção.

Sequência: preparar o host; copiar o Compose; definir parâmetros locais; iniciar os serviços; acessar a URL HTTPS; concluir o assistente; configurar tarefas automáticas, e-mail e autenticação; executar testes.

## Opção 2 — Instalação tradicional

Use uma distribuição Linux homologada, PHP e banco nas versões suportadas pela release. Baixe o pacote estável oficial, configure o servidor web para o diretório `public`, crie banco dedicado, execute o assistente e configure os serviços operacionais.

## Pós-instalação

1. Ajustar idioma, fuso horário e identidade.
2. Configurar ações automáticas.
3. Configurar envio e recebimento de e-mail.
4. Integrar autenticação corporativa.
5. Criar entidades, grupos e perfis.
6. Configurar calendários, níveis de serviço e notificações.
7. Testar formulários, regras, inventário e API.

## Operação

Mantenha cópias do banco, documentos e configuração. Teste restauração. Atualize primeiro em homologação. Monitore disponibilidade, certificado, capacidade, tarefas automáticas, notificações e integrações.
