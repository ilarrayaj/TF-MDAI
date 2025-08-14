import os, base64, json, requests

REPO = "ilarrayaj/TF-MDAI"
TOKEN = os.environ["GH_TOKEN"]
API = "https://api.github.com"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

COMMIT_AUTHOR = {"name": "TF_MDAI_Bot", "email": "bot@tfmdai.local"}
COMMIT_MESSAGE = "Initialize Technical File structure for MDR + AI Act"

paths = [
    "Technical-File-MDAI/README.md",
    "Technical-File-MDAI/.github/workflows/.gitkeep",
    "Technical-File-MDAI/.github/ISSUE_TEMPLATE/.gitkeep",
    "Technical-File-MDAI/00_Administrative/01_Regulatory_History/.gitkeep",
    "Technical-File-MDAI/00_Administrative/02_NB_Communications/.gitkeep",
    "Technical-File-MDAI/01_General-Information/01_Manufacturer.yml",
    "Technical-File-MDAI/01_General-Information/02_Device-Description.md",
    "Technical-File-MDAI/01_General-Information/03_CHANGE_HISTORY.md",
    "Technical-File-MDAI/01_General-Information/04_Authorised-Rep.md",
    "Technical-File-MDAI/01_General-Information/05_UDI-Strategy.md",
    "Technical-File-MDAI/02_QMS-Links/ISO13485_Procedures/.gitkeep",
    "Technical-File-MDAI/02_QMS-Links/AIA_QMS_Addendum/.gitkeep",
    "Technical-File-MDAI/03_Design-and-Manufacture/01_Software-Architecture/.gitkeep",
    "Technical-File-MDAI/03_Design-and-Manufacture/02_Hardware/.gitkeep",
    "Technical-File-MDAI/03_Design-and-Manufacture/03_Verification-Plan.md",
    "Technical-File-MDAI/03_Design-and-Manufacture/04_Design_Transfer/.gitkeep",
    "Technical-File-MDAI/04_Risk-Management/01_Risk_Plan.md",
    "Technical-File-MDAI/04_Risk-Management/02_HARA.xlsx",
    "Technical-File-MDAI/04_Risk-Management/03_Risk_Report.md",
    "Technical-File-MDAI/05_Clinical-Performance/01_PEP.md",
    "Technical-File-MDAI/05_Clinical-Performance/02_Data_Governance.md",
    "Technical-File-MDAI/05_Clinical-Performance/03_Study_Reports/.gitkeep",
    "Technical-File-MDAI/06_Verification-and_Validation/01_Software_Test_Protocol/.gitkeep",
    "Technical-File-MDAI/06_Verification-and_Validation/02_ML_Model_Validation.md",
    "Technical-File-MDAI/06_Verification-and_Validation/03_Cybersecurity_Test.md",
    "Technical-File-MDAI/06_Verification-and_Validation/04_Usability/.gitkeep",
    "Technical-File-MDAI/07_Operations/01_Service_Monitoring/.gitkeep",
    "Technical-File-MDAI/07_Operations/02_Product_Release/.gitkeep",
    "Technical-File-MDAI/07_Operations/03_DevOps_Scripts/.gitkeep",
    "Technical-File-MDAI/08_Post-Market/01_PMS_Plan.md",
    "Technical-File-MDAI/08_Post-Market/02_PMS_Report_Template.md",
    "Technical-File-MDAI/08_Post-Market/03_PMCF_Protocol.md",
    "Technical-File-MDAI/09_Labels-and_IFU/IFU_en.md",
    "Technical-File-MDAI/09_Labels-and_IFU/IFU_es.md",
    "Technical-File-MDAI/09_Labels-and_IFU/Marketing/.gitkeep",
    "Technical-File-MDAI/09_Labels-and_IFU/eIFU_Validation.md",
    "Technical-File-MDAI/10_Conformity/01_GSPR_Checklist.xlsx",
    "Technical-File-MDAI/10_Conformity/02_Declaration_of_Conformity.md",
    "Technical-File-MDAI/10_Conformity/03_NotifiedBody_Certs/.gitkeep",
    "Technical-File-MDAI/docs/.gitkeep"
]

def create_file(path, content=""):
    url = f"{API}/repos/{REPO}/contents/{path}"
    data = {
        "message": COMMIT_MESSAGE,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": "main",
        "committer": COMMIT_AUTHOR,
        "author": COMMIT_AUTHOR,
    }
    r = requests.put(url, headers=HEADERS, data=json.dumps(data))
    if r.status_code not in (201, 422):
        print(f"Error creating {path}: {r.status_code} {r.text}")
    else:
        print(f"Created: {path}")

for p in paths:
    create_file(p)
