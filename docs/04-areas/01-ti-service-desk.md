# TI e Service Desk

## Catalogo inicial

- incidente de hardware ou software
- solicitacao de equipamento
- instalacao de software
- acesso ou alteracao de perfil
- rede, VPN ou Wi-Fi
- conta, grupo ou caixa compartilhada

## Fluxo

```mermaid
flowchart LR
    U["Usuario"] --> F["Portal"]
    F --> N1["Service Desk N1"]
    N1 --> D{"Resolve no N1?"}
    D -->|Sim| S["Solucao"]
    D -->|Nao| N2["Especialista"]
    N2 --> S
    S --> C["Validacao e encerramento"]
```

## Configuracao

1. Crie grupos N1, Infra, Redes, IAM, Workplace e Aplicacoes.
2. Crie formularios por servico de maior volume.
3. Defina prioridade por impacto e urgencia.
4. Configure aprovacao para privilegios, ativos e software pago.
5. Associe SLA e OLA.
6. Crie modelos de tarefa e solucao.
7. Meça FCR, MTTA, MTTR, backlog, reabertura, SLA e satisfacao.
