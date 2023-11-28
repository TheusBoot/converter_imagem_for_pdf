import os
from reportlab.pdfgen import canvas
from PIL import Image

def convert_images_to_pdfs():
    # Obter o diretório de trabalho atual
    current_directory = os.getcwd()

    # Listar todos os arquivos no diretório de trabalho atual
    image_files = [f for f in os.listdir(current_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Verificar se há pelo menos uma imagem no diretório atual
    if not image_files:
        print("Nenhuma imagem encontrada no diretório atual.")
        return

    # Criar um objeto PDF usando reportlab
    pdf_output_path = os.path.join(current_directory, "output.pdf")
    pdf = canvas.Canvas(pdf_output_path)

    # Iterar sobre as imagens e adicionar cada uma ao PDF
    for image_file in image_files:
        # Construir o caminho completo da imagem
        image_path = os.path.join(current_directory, image_file)

        # Abrir a imagem usando PIL (Python Imaging Library)
        image = Image.open(image_path)

        # Obter as dimensões da imagem
        img_width, img_height = image.size

        # Adicionar uma nova página para cada imagem (exceto na primeira iteração)
        if pdf.getPageNumber() > 0:
            pdf.showPage()

        # Desenhar a imagem na página PDF
        pdf.drawInlineImage(image, 0, 0, width=img_width, height=img_height)

    # Salvar o arquivo PDF
    pdf.save()

# Exemplo de uso
convert_images_to_pdfs()
