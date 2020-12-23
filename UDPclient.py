from socket import * #Kütüphanemizi dahil ediyoruz.

serverName = gethostname() #Ardından server adres bilgileri lazım olacak.
serverPort = 12000 #Bunun için IP ve port numaraları belirleyeceğiz. IP local host olacak.

clientSocket = socket(AF_INET, SOCK_DGRAM)
#socket(family, type) yapısını biraz inceleyelim.  Family parametresi AF_UNIX, AF_INET ve AF_INET6 değişkenlerini alabilir.
#AF_UNIX: UNIX domain protokolleri
#AF_INET: TCP ve UDP için IPv4 protokolleri
#AF_INET6: TCP ve UDP için IPv6 protokolleri
#type parametresi SOCK_STREAM, SOCK_DGRAM, SOCK_RAW, SOCK_RDM ve SOCK_SEQPACKET değişkenlerini alabilir.
#SOCK_STREAM: TCP bağlantı tipi
#SOCK_DGRAM: UDP bağlantı tipi
#SOCK_RAW: Henüz olgunlaşmamış soketler
#SOCK_RDM: Güvenilir datagramlar için
#SOCK_SEQPACKET: Bağlantı üzerinden kayıtlar için bir dizi transfer.
#Ödevde UDP bağlantı tipi ve IPv4 adresleme seçeneğini istenmiş. Clienct ile bağlantıyı da hazır ettiğimize göre 
# Artık server kanalı dinlemeye hazırız demektir.

message = input("\nInput lowercase sentence:") #Servera göndermek istediğimiz mesajı giriyoruz.
clientSocket.sendto(message.encode(), (serverName, serverPort)) #Servere göndermek istediğimiz mesajı 
#yollmak için .sendto() bu fonksiyonun içine de server IP ve portunu veriyoruz.
#Burada Encode işlemi metinleri binary şekle dönüştürerek veri iletmemizi sağlıyor. Mesajımızı iletmemiz için 
# #8 bitlik baytlar hale getirmemiz lazım bu yüzden encoding yapmalıyız. Bu encoding ve decoding işlemlerini
#serverda da yapabilirdik, ben client tercih ettim.Bunun için de .encode () fonksiyonunu kullanıyoruz.

modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #gönderdikten sonra serverden mesajımızı geri 
#almak için .recvfrom() kullanıyoruz.
print("\nMessage Sent to Server :" +str(serverAddress)) #Bilgilendirme yazısı
print("Receiving Message From the Server...") #Bilgilendirme yazısı
print("Your Sentence :"+ modifiedMessage.decode()) #Serverdan aldığımız mesajımızı .decode() fonksiyonu ile orijinal 
#(string) hale getiriyoruz. Ve ekrana yazdırıyoruz.
clientSocket.close() #Son olarak artık soketimizi kapatıyoruz.

