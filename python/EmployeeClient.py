from __future__ import print_function
import logging

import grpc
import EmployeeService_pb2
import EmployeeService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = EmployeeService_pb2_grpc.EmployeeServiceStub(channel)

        # Query an employee's data
        response = stub.GetEmployeeDataFromID(EmployeeService_pb2.EmployeeID(id=101))
        print ('Employee\'s data: ' + str(response))

        # Add a new employee
        response = stub.CreateEmployee(EmployeeService_pb2.EmployeeData(id=301, name='Jose da Silva', title='Programmer'))
        print ('Added new employee ' + response.status)

        # Change an employee's title
        response = stub.UpdateEmployeeTitle(EmployeeService_pb2.EmployeeTitleUpdate(id=301, title='Senior Programmer'))
        print ('Updated employee ' + response.status)

        # Delete an employee
        response = stub.DeleteEmployee(EmployeeService_pb2.EmployeeID(id=201))
        print ('Deleted employee ' + response.status)

        # List all employees
        response = stub.ListAllEmployees(EmployeeService_pb2.EmptyMessage())
        print ('All employees: ' + str(response))

        #achar funcionario por titulo
        title = "Programmer"
        response = stub.GetEmployeesByTitle(EmployeeService_pb2.EmployeeTitleRequest(title = title))

        print(f"Todo do cargo: {title}\n"+ str(response))

        #achar funcionario por nome
        name = "Saravanan"
        response = stub.GetEmployeesByName(EmployeeService_pb2.EmployeeNameRequest(name = name))
        print(f"Todo com o nome: {name}\n"+ str(response))

if __name__ == '__main__':
    logging.basicConfig()
    run()