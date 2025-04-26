import pandas as pd
from .models import Output
from decimal import Decimal, InvalidOperation

def safe_decimal(val):
    try:
        return Decimal(str(val).strip())
    except (InvalidOperation, ValueError, TypeError):
        return Decimal(0)

def safe_number(val):
    try:
        val = str(val).strip()
        if val == '' or val.lower() == 'nan':
            return 0.0
        return float(val)
    except (ValueError, TypeError):
        return 0.0


def transform_and_save_to_output():
    from .models import Input, Reference

    input_qs = Input.objects.all()
    reference_qs = Reference.objects.all()

    if not input_qs.exists() or not reference_qs.exists():
        return "Input or Reference data not found."

    input_df = pd.DataFrame(list(input_qs.values()))
    reference_df = pd.DataFrame(list(reference_qs.values()))

    # Merge
    merged_df = pd.merge(input_df, reference_df, how='left', on=['refkey1', 'refkey2'])

    # Transformation
    outputs = []

    for _, row in merged_df.iterrows():
        field1 = str(row.get('field1', ''))
        field2 = str(row.get('field2', ''))
        refdata1 = str(row.get('refdata1', ''))
        refdata2 = str(row.get('refdata2', ''))
        refdata3 = str(row.get('refdata3', ''))

        field3 = safe_number(row.get('field3'))
        field5 = safe_number(row.get('field5'))    # changed to safe_number
        refdata4 = safe_number(row.get('refdata4')) # changed to safe_number

        max_val = max(field5, refdata4)

        output = Output(
            outfield1 = field1 + field2,
            outfield2 = refdata1,
            outfield3 = refdata2 + refdata3,
            outfield4 = str(field3 * max_val),   # now both are float
            outfield5 = str(max_val)
        )
        outputs.append(output)

    Output.objects.bulk_create(outputs)
    return "Transformation and Saving completed successfully!"
