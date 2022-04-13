class Laptop:

    name = None
    CPU = None
    RAM = None
    video_card = None
    HDD = None
    motherboard = None
    screen_size = None

    d = dict()
    
    def dicti(self,k,v):
        self.d[k]=v
    
    def showInfo(self):
        print(self.d)
    

acer = Laptop()
acer.name = 'acer'
acer.CPU = 'i3-4005U'
acer.RAM = '16GB'
acer.video_card = 'Nvidia GeForce 820M'
acer.HDD = '500GB'
acer.motherboard = 'aspire e1'
acer.screen_size = 15.3

acer.dicti('Название; ', acer.name)
acer.dicti('Процессор: ', acer.CPU)
acer.dicti('Оперативная память: ', acer.RAM)
acer.dicti('Видеокарта: ', acer.video_card)
acer.dicti('Жёсткий диск: ', acer.HDD)
acer.dicti('Материнская плата: ', acer.motherboard)
acer.dicti('Размер экрана: ', acer.screen_size)

acer.showInfo()

asus = Laptop()
asus.name = 'asus'
asus.CPU = 'amd ryzen 5'
asus.RAM = '8GB'
asus.video_card = 'Nvidia GTX 1060'
asus.HDD = '1TB'
asus.motherboard = 'b450m ds3h'
asus.screen_size = 17

asus.dicti('Название; ', asus.name)
asus.dicti('Процессор: ', asus.CPU)
asus.dicti('Оперативная память: ', asus.RAM)
asus.dicti('Видеокарта: ', asus.video_card)
asus.dicti('Жёсткий диск: ', asus.HDD)
asus.dicti('Материнская плата: ', asus.motherboard)
asus.dicti('Размер экрана: ', asus.screen_size)

asus.showInfo()


mac = Laptop()
mac.name = 'macbook'
mac.CPU = 'intel core i5'
mac.RAM = '16GB'
mac.video_card = 'Intel Iris Plus Graphics 655'
mac.HDD = '1TB'
mac.motherboard = 'A1502'
mac.screen_size = 14.3

mac.dicti('Название; ', mac.name)
mac.dicti('Процессор: ', mac.CPU)
mac.dicti('Оперативная память: ', mac.RAM)
mac.dicti('Видеокарта: ', mac.video_card)
mac.dicti('Жёсткий диск: ', mac.HDD)
mac.dicti('Материнская плата: ', mac.motherboard)
mac.dicti('Размер экрана: ', mac.screen_size)

mac.showInfo()