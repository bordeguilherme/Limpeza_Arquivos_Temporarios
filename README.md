<!DOCTYPE html>
<html

<body>
  <h1 align="center">Scripts de Limpeza de Arquivos Temporários</h1>
</br>
  <h2>Descrição</h2>
Esta documentação explica o uso de dois scripts de automação desenvolvidos para a limpeza de arquivos temporários. Esses scripts têm o objetivo de facilitar e simplificar o processo de manutenção do sistema.

  <h2>O que é um script de automação?</h2>
  <p>Um script de automação é um conjunto de instruções escritas em uma linguagem de programação – neste caso, Python – que automatiza tarefas repetitivas e tediosas, eliminando a necessidade de intervenção humana.</p>

  <h2>O que são arquivos temporários?</h2>
  <p>Como bem explica o site da <a href="https://recoverit.wondershare.com.br/file-recovery/what-are-temporary-files.html">Wondershare</a>, “um arquivo temporário, também conhecido como arquivo temp ou arquivo foo, é um tipo de arquivo criado para armazenar qualquer informação ou dados enquanto o arquivo está sendo criado ou modificado. Depois que o programa é fechado, esse arquivo temporário não é mais necessário [...]. Portanto, podemos dizer que os arquivos temporários são usados para mover e armazenar dados, ajudar a recuperar dados perdidos, gerenciar vários usuários e gerenciar vários tipos de configurações. Esses arquivos temporários são criados por seu sistema operacional quando você está executando ou concluindo qualquer tarefa em seu computador.”</p>

  <h2>Por que excluir esses arquivos temporários?</h2>
  <p>Como dito anteriormente, os arquivos temporários são úteis apenas durante o uso pelo programa correspondente. O acúmulo desses arquivos pode deixar o sistema mais lento, portanto, excluí-los pode melhorar o desempenho do computador.</p>

  <h2>Como se excluiria esses arquivos sem estes scripts?</h2>
  <p>Pressione as teclas Windows + R e digite %TEMP% para abrir os arquivos temporários locais, ou seja, do usuário (Ex.: Admin, Aluno, Felipe, e etc.) então, seria só selecionar todos os arquivos e excluir. Alguns darão erro porque estão sendo utilizados, mas é só ignorá-los. Temos ainda se pressionamos as teclas Windows + R e digitamos temp o computador abrirá os arquivos temporários da pasta raiz do Windows então, seria só seguir os mesmos passos que os arquivos temporários locais. Porém, estes – como é na pasta raiz do Windows – só com um perfil administrativo, e/ou com a permissão do administrador (com senha, caso tenha), poderão ser excluídos.</p>

  <h2>Resumo do Projeto</h2>
  <p>Este projeto inclui dois scripts: um para limpar arquivos temporários locais e outro para arquivos temporários da raiz do Windows. Os scripts foram convertidos em arquivos executáveis (.exe) – Aplicativos – para que possam ser usados sem a necessidade de Python instalado na máquina.</p>

  <h2>Como instalar os scripts na máquina</h2>
  
  <h3>Verificar qual o tipo de sistema do computador:</h3>
  <li>Sabendo a versão do Windows é agora necessário verificar qual o tipo de sistema da máquina. Para isso vá para Menu Iniciar > Configurações > Sistema > Sobre e verifique se o sistema é de 32 ou 64 bits. </li>

  <h3>Abrir a pasta correspondente ao seu tipo de sistema:</h3>
  <li>Repare que temos 4 pastas, pastas para Windows 7 (32 e 64 bits) e Windows 10 e 11 (32 e 64 bits). Abra a pasta correspondente ao seu sistema.</li>

  <h3>Copiar o executável do script de Limpeza Arquivos Temporários da Pasta Raiz do Windows:</h3>
  <li>Primeiro copie apenas o “Limpeza de Arquivos Temporários (Administrador)”, e identifique o perfil administrativo para colar em sua área de trabalho. Após isso vá para Explorador de Arquivos > Meu computador > Disco Local > Usuários > [Perfil Administrador] > Área de Trabalho > Ctrl+V. </li>

  <h3>Copiar o executável do script de Limpeza Arquivos Temporários Locais (do Usuário):</h3>
  <li>Agora copie o arquivo “Limpeza de Arquivos Temporários Locais (Usuários)” e essa no caso deve ficar na Área de Trabalho Pública, ou seja, na que Área de Trabalho que aparece para todos os usuários, para que todos possam fazer a limpeza de seus respectivos perfis. Antes de passar o novo passo a passo, na parte superior do explorador de arquivos clique em “Exibir” e, se não estiver marcada, marque a caixa que diz “Itens ocultos”. Agora vá: Explorador de Arquivos > Meu computador > Disco Local > Usuários > Público > Área de Trabalho Pública > Ctrl+V.</li>

   <h2>Como usar os scripts na máquina</h2>
  
  <h3>Executar o Arquivo:</h3>
  <li>No perfil administrativo, localize o arquivo Limpeza de Arquivos Temporários (Administrador).exe na Área de Trabalho. </li>
  <li>Clique com o botão direito e selecione "Executar como administrador" para garantir as permissões necessárias.</li>
  <li>Em cada perfil de usuário, localize o arquivo Limpeza de Arquivos Temporários Locais (Usuários).exe na Área de Trabalho e clique duas vezes com o botão esquerdo ou uma vez com o botão direito e selecione "Abrir".  </li>

  <h2>Dica</h2>
  <h3>Regularidade</h3>
  <li>Para ajudar a manter seu computador funcionando de maneira eficiente, considere executar este programa regularmente, como uma vez por semana ou pelo menos uma vez por mês. </li>

  <h2>Notas Finais</h2>
  <p>Este executável foi projetado para ser simples e fácil de usar, proporcionando uma maneira rápida de limpar arquivos temporários e melhorar o desempenho do seu computador. </p>

  <h2>Tecnologias Utilizadas</h2>
  <div align="center">
   <img src="img readme/Python.png" height="70" width="70">
    </br>
 <a href="https://www.python.org/downloads/release/python-3810/">Python 3.8.10</a> 

 <a href="https://www.python.org/downloads/release/python-3123/">Python 3.12.3</a>
   </div>

<h2>Autor</h2>  
<div align="center">
<a href="https://github.com/bordeguilherme">Gulherme Borde</a>
  </div>
