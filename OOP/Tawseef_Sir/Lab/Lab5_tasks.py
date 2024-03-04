# from abc import ABC, abstractmethod
import copy


class Account():
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    # @abstractmethod

    def show_balance(self):
        print(f'Balance: {self.balance}')


class SavingsAccount(Account):
    def __init__(self, name, balance=0, interest_rate=0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def deposit_money(self, amount):
        self.balance += amount

    def make_profit(self):
        self.balance += self.balance * self.interest_rate

# ac1 = SavingsAccount("Zodu", 500, 0.3)
# ac1.make_profit()
# ac1.show_balance()


class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist}."


class Playlist:
    def __init__(self, name):
        self.name = name
        self.song_list = []

    def add_song(self, song):
        if song not in self.song_list:
            self.song_list.append(copy.deepcopy(song))
        else:
            print("Song alrady exist!")

    def remove_song(self, song_title):
        self.song_list = [x for x in self.song_list if x.title != song_title]

    def display_song(self):
        print([str(i) for i in self.song_list])

    def search_song(self, song_title):
        for song in self.song_list:
            if song.title == song_title:
                return print(f"{song} in the playlist")
        return print("Not Found")

song1 = Song( "I am from Barishal","Mahi", "5 min")
song2 = Song( "I am from NoaKhali","Habib", "5 min")
song3 = Song( "I am from Bangladesh","Mahi", "5 min")
MyPlayList = Playlist("Habibi")
MyPlayList.add_song(song1)
MyPlayList.add_song(song2)
MyPlayList.add_song(song3)
MyPlayList.display_song()
# MyPlayList.search_song("Mui Borishailaa")
MyPlayList.search_song("I am from Bangladesh")