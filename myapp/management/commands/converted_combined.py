import json
from datetime import datetime, timezone
import re

base_file_path = "/Users/karthikreddy/Desktop/IIT_ROORKEE/backend-roorkee/myapp/management/scrapedData"
base_file_path_Scraped_data = "/Users/karthikreddy/Desktop/IIT_ROORKEE/backend-roorkee/myapp/management/Scraped Data"
from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):
    help = 'Converts and combines data into a JSON file'

    def handle(self, *args, **kwargs):
        # Your logic for combining data goes here
        with open('combined_schemes_data.json', 'w') as outfile:
            json.dump(combined_data, outfile, indent=4)
        self.stdout.write(self.style.SUCCESS('Combined data has been successfully saved to combined_schemes_data.json'))


# def current_date():
#     return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def remove_leading_numbers(title):
    # Use a regular expression to remove leading numbers followed by a dot and whitespace
    return re.sub(r'^\d+\.\s*', '', title)
# Helper function to convert date format
def convert_date_format(date_str):
    if date_str:
        try:
            return datetime.strptime(date_str, "%d %b %Y").strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            return None
    return None

# Helper function to determine tags based on scheme title and description
def determine_tags(title, description):
    tags = []
    text = f"{title} {description}".lower()
    if "scholarship" in text:
        tags.append("scholarship")
    if "job" in text or "employment" in text:
        tags.append("job")
    return tags

def transform_and_add_meghalaya_data(original_data, combined_data):
    for item in original_data:
        state_name = "Meghalaya"
        created_at = "2024-06-25T12:00:00Z"
        department_name = item.get("Department: ").strip()
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        title = remove_leading_numbers(item.get("Title: ").strip())
        description = item.get("Description: ").strip()
        scheme = {
            "title": title,
            "introduced_on": convert_date_format(item.get("Introduced on: ")),
            "valid_upto": "2024-12-31T23:59:59Z",
            "funding_pattern": item.get("Sponsors: ").strip(),
            "description": description,
            "scheme_link": item.get("Scheme Link: ").strip(),
            "beneficiaries": [
                {"beneficiary_type": item.get("Scheme Beneficiaries: ").strip()}
            ] if item.get("Scheme Beneficiaries: ") else [],
            "documents": [],
            "sponsors": [
                {"sponsor_type": item.get("Sponsors: ").strip()}
            ],
            "criteria": [
                {"description": item.get("How to Avail: ").strip(), "value": ""}
            ] if item.get("How to Avail: ") else [],
            "procedures": [
                {"step_description": item.get("How to Avail: ").strip()}
            ] if item.get("How to Avail: ") else [],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)

# Function to transform and add Tamil Nadu data
def transform_and_add_tamilnadu_data(original_data, combined_data):
    for item in original_data:
        state_name = "Tamil Nadu"
        created_at = "2024-06-25T12:00:00Z"
        department_name = item.get("Concerned Department").strip()
        organisation_name = item.get("Organisation Name")
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": organisation_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        title = item.get("Title / Name").strip()
        description = item.get("Description").strip()
        scheme = {
            "title": title,
            "introduced_on": convert_date_format(item.get("Introduced On")),
            "valid_upto": "2024-12-31T23:59:59Z",
            "funding_pattern": item.get("Sponsored By"),
            "description": description,
            "scheme_link": item.get("URL"),
            "beneficiaries": [
                {"beneficiary_type": item.get("Beneficiaries")}
            ] if item.get("Beneficiaries") else [],
            "documents": [],
            "sponsors": [
                {"sponsor_type": item.get("Sponsored By")}
            ],
            "criteria": [
                {"description": item.get("How To Avail"), "value": ""}
            ] if item.get("How To Avail") else [],
            "procedures": [
                {"step_description": item.get("How To Avail")}
            ] if item.get("How To Avail") else [],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)

# Function to transform and add Puducherry data
def transform_and_add_puducherry_data(original_data, combined_data):
    for item in original_data:
        state_name = "Puducherry"
        created_at = "2024-06-25T12:00:00Z"
        department_name = "Adi Dravidar Welfare Department"
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        title = remove_leading_numbers(item.get("title").strip())
        description = " ".join(item["details"].get("Objective", [])).strip()
        scheme = {
            "title": title,
            "introduced_on": "2024-06-25T12:00:00Z",
            "valid_upto": "2024-12-31T23:59:59Z",
            "funding_pattern": "State",
            "description": description,
            "scheme_link": item.get("link"),
            "beneficiaries": [
                {"beneficiary_type": "SC/ST/OEBC"}
            ],
            "documents": [
                {"document_name": doc} for doc in item["details"].get("Required Documents / Enclosures with Application", [])
            ],
            "sponsors": [
                {"sponsor_type": "State"}
            ],
            "criteria": [
                {"description": eligibility, "value": ""} for eligibility in item["details"].get("Eligibility", [])
            ],
            "procedures": [],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)

# Function to transform and add Jammu and Kashmir data
def transform_and_add_jammukashmir_data(original_data, combined_data):
    for program in original_data:
        state_name = "Jammu and Kashmir"
        created_at = "2024-06-25T12:00:00Z"
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department_name = program.get("title").strip()
        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        for item in program.get("schemes", []):
            title = remove_leading_numbers(item.get("name").strip())
            description = item["details"].get("Description of the Scheme", "").strip()
            scheme = {
                "title": title,
                "introduced_on": "2024-06-25T12:00:00Z",
                "valid_upto": "2024-12-31T23:59:59Z",
                "funding_pattern": "Central and State",
                "description": description,
                "scheme_link": item.get("url"),
                "beneficiaries": [
                    {"beneficiary_type": item["criteria"].get("Category")}
                ] if item.get("criteria") else [],
                "documents": [],
                "sponsors": [
                    {"sponsor_type": "Central and State"}
                ],
                "criteria": [
                    {"description": key + ": " + value} for key, value in item["criteria"].items()
                ] if item.get("criteria") else [],
                "procedures": [
                    {"step_description": item["details"].get("Procedure", "")}
                ] if item.get("details") else [],
                "tags": determine_tags(title, description)
            }
            organisation["schemes"].append(scheme)

def transform_and_add_gujarat_data(original_data, combined_data):
    for item in original_data:
        state_name = "Gujarat"
        created_at = "2024-06-25T12:00:00Z"
        department_name = "Scheduled Caste Welfare Department"
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        title = remove_leading_numbers(item.get("title").strip())
        description = item["details"].get("Scheme Name")
        scheme = {
            "title": title,
            "introduced_on": "2024-06-25T12:00:00Z",
            "valid_upto": "2024-12-31T23:59:59Z",
            "funding_pattern": "State",
            "description": description,
            "scheme_link": item["details"].get("scheme_link"),

            "beneficiaries": [
                {"beneficiary_type": "SC"}
            ],
            "documents": [
                {"document_name": "Pre-defined Application Form", "description": item["details"].get("Pre-defined Application Form")}
            ],
            "sponsors": [
                {"sponsor_type": "State"}
            ],
            "criteria": [
                {"description": item["details"].get("Eligibility Criteria :"), "value": ""}
            ],
            "procedures": [
                {"step_description": item["details"].get("Assistance Details", "").split("\n")[0]}
            ],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)
    

def transform_and_add_maharashtra_data(original_data, combined_data):
    state_name = "Maharashtra"
    created_at = "2024-06-25T12:00:00Z"

    for item in original_data:
        title = remove_leading_numbers(item["details"].get("Name of the Scheme", "").strip())
        scheme_id = item.get("id", "")

        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department_name = item["details"].get("Category of Scheme", "").strip()
        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        description = item["details"].get("Scheme Objective", "").strip()

        scheme = {
            "title": title,
            "introduced_on": None if item["details"].get("Introduced On", "").strip() == "" else item["details"]["Introduced On"].strip(),
            "valid_upto": None if item["details"].get("Valid Upto", "").strip() == "" else item["details"]["Valid Upto"].strip(),
            "funding_pattern": item["details"].get("Funding by", "").strip(),
            "description": description,
            "scheme_link": item["details"].get("scheme_link"),  # This data is not provided in the example, adjust as needed
            "beneficiaries": [
                {"beneficiary_type": item["details"].get("Beneficiary Category", "").strip()}
            ],
            "documents": [],  # You may need to adjust this based on available data
            "sponsors": [],  # This data is not provided in the example, adjust as needed
            "criteria": [
                {"description": item["details"].get("Eligibility Criteria", ""), 
                 "value": ""}
            ],
            "procedures": [
                {"step_description": item["details"].get("Application Process", "").strip()}
            ],
            "tags": determine_tags(title, description),  # Implement determine_tags function
            "statistical_summary": []  # Exclude 'year' field from statistical summary
        }
        organisation["schemes"].append(scheme)


def transform_and_add_uttar_pradesh_data(original_data, combined_data):
    for item in original_data:
        state_name = "Uttar Pradesh"
        created_at = "2024-06-25T12:00:00Z"
        department_name = "उत्तर प्रदेश सरकार"
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        title = remove_leading_numbers(item.get("title").strip())
        scheme_link = item.get("scheme_link")
        description = item.get("description")
        scheme = {
            "title": title,
            "introduced_on": convert_date_format(item.get("introduced_on")),
            "valid_upto": convert_date_format(item.get("valid_upto")),
            "funding_pattern": item.get("funding_pattern"),
            "description": description,
            "scheme_link": scheme_link,
            
            "beneficiaries": [
                {"beneficiary_type": beneficiary} for beneficiary in item.get("beneficiaries", [])
            ],
            "sponsors": [
                {"sponsor_type": sponsor} for sponsor in item.get("sponsors", [])
            ],
            "criteria": [
                {"description": criterion, "value": ""} for criterion in item.get("criteria", [])
            ],
            "procedures": [
                {"step_description": step} for step in item.get("procedures", [])
            ],
            "tags": determine_tags(title, description),
            "benefits": [
                {"benefit_type": benefit} for benefit in item.get("benefits", [])
            ],
            "criteria": [
                {"description": eligibility} for eligibility in item.get("eligibility", [])
            ],
            "application_process": [
                {"step_description": step} for step in item.get("application_process", [])
            ],
            "documents": [
                {"document_name": requirement} for requirement in item.get("requirements", [])
            ]
        }
        organisation["schemes"].append(scheme)

def transform_and_add_himachal_pradesh_data(original_data, combined_data):
    for item in original_data:
        state_name = "Himachal Pradesh"
        created_at = "2024-06-25T12:00:00Z"
        department_name = "other"
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        title = remove_leading_numbers(item.get("name").strip())
        description = item.get("objective")
        scheme = {
            "title": title,
            "introduced_on": convert_date_format(item.get("Introduced on: ")),
            "valid_upto": "2024-12-31T23:59:59Z",
            "funding_pattern": item.get("Sponsors: "),
            "description": description,
            "scheme_link": item.get("applyOnlineLink"),
            "beneficiaries": [
                {"beneficiary_type": item.get("Scheme Beneficiaries: ").strip()}
            ] if item.get("Scheme Beneficiaries: ") else [],
            "documents": [],
            "sponsors": [
                {"sponsor_type": item.get("Sponsors: ")}
            ],
            "criteria": [
                {"description": item.get("eligibility")}
                ],
            "procedures": [
                {"step_description": item.get("process")}
                ],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)

def transform_and_add_manipur_data(original_data, combined_data):
    state_name = "Manipur"
    created_at = "2024-06-25T12:00:00Z"

    for item in original_data:
        title = remove_leading_numbers(item.get("title", "").strip())
        scheme_id = item.get("id", "")

        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department_name = item.get("Category of Scheme", "").strip()
        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        description = item.get("Scheme Objective", "").strip()

        scheme = {
            "title": title,
            "introduced_on": None,
            "valid_upto": None if item.get("Valid Upto", "").strip() == "" else item["Valid Upto"].strip(),
            "funding_pattern": item.get("Funding by", "").strip(),
            "description": description,
            "scheme_link": item.get("scheme_link"),  
            "beneficiaries": [
                {"beneficiary_type": item.get("beneficiary", "").strip()}
            ],
            "documents": [], 
            "sponsors": [],  
            "criteria": [
                {"description": item.get("Eligibility Criteria", ""), 
                 "value": ""}
            ],
            "procedures": [
                {"step_description": item.get("howToApply", "").strip()}
            ],
            "benefits": [
                {"benefit_type": item.get("benefits", [])} 
            ],
            "tags": determine_tags(title, description),  # Implement determine_tags function
            "statistical_summary": []  # Exclude 'year' field from statistical summary
        }
        organisation["schemes"].append(scheme)

def transform_and_add_kerala_data(original_data, combined_data):
    state_name = "Kerala"
    created_at = "2024-06-25T12:00:00Z"

    for item in original_data:
        title = remove_leading_numbers(item.get("title", "").strip())

        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department_name = item.get("Category of Scheme", "").strip()
        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": department_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        description = item.get("description", "").strip()

        scheme = {
            "title": title,
            "introduced_on": None,
            "valid_upto": None if item.get("Valid Upto", "").strip() == "" else item["Valid Upto"].strip(),
            "funding_pattern": item.get("Funding by", "").strip(),
            "description": description,
            "scheme_link": item.get("scheme_link"),  
            "beneficiaries": [
                {"beneficiary_type": item.get("beneficiary", "").strip()}
            ],
            "documents": [], 
            "sponsors": [],  
            "criteria": [
                {"description": item.get("Eligibility Criteria", ""), 
                 "value": ""}
            ],
            "procedures": [
                {"step_description": item.get("howToApply", "").strip()}
            ],
            "benefits": [
                {"benefit_type": item.get("benefits", [])} 
            ],
            "tags": determine_tags(title, description),  # Implement determine_tags function
            "statistical_summary": []  # Exclude 'year' field from statistical summary
        }
        organisation["schemes"].append(scheme)

        
def transform_and_add_andhra_pradesh_data(original_data, combined_data):
    for item in original_data:
        state_name = 'Andhra Pradesh'
        created_at = "2024-06-25T12:00:00Z"
        department_name = ''
        organisation_name = ''
        state = next((s for s in combined_data['states'] 
            if s['state_name'] == state_name),None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)
        
        department = next((d for d in state['departments']
            if d["department_name"] == department_name ), None)
        
        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": organisation_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)
        organisation = department["organisations"][0]
        title = item.get("title").strip()
        description = item.get("description").strip()
        scheme = {
            "title": title,
            "introduced_on":"2024-06-25T12:00:00Z",
            "valid_upto": '2024-12-31T23:59:59Z',
            "funding_pattern":"Yet to be updated",
            "description": description,
            "scheme_link": "",
            "beneficiaries":  [
                {"beneficiary_type": item.get("Beneficiaries")}
            ] if item.get("Beneficiaries") else [],
            "documents": [],
            "sponsors": [
                {"sponsor_type":  "Yet to be updated"}
            ],
            "criteria": [
                {"description": item.get("How To Avail"), "value": ""}
            ] if item.get("How To Avail") else [],
            "procedures": [
                {"step_description": item.get("How To Avail")}
            ] if item.get("How To Avail") else [],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)
        

def transform_and_add_assam_data(original_data, combined_data):
    for item in original_data:
        state_name = 'Assam'
        created_at = "2024-06-25T12:00:00Z"
        department_name = ''
        organisation_name = ''
        state = next((s for s in combined_data['states'] 
            if s['state_name'] == state_name),None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)
        
        department = next((d for d in state['departments']
            if d["department_name"] == department_name ), None)
        
        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": organisation_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)
        organisation = department["organisations"][0]
        title = item.get("title").strip()
        description = item.get("description").strip()
        scheme = {
            "id" : item.get("id", ""),
            "title": title,
            "introduced_on":"2024-06-25T12:00:00Z",
            "valid_upto": '2024-12-31T23:59:59Z',
            "funding_pattern":"Yet to be updated",
            "description": description,
            "scheme_link": "Yet to be updated",
            "beneficiaries":  [
                {"beneficiary_type": item.get("Beneficiaries")}
            ] if item.get("Beneficiaries") else [],
            "documents": [],
            "sponsors": [
                {"sponsor_type":  "Yet to be updated"}
            ],
            "criteria": [
                {"description": item.get("How To Avail"), "value": ""}
            ] if item.get("How To Avail") else [],
            "procedures": [
                {"step_description": item.get("How To Avail")}
            ] if item.get("How To Avail") else [],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)
    
def transform_and_add_haryana_data(original_data, combined_data):
    for item in original_data:
        state_name = "Haryana"
        created_at = "2024-06-25T12:00:00Z"
        department_name = ''
        organisation_name = ''
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)
        
        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": organisation_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)

        organisation = department["organisations"][0]
        title = item.get("title").strip()
        description = item.get("description").strip()
        scheme = {
        "title": title,
        "introduced_on": convert_date_format(item.get("publishDate")),
        "valid_upto": "2024-12-31T23:59:59Z",
        "funding_pattern": 'Yet to be Updated',
        "description": description + '\n' + item.get('benefits'),
        "scheme_link": item.get("schemeUrl"),
        "beneficiaries": [
            {"beneficiary_type": item.get("Beneficiaries")}
        ] if item.get("Beneficiaries") else [],
        "documents": [{"document_name": "More details", "description": item.get("pdfUrl")}],
            "sponsors": [
            {"sponsor_type": item.get("Sponsored By")}
        ],
        "criteria": [
            {"description": item.get("howToApply"), "value": ""}
        ] if item.get("howToApply") else [],
        "procedures": [
            {"step_description": item.get("howToApply")}
        ] if item.get("howToApply") else [],
        "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)

def transform_and_add_punjab_data(original_data, combined_data):
    for item in original_data:
        state_name = "Punjab"
        created_at = "2024-06-25T12:00:00Z"
        department_name = ''
        organisation_name = ''
        state = next((s for s in combined_data["states"] if s["state_name"] == state_name), None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)

        department = next((d for d in state["departments"] if d["department_name"] == department_name), None)

        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": organisation_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)
        organisation = department["organisations"][0]
        title = item.get("title").strip()
        description = item.get("Description").strip()
        scheme = {
            "title": title,
            "introduced_on": "2024-06-25T12:00:00Z",
            "valid_upto": "2024-12-31T23:59:59Z",
            "funding_pattern": item.get("FUNDING PATTERN"),
            "description": description,
            "scheme_link": '',
            "beneficiaries": [
                {"beneficiary_type": item.get("Beneficiaries")}
            ] if item.get("Beneficiaries") else [],
            "documents": [],
            "sponsors": [
                {"sponsor_type": item.get("SOURCES OF FUNDS")}
            ],
            "criteria": [
                {"description": item.get("ELIGIBILITY"), "value": ""}
            ] if item.get("ELIGIBILITYl") else [],
            "procedures": [
                {"step_description": item.get("PROCEDURE FOR TAKING LOAN")}
            ] if item.get("PROCEDURE FOR TAKING LOAN") else [],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)

def transform_and_add_odisha_data(original_data, combined_data):
    for item in original_data:
        state_name = 'Odisha'
        created_at = "2024-06-25T12:00:00Z"
        department_name = ''
        organisation_name = ''
        state = next((s for s in combined_data['states'] 
            if s['state_name'] == state_name),None)

        if not state:
            state = {
                "state_name": state_name,
                "created_at": created_at,
                "departments": []
            }
            combined_data["states"].append(state)
        
        department = next((d for d in state['departments']
            if d["department_name"] == department_name ), None)
        
        if not department:
            department = {
                "department_name": department_name,
                "created_at": created_at,
                "organisations": [
                    {
                        "organisation_name": organisation_name,
                        "created_at": created_at,
                        "schemes": []
                    }
                ]
            }
            state["departments"].append(department)
        organisation = department["organisations"][0]
        title = item.get("title").strip()
        description = item.get("description").strip() if item.get("description") else ''
        scheme = {
            "title": title,
            "introduced_on":"2024-06-25T12:00:00Z",
            "valid_upto": '2024-12-31T23:59:59Z',
            "funding_pattern":"",
            "description": description,
            "scheme_link": item.get("schemeUrl"),
            "beneficiaries":  [
                {"beneficiary_type": item.get("Beneficiaries")}
            ] if item.get("Beneficiaries") else [],
            "documents": [],
            "sponsors": [
                {"sponsor_type":  "Yet to be updated"}
            ],
            "criteria": [
                {"description": item.get("How To Avail"), "value": ""}
            ] if item.get("How To Avail") else [],
            "procedures": [
                {"step_description": item.get("How To Avail")}
            ] if item.get("How To Avail") else [],
            "tags": determine_tags(title, description)
        }
        organisation["schemes"].append(scheme)

# Read data from JSON files
with open(base_file_path+"/meghalaya.json", "r") as file:
    meghalaya_data = json.load(file)

with open(base_file_path+"/tamilnadu.json", "r") as file:
    tamilnadu_data = json.load(file)

with open(base_file_path+"/puducherry.json", "r") as file:
    puducherry_data = json.load(file)

with open(base_file_path+"/jammukashmir.json", "r") as file:
    jammukashmir_data = json.load(file)

with open(base_file_path+"/gujratschemes.json", "r") as file:
    gujarat_data = json.load(file)

with open(base_file_path+"/maharastra.json", "r") as file:
    maharashtra_data = json.load(file)

with open(base_file_path+"/up/up_youth_welfare.json", "r") as file:
    up_data = json.load(file)

with open(base_file_path+"/himachalPradesh.json", "r") as file:
    himachal_data = json.load(file)

with open(base_file_path+"/andhra.json", "r") as file:
    andhra_pradesh_data = json.load(file)

with open(base_file_path+"/andhra.json", "r") as file:
    andhra_pradesh_data = json.load(file)

with open(base_file_path_Scraped_data+"/manipur.json", "r") as file:
    manipur_data = json.load(file)
with open(base_file_path+"/kerela.json", "r") as file:
    kerala_data = json.load(file)
with open(base_file_path+"/madhya_pradesh.json", "r") as file:
    madhya_pradesh_data = json.load(file)

with open(base_file_path+"/assam.json", "r") as file:
    assam_data = json.load(file)

with open(base_file_path+"/haryanaSchemes.json", "r") as file:
    haryana_data = json.load(file)

with open(base_file_path+'/punjab.json','r') as file:
    punjab_data = json.load(file)

with open(base_file_path+"/odisha.json", "r") as file:
    odisha_data = json.load(file)

    
# Initialize the combined data structure
combined_data = {
    "states": []
}


# Transform and add data to the combined structure
transform_and_add_meghalaya_data(meghalaya_data, combined_data)
transform_and_add_tamilnadu_data(tamilnadu_data, combined_data)
transform_and_add_puducherry_data(puducherry_data, combined_data)
transform_and_add_jammukashmir_data(jammukashmir_data, combined_data)
transform_and_add_gujarat_data(gujarat_data, combined_data)
transform_and_add_maharashtra_data(maharashtra_data, combined_data)
transform_and_add_uttar_pradesh_data(up_data,combined_data)
transform_and_add_himachal_pradesh_data(himachal_data,combined_data)
transform_and_add_manipur_data(manipur_data, combined_data)
transform_and_add_kerala_data(kerala_data, combined_data)
transform_and_add_andhra_pradesh_data(andhra_pradesh_data,combined_data)
transform_and_add_assam_data(assam_data, combined_data)
transform_and_add_haryana_data(haryana_data, combined_data)
transform_and_add_punjab_data(punjab_data, combined_data)
transform_and_add_odisha_data(odisha_data, combined_data)
combined_data['states'].append(madhya_pradesh_data)

# Save the combined data to a new JSON file
with open(base_file_path+"/combined_schemes_data.json", "w") as file:
    json.dump(combined_data, file,ensure_ascii=False, indent=4)

print("Combined data has been successfully saved to combined_schemes_data.json")