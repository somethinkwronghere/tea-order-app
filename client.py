import socket
import json

def connect_to_server(host='localhost', port=5000):
    # Client socket'i oluştur
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Server'a bağlan
        client.connect((host, port))
        print(f"Server'a bağlandı: {host}:{port}")
        
        while True:
            # Kullanıcıdan komut al
            print("\nKomutlar:")
            print("1. Fiyatları göster")
            print("2. Sipariş ver")
            print("3. Siparişleri listele")
            print("4. Çıkış")
            
            choice = input("\nSeçiminiz (1-4): ")
            
            if choice == '1':
                # Fiyatları iste
                message = {'type': 'get_prices'}
                client.send(json.dumps(message).encode('utf-8'))
                response = json.loads(client.recv(4096).decode('utf-8'))
                if response['type'] == 'prices':
                    print("\nFiyatlar:")
                    for item, price in response['data'].items():
                        print(f"{item}: {price} TL")
                        
            elif choice == '2':
                # Sipariş ver
                print("\nSiparişinizi girin (örn: 'Çay x 2, Kahve (sade) x 1'):")
                order_text = input("Sipariş: ")
                
                message = {
                    'type': 'place_order',
                    'order': order_text
                }
                client.send(json.dumps(message).encode('utf-8'))
                response = json.loads(client.recv(4096).decode('utf-8'))
                if response['type'] == 'order_confirmed':
                    print(f"Siparişiniz alındı! Sipariş ID: {response['order_id']}")
                    
            elif choice == '3':
                # Siparişleri listele
                message = {'type': 'get_orders'}
                client.send(json.dumps(message).encode('utf-8'))
                response = json.loads(client.recv(4096).decode('utf-8'))
                if response['type'] == 'orders':
                    print("\nAktif Siparişler:")
                    for order in response['data']:
                        print(f"ID: {order['id']}")
                        print(f"Sipariş: {order['order']}")
                        print(f"Zaman: {order['time']}")
                        print("-" * 30)
                        
            elif choice == '4':
                print("Çıkış yapılıyor...")
                break
                
            else:
                print("Geçersiz seçim!")
                
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        client.close()

if __name__ == '__main__':
    # Server IP'sini girin (varsayılan: localhost)
    server_ip = input("Server IP adresi (varsayılan: localhost): ").strip() or 'localhost'
    connect_to_server(server_ip) 