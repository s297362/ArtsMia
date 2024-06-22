import database.DB_connect
from database.DB_connect import DBConnect
from model.arco import Arco
from model.object import Object


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getOggetti():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM objects"""
        cursor.execute(query, ())
        results = []
        for row in cursor:
            results.append(Object(**row))
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT eo.object_id AS o1, eo2.object_id AS o2, COUNT(*) AS weight 
FROM exhibition_objects eo, exhibition_objects eo2 
WHERE eo2.exhibition_id = eo.exhibition_id AND eo2.object_id < eo.object_id
GROUP BY eo2.object_id, eo.object_id
ORDER BY weight DESC """
        cursor.execute(query, ())
        results = []
        for row in cursor:
            results.append(Arco(**row))
        cursor.close()
        conn.close()
        return results