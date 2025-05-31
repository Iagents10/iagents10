
# Resumo Técnico – Aula 7 - Agentes Autônomos

## 1. Revisão do Papel das LLMs (Large Language Models)
- LLMs são redes treinadas com grandes volumes de dados (texto, imagem, áudio, dados estruturados, etc.).
- São modelos fundacionais (Foundation Models): pré-treinados e depois adaptados via:
  - Fine-tuning
  - Prompt engineering
  - Retrieval augmented generation (RAG).
- LLMs não possuem conhecimento atualizado automaticamente; seu conhecimento é "congelado" no momento do treinamento.

## 2. Formas de melhorar o desempenho de uma LLM
- Prompt Engineering: Modificar o prompt para melhorar a qualidade das respostas.
- Fine-tuning: Especializar o modelo com novos dados, mais caro e complexo.
- Treinamento completo: Treinar um novo modelo, extremamente custoso.
- RAG (Retrieval Augmented Generation): Complementar com bases externas via embeddings e bancos vetoriais.

## 3. O que é o RAG (Retrieval Augmented Generation)
- Pega dados não presentes no treinamento original.
- Processa e transforma documentos em embeddings (vetores numéricos).
- Armazena em banco vetorial.
- Na consulta, busca os embeddings mais semelhantes, envia junto com o prompt para enriquecer o contexto da LLM.
- Cuidado: O método de embedding deve ser compatível com a LLM usada.

## 4. Conceito de Agente Autônomo
- Origem no Reinforcement Learning (Aprendizado por Reforço): agente recebe recompensas/penalidades conforme interage com o ambiente.
- Agente melhora sua performance com base nas experiências.
- Exemplo clássico: robôs de limpeza, jogos de Atari, AlphaGo.

## 5. Níveis de Agentes Baseados em LLMs

### a) Agente Simples (Reativo)
- Como o ELIZA (anos 60): regras fixas, não raciocina.

### b) Agente com LLM (Decisão de Ação)
- LLM decide qual ação tomar com base em input do usuário.
- Exemplo: robôs com interface de linguagem natural (Google).

### c) Agente com Raciocínio e Planejamento (LLM Planner)
- Decompõe problemas complexos.
- Planeja ações e executa, adaptando conforme o feedback.
- Exemplo: resolver questões matemáticas, buscas na internet, uso de ferramentas externas.

## 6. Habilidade de Raciocínio em LLMs
- Chain-of-Thought: técnica para decompor o raciocínio em etapas.
- Ferramentas Externas: permitem consultas online, execução de código (ex: Python), consultas a bancos de dados, etc.

## 7. Modelo React (Raciocinar + Agir)
- Agente planeja, executa ações, observa o resultado e ajusta o plano.
- Integra raciocínio e ferramentas externas.
- Permite maior autonomia adaptativa.

## 8. Planejamento de Agentes
- Quebra de tarefas: decompor o problema em etapas simples.
- Definição de autonomia: Copiloto, Colaborativo, Supervisionado, Autônomo.
- Seleção de LLM, ferramentas e frameworks: LangChain, N8N, CrewAI, LangFlow.
- Protocolos de comunicação: MCP (Anthropic), Hway (Google).

## 9. Adaptação dos Agentes
- Contextual: adapta-se ao contexto recebido.
- Paramétrica: adapta ações conforme os estados mudam.
- Reflexiva: aprende com a própria experiência.

## 10. Tratamento de Exceções e Monitoramento
- Prever falhas (ex: conexões, APIs, erros matemáticos).
- Implementar controle de exceções nos fluxos dos agentes.

## 11. Ferramentas e Frameworks discutidos

| Framework | Características | Desvantagens |
| --------- | --------------- | ------------- |
| Autogen (Microsoft) | Colaboração entre agentes | Complexo para projetar e depurar |
| Pydantic | Biblioteca Python | Apenas para Python |
| LangChain | Framework mais completo e complexo | Curva de aprendizado alta |
| Lama Index | Otimizado para RAG e multiagentes | Requer ajuste fino |
| N8N | Low-code (drag & drop) | Limitado em escala e capacidade |
| LangFlow | Interface visual para LangChain | Cobrança para uso em nuvem |

## 12. Questões de Custo
- Cada chamada, ferramenta e token geram custo.
- Arquiteturas complexas podem escalar mal financeiramente.
- Avaliar custo total (ferramentas, nuvem, API, LLM, etc.)

## 13. Exemplo de Projeto e Atividade Prática
- Tema de projeto.
- Justificativa de valor.
- Público-alvo.
- Cronograma preliminar.
- Pitdeck (apresentação para banca avaliadora).

## 14. Observação Geral
- Domínio técnico, bom planejamento de arquitetura, visão clara de custos e limitações práticas.

## 15. Desafio 2 (Projeto prático dos alunos)

### Entregas obrigatórias:

**Relatório técnico (PDF):**
- Nome do grupo e integrantes.
- Tema escolhido.
- Justificativa de escolha.
- Público-alvo.
- Cronograma preliminar.
- Diagramas, tabelas, gráficos adicionais.

**Pitch Deck (PPTX):**
- Apresentação de 5 minutos.

**Tema obrigatório:** Aplicações envolvendo tratamento de documentos fiscais.

**Data limite:** 11/06 às 23:59.

## 16. Orientações finais operacionais
- Seguir o formato de nome de arquivo exatamente.
- Envio por e-mail com anexo.

## 17. Resumo Visual da Arquitetura de um Agente Completo

Input usuário --> Prompt + Contexto --> Raciocínio (Chain-of-Thought) --> Consulta a base RAG (embeddings) --> Busca ferramentas (API, Web, Scripts) --> Execução das ações --> Observação dos resultados --> Ajuste de plano --> Resposta final ao usuário

## 18. Nota importante
Tema altamente promissor no mercado, porém ainda com muita expectativa irreal e hype. Exige conhecimento técnico sólido.
