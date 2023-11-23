# Autodock-vina-with-interface
Interface for autodock vina
Script para Download de Ligante e Execução do Vina
Este script em Python cria uma interface gráfica simples usando o módulo tkinter para realizar o download de um ligante e executar o Vina, um software de docking molecular.

Requisitos
Certifique-se de ter o Python instalado no seu sistema. O script faz uso das bibliotecas tkinter para a interface gráfica.

Como Usar
Download do Ligante:

Insira o CID do ligante que deseja baixar no campo de entrada.
Clique no botão "Download Ligand" para iniciar o download.
Configuração:

A seção "Config" permite selecionar um arquivo de configuração.
Saída:

Os campos "Output" e "Image Output" são para especificar os diretórios de saída desejados.
Execução do Vina:

Clique no botão "Run Vina" para executar o Vina com as configurações e ligante selecionados.
Detalhes do Script
O script é composto pelos seguintes elementos:

ligand_download_button: Botão para iniciar o download do ligante, onde o usuário deve inserir o CID do ligante desejado.

config_entry: Campo de entrada para a configuração.

config_button: Botão para selecionar o arquivo de configuração.

output_entry: Campo de entrada para o diretório de saída.

image_entry: Campo de entrada para o diretório de saída da imagem.

run_button: Botão para executar o Vina com as configurações selecionadas.

Como Executar o Script
Clone ou baixe este repositório.

Abra um terminal/prompt de comando e navegue até o diretório do script.

Execute o script com o comando python nome_do_script.py.

A interface gráfica será exibida. Preencha os campos conforme necessário e utilize os botões para realizar as ações desejadas.
