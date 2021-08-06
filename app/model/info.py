from app import db
class Information(db.Model):
    __tablename__ = 'student_information'  
    id = db.Column(db.Integer, primary_key=True)  
    Student_Name = db.Column(db.String(25))
    Student_Department= db.Column(db.String(25))
    
    

