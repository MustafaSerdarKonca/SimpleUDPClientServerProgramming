from socket import * #Kütüphanemizi dahil ediyoruz.

serverName = gethostname() #Ardından server adres bilgileri lazım olacak.
serverPort = 12000 #Bunun için IP ve port numaraları belirleyeceğiz. IP local host olacak.
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind((serverName, serverPort)) #Soketimizi oluşturmuş olduk.
print ("\nThe server is ready to receive\n")  #Artık sunucu bağlantıya hazır. Bunu belirtiyoruz.
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) #İlk parametre, clienttan gelen mesaj ve 
    #ikinci parametre ise bu mesajı gönderen clientın adresidir .recvfrom() gelen mesajları okumamızı sağlar.
    print("Message From Client:" +str(clientAddress)) #Bilgilendirme yazısı
    print("Processing...") #Bilgilendirme yazısı
    modifiedMessage = message.upper() #Okunan mesaj .upper() fonksiyonu ile büyük harfli hale getirilir.
    serverSocket.sendto(modifiedMessage, clientAddress) #Büyük harf haline getirilen mesajı clienta gönderilir.
    print("Sending a Message to the Client:" +str(clientAddress)) #Bilgilendirme yazısı