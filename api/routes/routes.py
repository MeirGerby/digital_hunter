from fastapi import APIRouter 
from repository.sql_queries import MysqlQueries 
from shared import MySQLConnector

queries = MysqlQueries()
router = APIRouter() 

@router.get("/movement-alert")
async def target_movement_alert():
    conn = MySQLConnector()
    data =  queries.target_movement_alert(conn)
    return data 


@router.get("/analysis")
async def analysis_collection_sources():
    conn = MySQLConnector()
    data =  queries.analysis_collection_sources(conn)
    return data 

@router.get("/new-targets")
async def finding_new_targets():
    conn = MySQLConnector()
    data =  queries.finding_new_targets(conn)
    return data 