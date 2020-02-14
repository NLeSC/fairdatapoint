from pyshacl import validate

# This should be loaded from a file: fdp/schema/dataset.ttl or something
shapes_file = '''
@prefix schema: <http://schema.org/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

schema:DatasetShape
    a sh:NodeShape ;
    sh:targetClass schema:Dataset ;
    sh:property [
        sh:path schema:givenName ;
        sh:datatype xsd:string ;
        sh:name "given name" ;
    ] ;
    sh:property [
        sh:path schema:birthDate ;
        sh:lessThan schema:deathDate ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path schema:gender ;
        sh:in ( "female" "male" ) ;
    ] ;
    sh:property [
        sh:path schema:address ;
        sh:node schema:AddressShape ;
    ] .
schema:AddressShape
    a sh:NodeShape ;
    sh:closed true ;
    sh:property [
        sh:path schema:streetAddress ;
        sh:datatype xsd:string ;
    ] ;
    sh:property [
        sh:path schema:postalCode ;
        sh:or ( [ sh:datatype xsd:string ] [ sh:datatype xsd:integer ] ) ;
        sh:minInclusive 10000 ;
        sh:maxInclusive 99999 ;
    ] .
'''
shapes_file_format = 'turtle'

# This data should be posted
data_file = '''
@prefix schema: <http://schema.org/> .

<http://example.org/ns#Bob> a schema:Dataset ;
    schema:address <http://example.org/ns#BobsAddress> ;
    schema:birthDate "1971-07-07" ;
    schema:deathDate "1998-09-10" ;
    schema:familyName "Junior" ;
    schema:givenName "Robert" .

<http://example.org/ns#BobsAddress> schema:postalCode 94040 ;
    schema:streetAddress "1600 Amphitheatre Pkway" .
'''
data_file_format = 'turtle'


conforms, v_graph, v_text = validate(data_file, shacl_graph=shapes_file,
                                     data_graph_format=data_file_format,
                                     shacl_graph_format=shapes_file_format,
                                     inference='rdfs', debug=False,
                                     serialize_report_graph=True)

print('Dataset not yet  implemented -- self destructing...')
exit()
print('conforms >>>>>>>>>>>>>>>>>')
print(conforms)
print('v_graph >>>>>>>>>>>>>>>>>>')
print(v_graph)
print('v_text >>>>>>>>>>>>>>>>>>>')
print(v_text)
