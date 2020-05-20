# arquivo de camera
import os
import cv2
import imutils

foderPath = os.path.dirname(__file__)

# Importar arquivo XML


# Importar arquivo XML
# caminho arquivos (C:\Users\Renato\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascades)


xmlPedetrians = 'hogcascade_pedestrians.xml'
xmlPedetriansPath = os.path.join(
    foderPath, 'hogcascade_pedestrians.xml')

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# Inicializar Classificador
clf = cv2.CascadeClassifier(
    '/project/packages/raspbarryServer/hogcascade_pedestrians.xml')

# Inicializar webcam
cap = cv2.VideoCapture(0)
# Loop para leitura do conteúdo
while not cv2.waitKey(2) & 0xFF == ord('q'):
    # Capturar proximo frame
    ret, frameCamera = cap.read()
    frame = imutils.resize(frameCamera, width=min(400, frameCamera.shape[1]))

    # Converter para tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Classificar
    plates = clf.detectMultiScale(gray, 1.3, 5)
    (regions, _) = hog.detectMultiScale(frame,
                                        winStride=(4, 4),
                                        padding=(4, 4),
                                        scale=1.05)

    # Desenhar retangulo
    for x, y, w, h in plates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0))

    for (x, y, w, h) in regions:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)

        # Visualizar
    cv2.imshow('frame', frame)

# Desligar a webcam
cap.release()

# Fechar janela do vídeo
cv2.destroyAllWindows()

''' testes a se fazer

    testar a placa de pare, como identificar ....
    teste de envio de informação via socket ....

'''
