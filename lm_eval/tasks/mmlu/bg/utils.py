import datasets

def filter_subject(dataset: datasets.Dataset, subject: str) -> datasets.Dataset:
    return dataset.filter(lambda example: example["subject"] == subject)

def filter_abstract_algebra(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "abstract_algebra")

def filter_anatomy(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "anatomy")

def filter_astronomy(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "astronomy")

def filter_business_ethics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "business_ethics")

def filter_clinical_knowledge(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "clinical_knowledge")

def filter_college_biology(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "college_biology")

def filter_college_chemistry(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "college_chemistry")

def filter_college_computer_science(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "college_computer_science")

def filter_college_mathematics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "college_mathematics")

def filter_college_medicine(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "college_medicine")

def filter_college_physics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "college_physics")

def filter_computer_security(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "computer_security")

def filter_conceptual_physics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "conceptual_physics")

def filter_econometrics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "econometrics")

def filter_electrical_engineering(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "electrical_engineering")

def filter_elementary_mathematics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "elementary_mathematics")

def filter_formal_logic(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "formal_logic")

def filter_global_facts(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "global_facts")

def filter_high_school_biology(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_biology")

def filter_high_school_chemistry(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_chemistry")

def filter_high_school_computer_science(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_computer_science")

def filter_high_school_european_history(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_european_history")

def filter_high_school_geography(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_geography")

def filter_high_school_government_and_politics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_government_and_politics")

def filter_high_school_macroeconomics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_macroeconomics")

def filter_high_school_mathematics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_mathematics")

def filter_high_school_microeconomics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_microeconomics")

def filter_high_school_physics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_physics")

def filter_high_school_psychology(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_psychology")

def filter_high_school_statistics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_statistics")

def filter_high_school_us_history(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_us_history")

def filter_high_school_world_history(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "high_school_world_history")

def filter_human_aging(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "human_aging")

def filter_human_sexuality(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "human_sexuality")

def filter_international_law(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "international_law")

def filter_jurisprudence(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "jurisprudence")

def filter_logical_fallacies(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "logical_fallacies")

def filter_machine_learning(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "machine_learning")

def filter_management(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "management")

def filter_marketing(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "marketing")

def filter_medical_genetics(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "medical_genetics")

def filter_miscellaneous(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "miscellaneous")

def filter_moral_disputes(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "moral_disputes")

def filter_moral_scenarios(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "moral_scenarios")

def filter_nutrition(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "nutrition")

def filter_philosophy(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "philosophy")

def filter_prehistory(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "prehistory")

def filter_professional_accounting(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "professional_accounting")

def filter_professional_law(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "professional_law")

def filter_professional_medicine(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "professional_medicine")

def filter_professional_psychology(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "professional_psychology")

def filter_public_relations(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "public_relations")

def filter_security_studies(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "security_studies")

def filter_sociology(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "sociology")

def filter_us_foreign_policy(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "us_foreign_policy")

def filter_virology(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "virology")

def filter_world_religions(dataset: datasets.Dataset) -> datasets.Dataset:
    return filter_subject(dataset, "world_religions")
