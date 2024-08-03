import json
from flask import jsonify
import psycopg2
from flask_cors import CORS



class db:
 def connect(self):
    return psycopg2.connect(host = "localhost", user = "postgres", password = "1234", database = "postgres", port = "5432")
 def get_all(self):
        try:
            con = self.connect()
            cursor = con.cursor()
            cursor.execute('select * from item')
            data = cursor.fetchall()
            if len(data):
                response = jsonify({'message' : 'success', 'data' : data}) 
            else:
                response = jsonify({'message' : 'success', 'data' : []})
        except Exception as e:
            response = jsonify({'message' : 'failed', 'error':str(e), 'data' : []})
        finally:
            con.close()
            
            
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
       
        
 def getitemiId(self, iId):
        try:
             con = self.connect()
             cursor = con.cursor()
             cursor.execute('select * from item where iId = ' + iId ) 
             data = cursor.fetchone()
             if len(data):
                response = jsonify({'message' : 'success', 'data' : data}) 
             else:
                response = jsonify({'message' : 'success', 'data' : []})
        
        except Exception as e:
            response = jsonify({'message' : 'failed', 'error':str(e), 'data' : []})
        finally:
         con.close()
            
            
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
        
      
 def insert_item(self, iId, Iname, Sprice):
    try:
        con = self.connect()
        cursor = con.cursor()
        query = "insert into item (iId, Iname, Sprice) VALUES ('" +iId+ "', '" +Iname+ "', '" +Sprice+ "')"
        cursor.execute(query)
        con.commit()
        response = jsonify({'message': 'success', 'data': 'Inserted'})
    except Exception as e:
        response = jsonify({'message': 'failed', 'error': str(e), 'data': []})
    finally:
        con.close()
            
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


        
 def update_item(self, iId, Iname, Sprice):
    try:
        con = self.connect()
        cursor = con.cursor()
        cursor.execute('UPDATE item SET iId = %s, Iname = %s WHERE Sprice = %s', (str(iId), str(Iname), str(Sprice)))
        con.commit()
        response = jsonify({'message': 'success', 'data': 'Updated'})
    except Exception as e:
        response = jsonify({'message': 'failed', 'error': str(e), 'data': []})
    finally:
        con.close()

        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

        
 def delete_item(self, iId, Iname, Sprice):
    try:
        con = self.connect()
        cursor = con.cursor()
        cursor.execute('DELETE FROM item WHERE iId = %s AND Iname = %s AND Sprice = %s', (str(iId), str(Iname), str(Sprice)))
        con.commit()
        response = jsonify({'message': 'success', 'data': 'Deleted'})
    except Exception as e:
        response = jsonify({'message': 'failed', 'error': str(e), 'data': []})
    finally:
        con.close()
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response



def search_item(self, iId,):
    try:
        con = self.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM item WHERE iId LIKE %s OR Iname LIKE %s", ( (str(iId))))
        data = cursor.fetchall()
        if len(data):
            response = jsonify({'message': 'success', 'data': data})
        else:
            response = jsonify({'message': 'success', 'data': []})

    except Exception as e:
        response = jsonify({'message': 'failed', 'error': str(e), 'data': []})
    finally:
        con.close()

    return response
