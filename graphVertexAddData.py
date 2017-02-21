import subprocess

subprocess.call([
    'curl',
    '-X',
    'POST',
    '-d',
    '{"student_FirstName" : "Abhishek","student_LastName" : "Upadhyay","student_Age" : 26, "student_Email" : "abhishek.up25@gmail.com","student_PhNo" : "6692121422"}',
    '-H',
    'content-type : application/json',
    '-H',
    'Authorization : gds-token N2Y2NDhiNWItN2IxZS00ODQ5LWI3MzktMTBlNmQ1NzMyMTE1OjE0ODc2NzE0NzcxNDg6Qm9yWUUvL0tFVjROY29NRG82VHNaZ2dQN2o1OHc1VTc3RXllMHRRNGJBaz0=',
    'https://ibmgraph-alpha.ng.bluemix.net/ecdf3326-42c9-4fe2-b1d5-04415c9dfa35/g/vertices'
])
"""
Vertex Data Added Response json
{"requestId":"629db745-202a-45b5-add1-ea54183db5d5",
"status":{"message":"","code":200,"attributes":{}},
"result":
{"data":
[{"id":4272,"label":"vertex","type":"vertex",
"properties":{"student_FirstName":[{"id":"t2-3ao-sl","value":"Abhishek"}],
"student_Age":[{"id":"17a-3ao-2dh","value":26}],
"student_LastName":[{"id":"1li-3ao-1l1","value":"Upadhyay"}],
"student_Email":[{"id":"1zq-3ao-35x","value":"abhishek.up25@gmail.com"}],
"student_PhNo":[{"id":"2dy-3ao-3yd","value":"6692121422"}]}}]


"""
