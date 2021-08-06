from app import db
from app.model.info import Information

class Student:
    def exception_handler(func):
        def inner_function(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except Exception as e:
                 return{'status':400,'message':'Error occurs'}
        return inner_function 
    def json(self):
        return {'id': self.id, 'Student_Name': self.Student_Name,'Student_department': self.Student_Department}
      
    #Create student information
    @exception_handler 
    def create_information(Student_Name,Student_department):
        add_information = Information(Student_Name=Student_Name, Student_Department=Student_department)
        db.session.add(add_information)  
        db.session.commit() 

    #Read all student information 
    @exception_handler  
    def read_all_information():
    
        return [Student.json(data) for data in Information.query.all()] 

    #Read student information by id
    @exception_handler 
    def read_information_by_id(id):
        
        return [Student.json(Information.query.filter_by(id=id).first())]
        
    #Update student information 
    @exception_handler 
    def update_information(id,Student_Name,Student_department):
    
        update = Information.query.filter_by(id=id).first()
        update.Student_Name = Student_Name
        update.Student_Department = Student_department
        db.session.commit()

    #Delete student information 
    @exception_handler 
    def delete_information(id):
        Information.query.filter_by(id=id).delete()
        db.session.commit()  

    