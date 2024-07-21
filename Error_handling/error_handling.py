#There are two methods to handle the file or error 

# step 1 
file = open('test.py','w')
try:
    file.write("error handlimg file.")
finally:
    file.close()

# step 2

with open('test.py','w') as file:
    file.write("error handlimg file.")



sr_config = {
    'url': 'https://confluent.cloud/environments/env-jvy0j8/schema-registry/schemas/',
    'basic.auth.user.info':'HMUWQKBNVTND4VTU : c7B08oKbgh1vrn3N8F+hZ3Xf/ZKhvuuza0+oEimECKAuXJc4afFo5JsrMrxludhF'
}
