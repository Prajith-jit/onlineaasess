import  os
import  json
from    azure.identity      import AzureCliCredential
from    azure.mgmt.resource import ResourceManagementClient

credential = AzureCliCredential()

#Need to update your subscription id
subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID','your sub id')
resource_client = ResourceManagementClient(credential, subscription_id)
group_list = resource_client.resource_groups.list()

rgname      = []
rglocation  = []

for group in list(group_list):
    rgname.append(group.name)
    rglocation.append(group.location)

map_of_rg ={
    "rgname"        : 'avdtest',
    "rglocation"    : 'UK South'
}

# Open a Json and write into it
with open('output.json', 'w') as fp:
    json.dump(map_of_rg, fp)