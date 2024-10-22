import cv2
import random
from PIL import Image, ImageFilter, ImageEnhance
import os

cap = cv2.VideoCapture(0)
leido, frame = cap.read()
if leido == True:
    cv2.imwrite("photo.jpg", frame)
    print("foto tomada correctamente")
else:
    print("Error al acceder a la camara") 
cap.release()


# Función que aplica un filtro aleatorio a la imagen
def apply_random_filter(image):
    filters = [
        ("BLUR", ImageFilter.BLUR),
        ("CONTOUR", ImageFilter.CONTOUR),
        ("DETAIL", ImageFilter.DETAIL),
        ("SHARPEN", ImageFilter.SHARPEN),
        ("SMOOTH", ImageFilter.SMOOTH),
        ("EDGE_ENHANCE", ImageFilter.EDGE_ENHANCE),
    ]
    
    filter_name, filter_to_apply = random.choice(filters)
    print(f"Applying filter: {filter_name}")
    return image.filter(filter_to_apply)

# Función que ajusta aleatoriamente el brillo, contraste o color
def random_adjust(image):
    adjustments = [
        ("Brightness", ImageEnhance.Brightness),
        ("Contrast", ImageEnhance.Contrast),
        ("Color", ImageEnhance.Color)
    ]
    
    adjustment_name, enhancer = random.choice(adjustments)
    print(f"Applying random adjustment: {adjustment_name}")
    
    enhancer_obj = enhancer(image)
    factor = random.uniform(0.5, 1.5)  # Factor de ajuste aleatorio
    return enhancer_obj.enhance(factor)

# Función principal para cargar la imagen, aplicar filtros y ajustes, y guardarla
def process_image(image_path, output_path='photo_filtered.jpg'):
    try:
        # Cargar la imagen
        image = Image.open(image_path)
        print(f"Image {image_path} loaded successfully.")
        
        # Aplica un filtro aleatorio
        image_with_filter = apply_random_filter(image)

        # Aplica un ajuste aleatorio (brillo, contraste o color)
        final_image = random_adjust(image_with_filter)

        # Evitar sobrescribir el archivo original generando un nuevo nombre si ya existe
        output_name = output_path
        base_name, ext = os.path.splitext(output_path)
        counter = 1
        while os.path.exists(output_name):
            output_name = f"{base_name}_{counter}{ext}"
            counter += 1

        # Guardar la imagen resultante
        final_image.save(output_name)
        print(f"Filtered image saved as {output_name}")

        # Mostrar la imagen
        final_image.show()

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Llamada a la función principal
process_image('photo.jpg')

