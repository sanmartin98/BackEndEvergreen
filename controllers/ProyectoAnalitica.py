from flask import jsonify, request
from db.db import cnx

class ProyectoAnalitica():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM proyectos_analitica")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close

    def create(body):
        data = (body['nombreProyecto'], body['descProyecto'], body['moduloEncargado'], body['personaEncargada'], body['descDataset'], body['tipoProyecto'], body['estado'])
        sql = "INSERT INTO proyectos_analitica(nombre_proyecto, desc_proyecto, modulo_encargado, persona_encargada, desc_dataset, tipo_proyecto, estado) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Insertado'}, 200
        cnx.close

    def delete(body):
        data = (body['idProyecto'],)
        sql = "DELETE FROM proyectos_analitica WHERE id_proyecto = %s"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Eliminado con exito'}, 200
        cnx.close

    def update(body):
        data = (body['nombreProyecto'], body['descProyecto'], body['moduloEncargado'], body['personaEncargada'], body['descDataset'], body['idProyecto'])
        sql = "UPDATE proyectos_analitica SET nombre_proyecto = %s, desc_proyecto = %s, modulo_encargado = %s, persona_encargada = %s, desc_dataset = %s WHERE id_proyecto = %s"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Actualizado con exito'}, 200
        cnx.close