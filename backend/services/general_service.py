from supabase.client import PostgrestAPIError
from supabase import PostgrestAPIResponse
from typing import Union, List
from pydantic import BaseModel
from models import PaginationModel
from db import supabase

class GeneralService():
    def __init__(self, table_name):
        self.table_name = table_name


    def create(self, item):
        try:
            data = supabase.table(self.table_name).insert(item).execute()
            print(data)
        except PostgrestAPIError as e:
            print("Error: ", e.json())
            return [None, e.json()]
        return [data, None]
    
    def find(self, model: BaseModel, pagination: PaginationModel, search_dict: dict):
        query = (
            supabase.from_(self.table_name)
                .select('*')
                .limit(pagination.per_page)
                .offset(pagination.per_page * (pagination.page-1))
                .order((pagination.sort_by), desc=(True if pagination.sort_order is 'desc' else False))
        )
        print(model)
        query = self.__get_search_query(query, model)

        try: 
            data = query.execute() 
        except PostgrestAPIError as e: 
            return [None, e.json()]
        return [data, None]
    

    def find_by_id(self, id):
        data = (
            supabase.from_(self.table_name)
                .select('*').eq("id", id).execute()
        )
        return self.find_one('id', id)

    def find_one(self, by_key: str, by_value):
        data = (
                supabase.from_(self.table_name)
                    .select('*').eq(by_key, by_value).execute()
            )
        return data
    


    
    def delete_by_id(self, id):
        return self.delete_one(by_key='id', by_value=id)

    def delete_one(self, by_key: str, by_value):
        data = (
                supabase.from_(self.table_name)
                    .delete().eq(by_key, by_value).execute()
            )
        return data

    def __get_search_query(self,query, model):
        # search_dict = {}
        return query
