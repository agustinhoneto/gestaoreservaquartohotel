from configurations.configurations import Configurations
from repositories.room_repository import RoomRepository
from models.room import Room
import pandas as pd

class RoomService():
    
    def __init__(self):
        self.__configurations = Configurations()
        self.__room_repository = RoomRepository()

    def create_and_save_room(self, hotel_id, room_id, floor, room_type, daily_rate):
        room = Room(hotel_id, room_id, floor, room_type, daily_rate)
        return self.__room_repository.save(room)
    
    def delete_hotel_rooms(self, hotel_id):
        rooms_df = self.__room_repository.read_room()
        for room_id in rooms_df.loc[rooms_df['hotel_id']==hotel_id, 'room_id']:
            self.__room_repository.delete_room(hotel_id, room_id)

    def remove_room(self, hotel_id, room_id):
        self.__room_repository.delete_room(hotel_id, room_id)

    def get_rooms_by_hotel_id(self, hotel_id):
        rooms_df = self.__room_repository.read_room()
        return rooms_df[rooms_df['hotel_id']==hotel_id] if not rooms_df.empty else pd.DataFrame()
    
    def show_rooms(self):
        print('Tipos de quartos: ')
        for room_type in self.__configurations.room_types:
            print(f'• {room_type}')

    def choose_room_type(self):
        room_type = input('Informe o tipo do quarto: ')
        while room_type not in self.__configurations.room_types:
                print('\t< Tipo de quarto inválido >\nInsira um dos tipos mostrados na lista!\n')
                self.show_rooms()
                room_type = input('Tipo do quarto: ')
        return room_type