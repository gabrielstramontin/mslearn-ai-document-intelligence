from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

# Integrated Terminal (PowerShell):
# 01. To install the Azure Form Recognizer SDK package, run [pip install azure-ai-formrecognizer==3.3.0]

# Store Connection Information:
# 02. Access the Azure Portal, and on displays the Azure AI Document Intelligence Overview, under Resource Management, select Keys and Endpoint. To the right of the Endpoint value, click the Copy to clipboard button.

endpoint = "<Endpoint URL>"
key = "<API Key>"

fileUri = "https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence/blob/main/Labfiles/01-prebuild-models/sample-invoice/sample-invoice.pdf?raw=true"
fileLocale = "en-US"
fileModelId = "prebuilt-invoice"

print(f"\nConnecting to Forms Recognizer at: {endpoint}")
print(f"Analyzing invoice at: {fileUri}")

# Create the Client:
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)
# Analyse the Invoice:
poller = document_analysis_client.begin_analyze_document_from_url(
    fileModelId, fileUri, locale=fileLocale
)

# Display Invoice Information to the user:
receipts = poller.result()

for idx, receipt in enumerate(receipts.documents):
vendor_name = receipt.fields.get("VendorName")

if vendor_name:
    print(f"\nVendor Name: {vendor_name.value}, with confidence {vendor_name.confidence}.")

    customer_name = receipt.fields.get("CustomerName")
    if customer_name:
        print(f"Customer Name: '{customer_name.value}, with confidence {customer_name.confidence}.")

    invoice_total = receipt.fields.get("InvoiceTotal")
    if invoice_total:
        print(f"Invoice Total: '{invoice_total.value.symbol}{invoice_total.value.amount}, with confidence {invoice_total.confidence}.")

print("\nAnalysis complete.\n")

# 03. To run the application, enter this command on the interactive terminal: [python document-analysis.py]
