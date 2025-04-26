import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .transformations import transform_and_save_to_output

from django.views.decorators.csrf import csrf_exempt
from .models import Input, Output, Reference

def home(request):
    if request.method == "GET":
        return HttpResponse("<h1>Welcome</h1>")

def import_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return HttpResponse("No file uploaded.", status=400)

        #Files.objects.create(file=uploaded_file)

        try:
            # Read the uploaded file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            else:
                return HttpResponse("Unsupported file format.", status=400)

            columns = df.columns.str.lower()  # Convert column headers to lowercase

            if {'field1', 'field2', 'field3', 'field4', 'field5', 'refkey1', 'refkey2'}.issubset(columns):
                # It's an Input file
                input_objects = [
                    Input(
                        field1=row['field1'],
                        field2=row['field2'],
                        field3=row['field3'],
                        field4=row['field4'],
                        field5=row['field5'],
                        refkey1=row['refkey1'],
                        refkey2=row['refkey2']
                    ) for _, row in df.iterrows()
                ]
                Input.objects.bulk_create(input_objects)
                return HttpResponse("Input file imported successfully!")

            elif {'refkey1', 'refdata1', 'refkey2', 'refdata2', 'refdata3', 'refdata4'}.issubset(columns):
                # It's a Reference file
                reference_objects = [
                    Reference(
                        refkey1=row['refkey1'],
                        refdata1=row['refdata1'],
                        refkey2=row['refkey2'],
                        refdata2=row['refdata2'],
                        refdata3=row['refdata3'],
                        refdata4=row['refdata4']
                    ) for _, row in df.iterrows()
                ]
                Reference.objects.bulk_create(reference_objects)
                return HttpResponse("Reference file imported successfully!")

            else:
                return HttpResponse("Unknown file structure. Please check headers.", status=400)

        except Exception as e:
            return HttpResponse(f"Error occurred: {e}", status=500)

    return render(request, 'main.html')

def export_output(request, format):
    outputs = Output.objects.all()
    if not outputs.exists():
        return JsonResponse({"error": "No output data available to export."}, status=400)
    
    df = pd.DataFrame(list(outputs.values('outfield1', 'outfield2', 'outfield3', 'outfield4', 'outfield5')))

    if format == 'json':
        return JsonResponse({
            "status": "success",
            "message": "Export successful",
            "data": df.to_dict(orient='records')
        }, safe=False)
    else:
        # For file downloads, return the file but add a success flag
        response = None
        if format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="output.csv"'
            df.to_csv(path_or_buf=response, index=False)
        elif format == 'xlsx':
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="output.xlsx"'
            with pd.ExcelWriter(response, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
        else:
            return JsonResponse({"error": "Unsupported format."}, status=400)
        
        # Add success indication
        response['X-Status'] = 'success'
        return response

@csrf_exempt
def transform_data(request):
    message = transform_and_save_to_output()
    return JsonResponse({"message": message})


