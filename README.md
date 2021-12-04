# Meteor Challenge

![Python Version](https://img.shields.io/badge/Python-3.9.7-orange?style=flat&logo=python&logoColor=eeeeee)
![OpenCV Version](https://img.shields.io/badge/OpenCV-4.5.4-orange?style=flat&logo=python&logoColor=eeeeee)

### Tasks:

- [X] Count the number of Stars
- [X] Count the number of Meteors
- [X] If the Meteors are falling perpendicularly to the Ground (Water level), count how many will fall on the Water
- [ ] (optional) Find the phrase that is hidden in the dots in the sky. 
HINT 1: 177 Characters
HINT 2: Most of the last tasks’ code can be reused for this one

Please, send us the result and code you used to solve the tasks above. Explain how you achieved the results in each question. Good work!!

Subject: [CHALLENGE] [METEOR] *your name*

[Sample] Answers:

Number of Stars
Number of Meteors
Meteors falling on the Water
(optional) Hidden Phrase

Pixel Ref:

    (pure white)    Stars
    (pure red)      Meteors
    (pure blue)     Water
    (pure black)    Ground

### Pré-requisitos

Antes de executar o código, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Python 3](https://www.python.org/downloads/), [OpenCV](https://docs.opencv.org/3.4/da/df6/tutorial_py_table_of_contents_setup.html). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

Após instalar as ferramentas, basta baixar o projeto, extrair e executar o comando:

    python countcolors.py

E os resultados serão impressos no prompt de comando, seguindo a ordem de:

    Altura x Largura
    Stars: 
    Meteors: 
    Meteors in water:

### Resolução

Antes de partir para a resolução do desafio em si, primeiramente, procurei alguma biblioteca que me auxiliasse com o processamento da imagem a ser analisada. Resolvi então utilizar a biblioteca OpenCV, com auxílio da linguagem Python. Logo, é necessário ter os dois instalados na máquina antes de executar o programa.

Após análise visual, percebi que cada estrela e meteoro, na verdade, se trata de um único pixel da imagem, puramente vermelho ou puramente branco, como é dito no desafio. Logo, a minha ideia inicial para as duas primeiras tarefas foi percorrer todos os pixels da imagem e verificar se a cor dele corresponde a branco ou vermelho, e para cada correspondência, incrementar um contador de estrelas ou meteoros.


Para mais informações sobre como o código foi pensado, visualizar o relatório presente no repositório.

### Autor
---

 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/39316240?v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Thiago Marinho</b></sub></a> <a href="https://blog.rocketseat.com.br/author/thiago//" title="Rocketseat">🚀</a>


Feito por Gabriela Silva!

 [![Linkedin Badge](https://img.shields.io/badge/-Gabriela-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/gabrielasil/)](https://www.linkedin.com/in/gabrielasil/) 
[![Gmail Badge](https://img.shields.io/badge/-gabrielamsilva02@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:gabrielamsilva02@gmail.com)](mailto:gabrielamsilva02@gmail.com)




