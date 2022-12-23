# my-worldle-solver
A simple robot that solves the Worldle game (worldle.teuteuf.fr)

![Screenshot from 2022-10-15 15-43-03](https://user-images.githubusercontent.com/48096245/196002988-91a085a2-023e-4984-a87e-c6ac2ed6816e.png)


# O Jogo

[Worldle](https://worldle.teuteuf.fr/)

O worldle é um jogo baseado no sucesso Wordle. Ele consiste em adivinhar o país do dia através de sua imagem no mapa e dos feedbacks do jogo relacionados à proximidade dele (em porcentagem, kilômetros e indicação de direção). 

[GitHub](https://github.com/teuteuf/worldle)

# O Resolvedor

O objetivo desse projeto é criar um resolvedor automático do jogo [Worldle](https://worldle.teuteuf.fr/), se resumindo a dois módulos principais:

- O módulo que recebe a imagem do país a ser adivinhado e retorna o nome do país que corresponde à imagem dada;
- O módulo de automação da resolução do problema, ou seja, o robô responsável por abrir a página no navegador, escolher o país correto e retornar o screenshot do sucesso na advinhação.

# Projetos Similares

[https://github.com/p-iraola/worldle_solver](https://github.com/p-iraola/worldle_solver)

O projeto acima se propõe a ser um auxiliar da resolução do Worldle, mas com uma abordagem completamente diferente. Essa abordagem consiste no usuário escolher um país no jogo e inserir no software as respostas de distância do jogo, para que o software retorne opções possíveis para que o usuário use na próxima tentativa. Este foi o primeiro projeto relacionado à resolução do Worldle que eu encontrei e recomendo muito que você conheça ele também.

Acredito que haja muitos outros projetos com esse objetivo, mas confesso que tive muita dificuldade de buscá-los, porque as pesquisas insistem em demonstrar os resolvedores de [Wordle](https://www.nytimes.com/games/wordle/index.html).

# Execução

Para executar o resolvedor, é necessária conexão com a internet, python 3 e a biblioteca Playwright. Clone o repositório e, na raiz do projeto, execute `python solver.py`. Aguarde um pouco enquanto ele analisa a página para identificar o país ou território. Uma janela de navegação irá aparecer e um país será escolhido automaticamente. A resposta será submetida e um screenshot do sucesso (espero) será salvo em seu computador! :)

