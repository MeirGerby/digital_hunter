from fastapi import APIRouter 
from repository.sql_queries import MysqlQueries 
from shared import MySQLConnector

queries = MysqlQueries()
router = APIRouter() 

@router.get("/")
async def target_movement_alert():
    conn = MySQLConnector()
    data =  queries.target_movement_alert(conn)
    return data 