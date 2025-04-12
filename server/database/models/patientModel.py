from database.dbConn import db

class PatientModel(db.Model):

	__tablename__ = 'patient_details'

	id = db.Column(db.Integer,primary_key=True)
	patient_id = db.Column(db.String(50), nullable=False)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	birth_date = db.Column(db.Date, nullable=False)
	sex = db.Column(db.String(50), nullable=False)

	def __init__(self, patient_id, first_name, last_name, birth_date, sex):
		self.patient_id = patient_id
		self.first_name = first_name
		self.last_name = last_name
		self.birth_date = birth_date
		self.sex = sex


