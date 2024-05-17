# 01. In the integrated terminal, run the following command to login to Azure: [az login]
# obs: The command will open the Microsoft Edge browser, login with the same account you used to create the Azure AI Document Intelligence resource.

# 02. Also, run the following command to list the Azure locations: [az account list-locations -o table]

# 03. You'll use [setup.cmd] script to run the Azure command line interface (CLI) commands required to create the other Azure resources you need. The program will:
- Create a storage account in your Azure resource group.
- Upload files from your local sampleforms folder to a container called sampleforms in the storage account.
- Print a Shared Access Signature URI.
# obs: Modify the subscription_id, resource_group, and location variable declarations with the appropriate values for the subscription, resource group, and location name where you deployed the Document Intelligence resource. Later, save your changes. Leave the expiry_date variable as it is for the exercise. This variable is used when generating the Shared Access Signature (SAS) URI. In practice, you will want to set an appropriate expiry date for your SAS. 

# 04. In the terminal for the Labfiles/02-custom-document-intelligence folder, enter the following command to run the script:
[
 $currentdir=(Get-Item .).FullName
 cd ..
 ./setup.cmd
 cd $currentdir
]

# 05. To test your custom Document Intelligence Model, you'll need install the Document Intelligence package in the terminal: [pip install azure-ai-formrecognizer==3.3.0]
# 06. Enter the following command to run the program: [python test-model.py]
