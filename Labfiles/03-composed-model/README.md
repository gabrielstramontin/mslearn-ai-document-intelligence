# Set up Resources:
01. We'll use a script to create the Azure AI Document Intelligence resource, a storage account with sample forms, and a resource group:
  - In the Cloud Shell, to clone the code repository, enter this command: (Bash type choosed at Cloud Shell)
[
rm -r doc-intelligence -f
git clone https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence doc-intelligence
]
  - Change the 03-composed-model directory and then execute the setup script:
[
cd doc-intelligence/Labfiles/03-composed-model/
bash setup.sh
]
