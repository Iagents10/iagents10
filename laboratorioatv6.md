**Relatorio laboratorio Seabra**

# Lab 1

CENÁRIO
Uma equipe de pesquisadores está desenvolvendo um estudo sobre o uso de agentes de IA autônomos em ambientes corporativos, buscando entender como diferentes arquiteturas (baseadas em LLMs) afetam a tomada de decisão, coordenação de tarefas e confiabilidade em processos críticos. Eles precisam de resumos analíticos que ajudem a mapear as principais abordagens, frameworks existentes e limitações atuais para alimentar um artigo científico.

DESAFIO
Crie um prompt estruturado para solicitar que a IA resuma as principais arquiteturas de agentes autônomos, destacando exemplos práticos, vantagens, desafios e aplicações em ambientes corporativos.

Prompt Estruturado:

Você é um analista especializado em Inteligência Artificial aplicada a ambientes corporativos. Preciso que elabore um resumo analítico e técnico sobre as principais arquiteturas de agentes autônomos baseados em LLMs (Large Language Models), com foco na sua aplicação em contextos empresariais.
ra
O conteúdo deve abordar, de forma clara e organizada, os seguintes pontos:

1.Principais Arquiteturas: Descreva as arquiteturas mais relevantes de agentes autônomos baseados em LLMs, como ReAct, AutoGPT, BabyAGI, CAMEL, etc.

2.Exemplos Práticos: Cite casos de uso reais ou simulados dessas arquiteturas em ambientes corporativos (ex: automação de processos, análise de dados, suporte a decisões, workflows).

3.Vantagens: Aponte os principais benefícios dessas abordagens para empresas (ex: escalabilidade, adaptabilidade, redução de custos operacionais).

4.Desafios e Limitações: Analise as limitações técnicas e éticas atuais, como confiabilidade, alucinação, segurança, accountability e necessidade de supervisão humana.

5.Frameworks e Ferramentas: Mencione frameworks e ferramentas que facilitam a criação e gestão desses agentes (ex: LangChain, CrewAI, AgentOS, Microsoft AutoGen).

6.Recomendações e Perspectivas Futuras: Forneça insights sobre tendências e caminhos promissores para a evolução desses agentes em ambientes corporativos.

Estruture o conteúdo com subtítulos claros e utilize linguagem técnica, mas acessível para pesquisadores da área. O objetivo é compor a base teórica de um artigo científico.

**Conteudo gerado (chatGPT):**

Claro! Aqui está o **resumo analítico estruturado** com base no prompt:

---

## **Arquiteturas de Agentes Autônomos Baseadas em LLMs para Ambientes Corporativos**

### 1. Principais Arquiteturas

#### **ReAct (Reasoning + Acting)**

Desenvolvido pela equipe da DeepMind, o ReAct combina raciocínio passo a passo com a execução de ações no ambiente. É ideal para tarefas complexas que exigem planejamento dinâmico.

#### **AutoGPT**

AutoGPT é um agente autônomo que opera de forma iterativa para atingir objetivos definidos pelo usuário. Ele divide metas em subtarefas e utiliza ferramentas externas (como APIs, buscadores, etc.) de maneira autônoma.

#### **BabyAGI**

Uma abordagem minimalista baseada em GTD (Getting Things Done), que foca em geração, priorização e execução de tarefas. Usa LLMs para cada etapa, formando um loop contínuo de melhoria.

#### **CAMEL (Communicative Agents for Mind Exploration of Large-scale language models)**

Baseia-se em múltiplos agentes especializados que interagem entre si com papéis distintos (como CEO, desenvolvedor, analista). Ideal para simulações colaborativas e brainstorming autônomo.

#### **CrewAI**

Um framework recente que permite criar equipes de agentes com papéis distintos, coordenados por um líder. Focado em workflows corporativos estruturados.

---

### 2. Exemplos Práticos em Ambientes Corporativos

* **AutoGPT em Finanças**: Automatiza a geração de relatórios de performance, cruzando dados de múltiplas fontes e sugerindo ações baseadas em tendências.
* **ReAct em Help Desks**: Usado para atendimento automatizado, com capacidade de raciocínio antes de acionar sistemas internos ou sugerir soluções.
* **CAMEL em I\&D (Pesquisa e Desenvolvimento)**: Simula equipes interdisciplinares para explorar soluções a problemas técnicos complexos.
* **CrewAI em Gestão de Projetos**: Coordena agentes especialistas (planejamento, execução, monitoramento) para gerenciar fluxos de trabalho colaborativos.

---

### 3. Vantagens

* **Autonomia e Proatividade**: Capacidade de agir sem intervenção humana direta.
* **Escalabilidade**: Fácil replicação de agentes para múltiplas áreas.
* **Integração com Sistemas Corporativos**: Utilização de APIs, CRMs, ERPs.
* **Redução de Custos**: Diminuição de esforço humano em tarefas repetitivas.
* **Tomada de Decisão Baseada em Dados**: Acesso e análise em tempo real de grandes volumes de informações.

---

### 4. Desafios e Limitações

* **Confiabilidade**: Agentes ainda cometem erros e "alucinam" respostas incorretas.
* **Segurança e Privacidade**: Riscos em manipulação de dados sensíveis sem supervisão adequada.
* **Accountability**: Difícil rastrear decisões automatizadas em ambientes críticos.
* **Sobrecarga Computacional**: Processos contínuos demandam infraestrutura robusta.
* **Supervisão Humana Necessária**: Principalmente em tarefas de alto impacto.

---

### 5. Frameworks e Ferramentas

* **LangChain**: Permite orquestrar LLMs, memória, ferramentas e agentes em pipelines.
* **CrewAI**: Gerencia equipes de agentes com papéis colaborativos.
* **AutoGen (Microsoft)**: Facilita a criação de múltiplos agentes interativos.
* **AgentOS**: Plataforma para criação, implantação e gerenciamento de agentes em larga escala.
* **OpenAgents**: Infraestrutura aberta para experimentação com agentes multi-LMs.

---

### 6. Recomendações e Perspectivas Futuras

* **Human-in-the-loop (HITL)**: Manter o fator humano em decisões críticas continua essencial.
* **Especialização de Agentes**: Divisão por domínios técnicos melhora a performance.
* **Auditoria de Processos**: Ferramentas de rastreamento e explicabilidade serão fundamentais.
* **Interoperabilidade**: Agentes deverão interagir com diversos sistemas legados.
* **IA Autônoma Ética**: Questões como viés, discriminação algorítmica e transparência precisam ser endereçadas com seriedade.

---
# Lab 2

CENÁRIO
Você atua como analista de dados em um centro de inteligência financeira. Precisa construir
um prompt que utilize a capacidade de mecanismo de busca dos LLMs conectados à internet para
visitar a página https://www.globo.com/ e trazer no máximo 5 notícias relevantes sobre
economia, com foco no impacto para o Brasil ou para o cenário internacional.
DESAFIO
Utilizando as técnicas de engenharia de prompt avançada, crie um comando que:
Busque notícias atuais relacionadas à política brasileira ou internacional no documento apensado
extraído do site da Globo, obtido no portal https://www.globo.com/.
Limite-se a no máximo 5 notícias.
Para cada notícia encontrada: Identifique se é nacional ou internacional, analise o sentimento da
notícia (positivo ou negativo) e apresente as informações no formato estruturado abaixo.
[ Título da Notícia ]
Tipo de Notícia : [Nacional ou Internacional]
Análise de sentimento da notícia : [Boa notícia para o país ou Péssima notícia para o país]

### Prompt gerado:

Aqui está um prompt avançado de engenharia de instruções, ideal para ser usado com LLMs conectados à internet (como agentes com acesso ao web tool) em um contexto de análise de inteligência financeira. Esse prompt estrutura de forma precisa o que o modelo deve buscar, como deve interpretar e como deve apresentar os resultados:

PROMPT AVANÇADO PARA AGENTE LLM COM ACESSO À INTERNET

Você atua como analista de dados de um centro de inteligência financeira. Acesse o site https://www.globo.com/ e identifique no máximo 5 notícias atuais sobre economia, com foco no impacto para o Brasil ou para o cenário internacional.
A partir das notícias encontradas, faça o seguinte:
    1. Classifique cada notícia como Nacional (se trata de economia brasileira) ou Internacional (se trata de economia mundial que impacta o Brasil).
    2. Faça uma análise de sentimento da notícia, determinando se ela representa uma Boa notícia para o país ou uma Péssima notícia para o país (com base no conteúdo econômico e impacto financeiro).
    3. Apresente as informações de forma estruturada como no exemplo abaixo:

[Título da Notícia]
Tipo de Notícia: [Nacional ou Internacional]
Análise de sentimento da notícia: [Boa notícia para o país ou Péssima notícia para o país]

Regras adicionais:
    • As notícias devem ser atuais (últimos 2 dias).
    • Elimine matérias duplicadas ou de caráter apenas opinativo sem base factual.
    • Priorize temas como: inflação, juros, dólar, commodities, mercado financeiro, decisões do Banco Central, política fiscal, acordos comerciais internacionais, crises globais que afetam o Brasil, etc.
    • Responda apenas com o conteúdo estruturado solicitado.

Se quiser, posso usar esse prompt agora para buscar as notícias diretamente. Deseja que eu execute?

### Execução do prompt gerado

Com base nas informações disponíveis, aqui estão as cinco notícias econômicas mais relevantes, com foco no impacto para o Brasil ou no cenário internacional:

Economia brasileira cresce 1,3% no primeiro trimestre, mostra indicador do BC
Tipo de Notícia: Nacional
Análise de sentimento da notícia: Boa notícia para o país
A economia brasileira registrou crescimento de 1,3% no primeiro trimestre de 2025 em relação ao trimestre anterior, conforme o Índice de Atividade Econômica do Banco Central (IBC-Br). Em comparação com o mesmo período de 2024, o crescimento foi de 3,7%. (O GLOBO)

Política comercial dos EUA alimenta incertezas sobre a economia global, diz Copom
Tipo de Notícia: Internacional
Análise de sentimento da notícia: Péssima notícia para o país
O Comitê de Política Monetária (Copom) do Banco Central destacou que a política comercial dos Estados Unidos está gerando incertezas na economia global, afetando negativamente os mercados emergentes, incluindo o Brasil. (Valor Econômico)

Economia global caminha para recessão, diz agência da ONU
Tipo de Notícia: Internacional
Análise de sentimento da notícia: Péssima notícia para o país
Segundo relatório de uma agência da ONU, o crescimento global deve desacelerar para 2,3% em 2025, colocando a economia mundial no caminho para uma recessão, o que pode impactar negativamente o Brasil. (O GLOBO)

Ibovespa sobe após corte no orçamento e recuo do governo sobre alta do IOF; dólar cai
Tipo de Notícia: Nacional
Análise de sentimento da notícia: Boa notícia para o país
O índice da Bolsa de Valores (Ibovespa) fechou em alta de 0,26%, aos 137.623 pontos, enquanto o dólar comercial caiu 0,27%, valendo R$ 5,65, refletindo positivamente no mercado financeiro brasileiro. (cbn)

Economia global é resiliente a choques, mas há risco protecionista, diz Tatiana Rosito
Tipo de Notícia: Internacional
Análise de sentimento da notícia: Péssima notícia para o país
Tatiana Rosito alertou que, apesar da resiliência da economia global a choques, há riscos associados ao protecionismo, o que pode prejudicar investimentos e afetar negativamente países como o Brasil. (Valor Econômico)



