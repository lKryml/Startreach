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
        except PostgrestAPIError as e:
            return [None, e.json()]
        return [data, None]
    
    def find(self, model: BaseModel, pagination: PaginationModel):
        query = (
            supabase.from_(self.table_name)
                .select('*')
                .limit(pagination.per_page)
                .offset(pagination.per_page * (pagination.page-1))
                .order((pagination.sort_by), desc=(True if pagination.sort_order == 'desc' else False))
        )
        query = self.__get_search_query(query, model)
        if pagination.where:
            print(pagination.where.items())
            for key, value in pagination.where.items():
                query = query.eq(key, value)
        try: 
            data = query.execute() 
        except PostgrestAPIError as e: 
            return [None, e.json()]
        return [data, None]
    

    def find_by_id(self, id):
        return self.find_one({ 'id': id })

    def find_one(self, where):
        if where is None:
            return [None, None]
        query = supabase.from_(self.table_name).select('*')
        for key, value in where:
            query = query.eq(key, value)
        try:
            data = query.limit(1).execute()
        except PostgrestAPIError as e:
            return [None, e.json()]
        return [data, None]
    

    def update(self, where: dict[str, any], item: BaseModel | dict):
        if where is None:
            return [None, None]
        
        if isinstance(item, BaseModel):
            item = item.model_dump()
        
        query = supabase.from_(self.table_name).update(item)
        for key, value in where:
            query = query.eq(key, value)

        try:
            data = query.execute()
        except PostgrestAPIError as e:
            return [None, e.json()]
        return [data, None]
        
    
    def delete_by_id(self, id):
        return self.delete_one({ 'id': id })

    def delete_one(self, where: dict[str, any]):
        if where is None:
            return [None, None]
        query = supabase.from_(self.table_name)
        for key, value in where:
            query = query.eq(key, value)
        try:
            data = query.delete().execute()
        except PostgrestAPIError as e:
            return [None, e.json()]
        return data
    
    
    def upload_image(self):
        pass

    def __get_search_query(self,query, model):
        return query
