# CMYKtoRGB
Script que converte imagens .jpg .jpeg .png do CMYK pra o RGB

# Como utilizar
1. Reuna as imagens em uma pasta (pode misturar CMYK e RGB)
2. Execute o arquivo cmyktorgb.exe
3. Informe o caminho para a pasta
4. Aguarde o processamento das imagens finalizar
5. Pronto, imagens convertidas para RGB

# Como funciona
1. Usuario informa o diretório onde as imagens estão alocadas
2. Script utiliza a biblioteca Pillow para abrir as imagens e analisar cada imagem
3. Imagens com formato de cores CMYK são convertidas para RGB
4. As imagens convertidas são salvas com o mesmo nome, substituindo as antigas
5. A cada imagem convertida, o script informa ao usuario *"NomeImagem.jpeg convertido com sucesso!*
6. Após analisar todas as imagens, o script retorna *"Conversão de imagens concluída com sucesso!"*
