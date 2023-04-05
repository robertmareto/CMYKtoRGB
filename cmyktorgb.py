from PIL import Image
import os

# selecionar a pasta onde estão as imagens
pasta = input("Digite o caminho para a pasta com as imagens: ")

# percorrer todos os arquivos na pasta selecionada
for arquivo in os.listdir(pasta):
    if arquivo.endswith('.jpg') or arquivo.endswith('.jpeg') or arquivo.endswith('.png'):
        
        # abrir a imagem em CMYK
        imagem_cmyk = Image.open(os.path.join(pasta, arquivo))
        
        # converter a imagem em CMYK para RGB
        imagem_rgb = imagem_cmyk.convert('RGB')
        
        # salvar a imagem convertida com o mesmo nome de arquivo da imagem original
        imagem_rgb.save(os.path.join(pasta, arquivo))
        
        # imprimir mensagem de conclusão
        print(f'{arquivo} convertido com sucesso!')
    
  
print("============================================")
print("Conversão de imagens concluída com sucesso!")
input("Pressione Enter para sair...")