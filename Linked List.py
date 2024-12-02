# Kelas Node
class Node:
    def __init__(self, data):
        self.data = data
        self.berikutnya = None

# Kelas Linked List
class LinkedList:
    def __init__(self):
        self.kepala = None

    def tambahkan(self, data):
        node_baru = Node(data)
        if not self.kepala:
            self.kepala = node_baru
        else:
            node_terakhir = self.kepala
            while node_terakhir.berikutnya:
                node_terakhir = node_terakhir.berikutnya
            node_terakhir.berikutnya = node_baru

    def tampilkan(self):
        node_sekarang = self.kepala
        while node_sekarang:
            print(node_sekarang.data, end=" -> ")
            node_sekarang = node_sekarang.berikutnya
        print("None")
