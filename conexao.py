import psycopg2
import os
import sys
from nota import Nota

class Conexao:

	def __init__(self, dbname, host = "localhost", user = "postgres" , password = "postgres" ):
		try:
			self.conn = psycopg2.connect("host="+host+" dbname="+dbname+" user="+user+" password="+password)
			self.cur = self.conn.cursor()
		except:
			  "Deu xabum na conexao...."
			  exit()	

	def encerra(self):
		self.cur.close()
		self.conn.close()
  
class LixeiraDAO():
	def __init__(self, conexao):
		self.insertSQL = "INSERT INTO lixeira (titulo, descricao, cor,imagem) VALUES(%s, %s, %s, %s)"
		self.deleteSQL = "DELETE FROM lixeira WHERE id = %s"
		self.selectOneSQL = "SELECT titulo, descricao, cor, imagem FROM lixeira where id = %s" 
		self.conexao = conexao
		self.selectTodosSQL = "SELECT titulo, descricao, id, cor, imagem FROM lixeira"

   	def inserir (self, nota):
		parametros = []
		parametros.append(nota.titulo)	
		parametros.append(nota.descricao)
		parametros.append(nota.cor)
		parametros.append(nota.imagem)		
		self.conexao.cur.execute(self.insertSQL, parametros)	
		self.conexao.conn.commit()
  
   	def restaurar(self, id):
		parametros = []
		parametros.append(id)
		
		self.conexao.cur.execute(self.selectOneSQL, parametros)
		registro = self.conexao.cur.fetchone()
		print "REGISTROS:"
		print registro

		notaDAO = NotaDAO(self.conexao)		
		notaDAO.inserir(Nota(registro[0], registro[1],id, registro[2],registro[3]))
		
		self.conexao.cur.execute(self.deleteSQL, parametros)	
		self.conexao.conn.commit()
          
          
          
   	def deletar(self, id):
		parametros = []
		parametros.append(id)
		self.conexao.cur.execute(self.deleteSQL, parametros)	
		self.conexao.conn.commit()
  
   	def listaTodos(self):
		self.conexao.cur.execute(self.selectTodosSQL)			
		linhasRetornadas = self.conexao.cur.rowcount; #linhas afetadas de um select
		#print linhasRetornadas
		vetNota = []
		i = 0
		while(i < linhasRetornadas):
			registro = self.conexao.cur.fetchone()
			vetNota.append(Nota(registro[0], registro[1],registro[2],registro[3],registro[4]))
			i = i + 1	
		return vetNota

class NotaDAO:
	def __init__(self, conexao):
		self.deleteSQL = "DELETE FROM nota WHERE id = %s"
		self.selectTodosSQL = "SELECT titulo, descricao, id, cor, imagem FROM nota"
		self.updateSQL = "UPDATE nota SET titulo = %s, descricao = %s, cor=%s, imagem=%s WHERE id = %s"
		self.insertSQL = "INSERT INTO nota (titulo, descricao, cor, imagem) VALUES(%s, %s, %s, %s)"
		self.pesquisaajaxSQL = "SELECT * FROM nota where titulo ilike %s"
		self.selectOneSQL = "SELECT * FROM nota where id = %s" 
		self.conexao = conexao	

	def ajax(self, titulo):
		self.conexao.cur.execute(self.pesquisaajaxSQL,[titulo])		
		linhasRetornadas = self.conexao.cur.rowcount; #linhas afetadas de um select
		vetNota = []
		i = 0
		while(i < linhasRetornadas):
			registro = self.conexao.cur.fetchone()
			vetNota.append(Nota(registro[0], registro[1], registro[2], registro[3], registro[4]))
			i = i + 1	
		self.conexao.conn.commit()
		return vetNota

	def inserir (self, nota):
		parametros = []
		parametros.append(nota.titulo)	
		parametros.append(nota.descricao)
		parametros.append(nota.cor)
		parametros.append(nota.imagem)
		self.conexao.cur.execute(self.insertSQL, parametros)	
		self.conexao.conn.commit()

	def alterar(self, nota):
		parametros = []
		parametros.append(nota.titulo)	
		parametros.append(nota.descricao)
		parametros.append(nota.cor)
		parametros.append(nota.imagem)
		parametros.append(nota.id)
		self.conexao.cur.execute(self.updateSQL, parametros)	
		self.conexao.conn.commit()

 
	def listaTodos(self):
		self.conexao.cur.execute(self.selectTodosSQL)			
		linhasRetornadas = self.conexao.cur.rowcount;
		vetNota = []
		i = 0
		while(i < linhasRetornadas):
			registro = self.conexao.cur.fetchone()
			
			vetNota.append(Nota(registro[0], registro[1], registro[2], registro[3], registro[4]))
			i = i + 1	
		return vetNota
	
	def replica(self, id):
		parametros= []
		parametros.append(id)         
		self.conexao.cur.execute(self.selectOneSQL, parametros)
		registro = self.conexao.cur.fetchone()
		notaDAO = NotaDAO(self.conexao)
		notaDAO.inserir(Nota(registro[0], registro[1], registro[3], registro[2],registro[4]))

	def deletar(self, id):
		parametros = []
		parametros.append(id)

		self.conexao.cur.execute(self.selectOneSQL, parametros)
		registro = self.conexao.cur.fetchone()
		lixeiraDAO = LixeiraDAO(self.conexao)

		lixeiraDAO.inserir(Nota(registro[0], registro[1], id, registro[2],registro[4]))
		
		self.conexao.cur.execute(self.deleteSQL, parametros)	
		self.conexao.conn.commit()

