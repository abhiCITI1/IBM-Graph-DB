import subprocess

schemaFile = open("studentJobHuntSchema.json" ,'rb').read()


subprocess.call([
    'curl',
    '-X',
    'POST',
    '-d',
    schemaFile,
    '-H',
    'content-type : application/json',
    '-H',
    'Authorization : gds-token N2Y2NDhiNWItN2IxZS00ODQ5LWI3MzktMTBlNmQ1NzMyMTE1OjE0ODc2NzE0NzcxNDg6Qm9yWUUvL0tFVjROY29NRG82VHNaZ2dQN2o1OHc1VTc3RXllMHRRNGJBaz0=',
    'https://ibmgraph-alpha.ng.bluemix.net/ecdf3326-42c9-4fe2-b1d5-04415c9dfa35/g/schema'
])
